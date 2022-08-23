#!/bin/bash

protoc --go_out=sdk-go --go_opt=paths=source_relative --go-grpc_out=sdk-go --go-grpc_opt=paths=source_relative proto/service.proto

python -m grpc_tools.protoc -Iproto/ --python_out=sdk-py/modelbox/ --grpc_python_out=sdk-py/modelbox/ proto/service.proto