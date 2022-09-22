# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import service_pb2 as service__pb2


class ModelStoreStub(object):
    """*
    ModelStore is the service exposed to upload trained models and training
    checkpoints, and manage metadata around them.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateModel = channel.unary_unary(
                '/modelbox.ModelStore/CreateModel',
                request_serializer=service__pb2.CreateModelRequest.SerializeToString,
                response_deserializer=service__pb2.CreateModelResponse.FromString,
                )
        self.ListModels = channel.unary_unary(
                '/modelbox.ModelStore/ListModels',
                request_serializer=service__pb2.ListModelsRequest.SerializeToString,
                response_deserializer=service__pb2.ListModelsResponse.FromString,
                )
        self.CreateModelVersion = channel.unary_unary(
                '/modelbox.ModelStore/CreateModelVersion',
                request_serializer=service__pb2.CreateModelVersionRequest.SerializeToString,
                response_deserializer=service__pb2.CreateModelVersionResponse.FromString,
                )
        self.ListModelVersions = channel.unary_unary(
                '/modelbox.ModelStore/ListModelVersions',
                request_serializer=service__pb2.ListModelVersionsRequest.SerializeToString,
                response_deserializer=service__pb2.ListModelVersionsResponse.FromString,
                )
        self.CreateExperiment = channel.unary_unary(
                '/modelbox.ModelStore/CreateExperiment',
                request_serializer=service__pb2.CreateExperimentRequest.SerializeToString,
                response_deserializer=service__pb2.CreateExperimentResponse.FromString,
                )
        self.ListExperiments = channel.unary_unary(
                '/modelbox.ModelStore/ListExperiments',
                request_serializer=service__pb2.ListExperimentsRequest.SerializeToString,
                response_deserializer=service__pb2.ListExperimentsResponse.FromString,
                )
        self.GetExperiment = channel.unary_unary(
                '/modelbox.ModelStore/GetExperiment',
                request_serializer=service__pb2.GetExperimentRequest.SerializeToString,
                response_deserializer=service__pb2.GetExperimentResponse.FromString,
                )
        self.CreateCheckpoint = channel.unary_unary(
                '/modelbox.ModelStore/CreateCheckpoint',
                request_serializer=service__pb2.CreateCheckpointRequest.SerializeToString,
                response_deserializer=service__pb2.CreateCheckpointResponse.FromString,
                )
        self.ListCheckpoints = channel.unary_unary(
                '/modelbox.ModelStore/ListCheckpoints',
                request_serializer=service__pb2.ListCheckpointsRequest.SerializeToString,
                response_deserializer=service__pb2.ListCheckpointsResponse.FromString,
                )
        self.GetCheckpoint = channel.unary_unary(
                '/modelbox.ModelStore/GetCheckpoint',
                request_serializer=service__pb2.GetCheckpointRequest.SerializeToString,
                response_deserializer=service__pb2.GetCheckpointResponse.FromString,
                )
        self.UploadFile = channel.stream_unary(
                '/modelbox.ModelStore/UploadFile',
                request_serializer=service__pb2.UploadFileRequest.SerializeToString,
                response_deserializer=service__pb2.UploadFileResponse.FromString,
                )
        self.DownloadFile = channel.unary_stream(
                '/modelbox.ModelStore/DownloadFile',
                request_serializer=service__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=service__pb2.DownloadFileResponse.FromString,
                )
        self.UpdateMetadata = channel.unary_unary(
                '/modelbox.ModelStore/UpdateMetadata',
                request_serializer=service__pb2.UpdateMetadataRequest.SerializeToString,
                response_deserializer=service__pb2.UpdateMetadataResponse.FromString,
                )
        self.ListMetadata = channel.unary_unary(
                '/modelbox.ModelStore/ListMetadata',
                request_serializer=service__pb2.ListMetadataRequest.SerializeToString,
                response_deserializer=service__pb2.ListMetadataResponse.FromString,
                )
        self.TrackArtifacts = channel.unary_unary(
                '/modelbox.ModelStore/TrackArtifacts',
                request_serializer=service__pb2.TrackArtifactsRequest.SerializeToString,
                response_deserializer=service__pb2.TrackArtifactsResponse.FromString,
                )
        self.LogMetrics = channel.unary_unary(
                '/modelbox.ModelStore/LogMetrics',
                request_serializer=service__pb2.LogMetricsRequest.SerializeToString,
                response_deserializer=service__pb2.LogMetricsResponse.FromString,
                )
        self.GetMetrics = channel.unary_unary(
                '/modelbox.ModelStore/GetMetrics',
                request_serializer=service__pb2.GetMetricsRequest.SerializeToString,
                response_deserializer=service__pb2.GetMetricsResponse.FromString,
                )
        self.LogEvent = channel.unary_unary(
                '/modelbox.ModelStore/LogEvent',
                request_serializer=service__pb2.LogEventRequest.SerializeToString,
                response_deserializer=service__pb2.LogEventResponse.FromString,
                )
        self.ListEvents = channel.unary_unary(
                '/modelbox.ModelStore/ListEvents',
                request_serializer=service__pb2.ListEventsRequest.SerializeToString,
                response_deserializer=service__pb2.ListEventsResponse.FromString,
                )
        self.WatchNamespace = channel.unary_stream(
                '/modelbox.ModelStore/WatchNamespace',
                request_serializer=service__pb2.WatchNamespaceRequest.SerializeToString,
                response_deserializer=service__pb2.WatchNamespaceResponse.FromString,
                )


class ModelStoreServicer(object):
    """*
    ModelStore is the service exposed to upload trained models and training
    checkpoints, and manage metadata around them.
    """

    def CreateModel(self, request, context):
        """Create a new Model under a namespace. If no namespace is specified, models
        are created under a default namespace.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListModels(self, request, context):
        """List Models uploaded for a namespace 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateModelVersion(self, request, context):
        """Creates a new model version for a model
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListModelVersions(self, request, context):
        """Lists model versions for a model.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateExperiment(self, request, context):
        """Creates a new experiment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExperiments(self, request, context):
        """List Experiments
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExperiment(self, request, context):
        """Get Experiments
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCheckpoint(self, request, context):
        """Uploads a new checkpoint for an experiment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCheckpoints(self, request, context):
        """Lists all the checkpoints for an experiment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCheckpoint(self, request, context):
        """Gets a checkpoint from the modelstore for an experiment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFile(self, request_iterator, context):
        """UploadFile streams a files to ModelBox and stores the binaries to the condfigured storage
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """DownloadFile downloads a file from configured storage
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMetadata(self, request, context):
        """Persists a set of metadata related to objects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMetadata(self, request, context):
        """Lists metadata associated with an object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrackArtifacts(self, request, context):
        """Tracks a set of artifacts with a experiment/checkpoint/model
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LogMetrics(self, request, context):
        """Log Metrics for an experiment, model or checkpoint
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetrics(self, request, context):
        """Get metrics logged for an experiment, model or checkpoint.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LogEvent(self, request, context):
        """Log an event from any system interacting with metadata of a experiment, models or
        using a trained model or checkpoint.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEvents(self, request, context):
        """List events logged for an experiment/model, etc.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchNamespace(self, request, context):
        """Streams change events in any of objects such as experiments, models, etc, for a given namespace
        Response is a json representation of the new state of the obejct
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateModel': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateModel,
                    request_deserializer=service__pb2.CreateModelRequest.FromString,
                    response_serializer=service__pb2.CreateModelResponse.SerializeToString,
            ),
            'ListModels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListModels,
                    request_deserializer=service__pb2.ListModelsRequest.FromString,
                    response_serializer=service__pb2.ListModelsResponse.SerializeToString,
            ),
            'CreateModelVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateModelVersion,
                    request_deserializer=service__pb2.CreateModelVersionRequest.FromString,
                    response_serializer=service__pb2.CreateModelVersionResponse.SerializeToString,
            ),
            'ListModelVersions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListModelVersions,
                    request_deserializer=service__pb2.ListModelVersionsRequest.FromString,
                    response_serializer=service__pb2.ListModelVersionsResponse.SerializeToString,
            ),
            'CreateExperiment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateExperiment,
                    request_deserializer=service__pb2.CreateExperimentRequest.FromString,
                    response_serializer=service__pb2.CreateExperimentResponse.SerializeToString,
            ),
            'ListExperiments': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExperiments,
                    request_deserializer=service__pb2.ListExperimentsRequest.FromString,
                    response_serializer=service__pb2.ListExperimentsResponse.SerializeToString,
            ),
            'GetExperiment': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExperiment,
                    request_deserializer=service__pb2.GetExperimentRequest.FromString,
                    response_serializer=service__pb2.GetExperimentResponse.SerializeToString,
            ),
            'CreateCheckpoint': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCheckpoint,
                    request_deserializer=service__pb2.CreateCheckpointRequest.FromString,
                    response_serializer=service__pb2.CreateCheckpointResponse.SerializeToString,
            ),
            'ListCheckpoints': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCheckpoints,
                    request_deserializer=service__pb2.ListCheckpointsRequest.FromString,
                    response_serializer=service__pb2.ListCheckpointsResponse.SerializeToString,
            ),
            'GetCheckpoint': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCheckpoint,
                    request_deserializer=service__pb2.GetCheckpointRequest.FromString,
                    response_serializer=service__pb2.GetCheckpointResponse.SerializeToString,
            ),
            'UploadFile': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=service__pb2.UploadFileRequest.FromString,
                    response_serializer=service__pb2.UploadFileResponse.SerializeToString,
            ),
            'DownloadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=service__pb2.DownloadFileRequest.FromString,
                    response_serializer=service__pb2.DownloadFileResponse.SerializeToString,
            ),
            'UpdateMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMetadata,
                    request_deserializer=service__pb2.UpdateMetadataRequest.FromString,
                    response_serializer=service__pb2.UpdateMetadataResponse.SerializeToString,
            ),
            'ListMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMetadata,
                    request_deserializer=service__pb2.ListMetadataRequest.FromString,
                    response_serializer=service__pb2.ListMetadataResponse.SerializeToString,
            ),
            'TrackArtifacts': grpc.unary_unary_rpc_method_handler(
                    servicer.TrackArtifacts,
                    request_deserializer=service__pb2.TrackArtifactsRequest.FromString,
                    response_serializer=service__pb2.TrackArtifactsResponse.SerializeToString,
            ),
            'LogMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.LogMetrics,
                    request_deserializer=service__pb2.LogMetricsRequest.FromString,
                    response_serializer=service__pb2.LogMetricsResponse.SerializeToString,
            ),
            'GetMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetrics,
                    request_deserializer=service__pb2.GetMetricsRequest.FromString,
                    response_serializer=service__pb2.GetMetricsResponse.SerializeToString,
            ),
            'LogEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.LogEvent,
                    request_deserializer=service__pb2.LogEventRequest.FromString,
                    response_serializer=service__pb2.LogEventResponse.SerializeToString,
            ),
            'ListEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEvents,
                    request_deserializer=service__pb2.ListEventsRequest.FromString,
                    response_serializer=service__pb2.ListEventsResponse.SerializeToString,
            ),
            'WatchNamespace': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchNamespace,
                    request_deserializer=service__pb2.WatchNamespaceRequest.FromString,
                    response_serializer=service__pb2.WatchNamespaceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'modelbox.ModelStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ModelStore(object):
    """*
    ModelStore is the service exposed to upload trained models and training
    checkpoints, and manage metadata around them.
    """

    @staticmethod
    def CreateModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/CreateModel',
            service__pb2.CreateModelRequest.SerializeToString,
            service__pb2.CreateModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListModels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/ListModels',
            service__pb2.ListModelsRequest.SerializeToString,
            service__pb2.ListModelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateModelVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/CreateModelVersion',
            service__pb2.CreateModelVersionRequest.SerializeToString,
            service__pb2.CreateModelVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListModelVersions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/ListModelVersions',
            service__pb2.ListModelVersionsRequest.SerializeToString,
            service__pb2.ListModelVersionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateExperiment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/CreateExperiment',
            service__pb2.CreateExperimentRequest.SerializeToString,
            service__pb2.CreateExperimentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListExperiments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/ListExperiments',
            service__pb2.ListExperimentsRequest.SerializeToString,
            service__pb2.ListExperimentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExperiment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/GetExperiment',
            service__pb2.GetExperimentRequest.SerializeToString,
            service__pb2.GetExperimentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCheckpoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/CreateCheckpoint',
            service__pb2.CreateCheckpointRequest.SerializeToString,
            service__pb2.CreateCheckpointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCheckpoints(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/ListCheckpoints',
            service__pb2.ListCheckpointsRequest.SerializeToString,
            service__pb2.ListCheckpointsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCheckpoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/GetCheckpoint',
            service__pb2.GetCheckpointRequest.SerializeToString,
            service__pb2.GetCheckpointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/modelbox.ModelStore/UploadFile',
            service__pb2.UploadFileRequest.SerializeToString,
            service__pb2.UploadFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/modelbox.ModelStore/DownloadFile',
            service__pb2.DownloadFileRequest.SerializeToString,
            service__pb2.DownloadFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/UpdateMetadata',
            service__pb2.UpdateMetadataRequest.SerializeToString,
            service__pb2.UpdateMetadataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/ListMetadata',
            service__pb2.ListMetadataRequest.SerializeToString,
            service__pb2.ListMetadataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrackArtifacts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/TrackArtifacts',
            service__pb2.TrackArtifactsRequest.SerializeToString,
            service__pb2.TrackArtifactsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LogMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/LogMetrics',
            service__pb2.LogMetricsRequest.SerializeToString,
            service__pb2.LogMetricsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/GetMetrics',
            service__pb2.GetMetricsRequest.SerializeToString,
            service__pb2.GetMetricsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LogEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/LogEvent',
            service__pb2.LogEventRequest.SerializeToString,
            service__pb2.LogEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelbox.ModelStore/ListEvents',
            service__pb2.ListEventsRequest.SerializeToString,
            service__pb2.ListEventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WatchNamespace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/modelbox.ModelStore/WatchNamespace',
            service__pb2.WatchNamespaceRequest.SerializeToString,
            service__pb2.WatchNamespaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
