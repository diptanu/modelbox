<p align="center"><img src="https://raw.githubusercontent.com/diptanu/modelbox/main/docs/images/ModelBox1.png" width="300" height="150"></p>

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/diptanu/modelbox/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/diptanu/modelbox/tree/main)

# AI Model Operations and Metadata Management Service

ModelBox is an AI models and metadata management service. 

It can integrate with Deep Learning frameworks to provide model checkpoint and artifact tracking. Optional features include serving AI models to inference engines and measuring their performance. 

Additionally, ModelBox provides a pluggable storage interface to track metadata & artifacts related to models, and experiments producing checkpoints. 

## Features
- Python SDK to integrate with custom PyTorch (or any other ML framework) trainer.
- Model versioning and lineage tracking of Models in relation to Experiments which created them.
- Labelling models and checkpoints to track the environment they are deployed in, metrics, and other related metadata meaningful to users.
- Integrates transparenly with DL Frameworks like PyTorch Lightning for checkpoint storage/retrieval, metadata and metrics logging.
- Load production ready models in inference engines directly from ModelBox - clients in Python, Go, etc. Rust and C++ library are in the works.

## Planned Features
- Add retention policies written in any WASM compatible language which has all the model and checkpoint related metadata available.
- Add RBAC based access control for models and checkpoints for compliance.
- Create a worker infrastructure which automatically transforms models, benchmarks for performance on inference hardware, etc, and update the model metadata.
- Make the worker architecture pluggable such that users can write custom workers any language while the model, metrics and other metadata are available to the runtime, abstracting the storage and other infrastructure primitives.
- Build Model Explainability features, such as exctracting information about shape of input and output tensors, types of layers used by the model, parameter counts, etc.
- Build infrastructure to run known recipes for model optimazation for inference such as Layer Fusion, replacing transformer layers with more optimized implemenations such as Faster Transformer, quantization, model compression, etc.
- Beyond being able to stream a model binary using the streaming api, build exporters which are more native to model deployment.


## Tutorials and Demos
If you would like to jump straight in, we have some notebooks which demonstrates the usage of the Python SDK independently and with Pytorch and Pytorch Lightning.
- [Pytorch SDK Tutorial](tutorials/Tutorial_Python_SDK.ipynb) 
- [Pytorch Lightning Integration](tutorials/Pytorch_Lightning_Integration_Tutorial.ipynb) 
- [Pytorch Tutorial](tutorials/Tutorial_Pytorch.ipynb) * Work In Progress * 

## Concepts and Understanding the ModelBox API
![Model Box Concepts!](docs/images/API_Concepts.png "Model Box API Concepts")

### Namespace
A Namespace is a mechanism to organize related models or models published by a team. They are also use for access control and such to the metadata of uploaded models, invoking benchmarks or other model transformation work. Namespaces are automatically created when a new model or experieemnt specifies the namespace it wants to be associated with.

### Model
A model is an object to track common metadata, and to apply policies on models created by experiments to solve a machine learning task. For ex. datasets to evaluate all trained models of a task can be tracked using this object. Users can also add rules around retention policies of trained versions, setup policies for labelling a trained model if it has better metrics on a dataset, and meets all other criterion.

### Model Version
A model version is a trained model, it includes the model binary, related files that a user wants to track - dataset file handles, any other metadata, model metrics, etc. Model versions are always related to a Model and all the policies created for a Model are applied to Model Versions.

### Experiment and Checkpoints
Experiments are used to ingest model checkpoints created during a training run. ModelBox is not an experiment metadata tracker so there is no support for rich experiment management which are available on experiment trackers such as Weights and Biases, the experiment abstraction here exists so that we can track and ingest model checkpoints which eventually become model versions if they have good metrics and does well in benchmarks.

## Architecture
ModelBox has the following components
- Metadata Server
- Blob Server
- Cli
- Client Libraries 

### Metadata Server
Meta Data Server is responsible for tracking metadata around models which are created by the training frameworks or users who are uploading trained models and other training artifacts. The Meta Data server exposes a GRPC endpoint for clients to communicate with the server. The metadata server has a pluggable architecture to allow using various databases such as MySQL, PostGres, etc. Additional datastore support can be very easily added by implementing the metadata storage inferface.

### Blob Server
Blob Server exposes APIs for clients to upload training artifacts and download models in a streaming fashion across a large number of storage services. The Blob Servers are stateless and hence you can scale them based on your serving needs. You can create dedicate serving capabilities for certain training workloads or for streaming models to production inference servers for example.
Blob Serves have pluggable storage which allows using various backends such as File System based services like NAS or NFS or Cloud Blob Storage services such as S3.

Blob Servers are optional, and users are free to use whichever blob serving capabilites they already have. But, for advanced features such as loading models directly from inference engines, transforming models by ModelBox workers, the blob servers are required as they provide an uniform API to store and retrieve models.

### Cli
The ModelBox CLI provides an interface to interact with the Metadata API and Blob Storage API and create and download models and all other aspects of the service.

### SDK and Client Libraries
The SDK/client libraries are meant for integration with Deep Learning and ML frameworks to integrate ModelBox with the experiment code which creates the model and other training artifacts. The libraries can also be used with applications or control planes which wants to use ModelBox in a larger in house Machine Learning platform.

### High Level Architecture
![Model Box High Level Architecture!](docs/images/ModelBox_HighLevel.png "Model Box High Level Architecture")


## Configuration
ModelBox Server and Cli are configured by toml files and same configuration can be generated by the CLI. Please refer to the comments on the config and the documentation below to understand what the attributes of the configuration does.

```
modelbox server init-config
```

### Server Configuration
- `listen_addr`: The interface and port on which the server will be listening for Client RPC Requests.

#### Storage Configuration
- metadata_storage: The name of the storage backend which ModelBox is going to use for storing metadata about models. Possible values - 
    - `mysql`
         `Host` Host of the MySQL server.
         `Port` Port of the MySQL server.
         `Password` Password of the server.
    - `integrated`

### Cli Configuration

```
modelbox client init-config
```

- `server_addr`: The address of the Metadata Server

## Deployment

All the components of ModelBox is packaged in a single binary which eases deployment in production. 

## Operation Examples

### Starting the metadata server
Generate the config
```
modelbox server init-config
```

Edit the config and start the server

```
$ modelbox server start --config-path ./path/to/modelbox.toml
```

### CLI Examples
Generate the client config
```
modelbox client init-config
```

Create an experiment. Experiments are usually created programatically via the modelbox SDK which integrates with deep learning frameworks.
```
modelbox client experiments create --namespace langtech --owner your@email.com --name wav2vec-lid --framework pytorch
```

List Experiments for a namespace
```
modelbox client experiments list --namespace langtech
```

Create a Model for the experiment. The cli doesn't support adding metadata and artifacts yet, however the Python, Go SDKs does.
```
modelbox client models create --name wav2vec --owner diptanuc@gmail.com --task asr --description English ASR --namespace langtech 
```

List Models in a namespace
```
modelbox client list --namespace langtech
```

## Development
Build the modelbox control plane and cli locally -
```
go install ./cmd/modelbox/
```
or 
```
go build -o /path/to/binary ./cmd/modelbox/
```
Install the python SDK locally for development -
```
cd client-py
pip install .
```

## Monitoring
Metrics on the metadata server is exposed by the `/metrics` endpoint and can be collected by a Prometheus collector.
The default port for the endpoint is `:2112` and can be configured in the server config.
