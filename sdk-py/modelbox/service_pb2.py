# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x08modelbox\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"9\n\x15WatchNamespaceRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\r\n\x05since\x18\x02 \x01(\x04\"g\n\x16WatchNamespaceResponse\x12$\n\x05\x65vent\x18\x01 \x01(\x0e\x32\x15.modelbox.ChangeEvent\x12\'\n\x07payload\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\">\n\x07Metrics\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x06values\x18\x02 \x03(\x0b\x32\x16.modelbox.MetricsValue\"v\n\x0cMetricsValue\x12\x0c\n\x04step\x18\x01 \x01(\x04\x12\x16\n\x0ewallclock_time\x18\x02 \x01(\x04\x12\x0f\n\x05\x66_val\x18\x05 \x01(\x02H\x00\x12\x12\n\x08s_tensor\x18\x06 \x01(\tH\x00\x12\x12\n\x08\x62_tensor\x18\x07 \x01(\x0cH\x00\x42\x07\n\x05value\"Z\n\x11LogMetricsRequest\x12\x11\n\tparent_id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12%\n\x05value\x18\x03 \x01(\x0b\x32\x16.modelbox.MetricsValue\"\x14\n\x12LogMetricsResponse\"&\n\x11GetMetricsRequest\x12\x11\n\tparent_id\x18\x01 \x01(\t\"\x93\x01\n\x12GetMetricsResponse\x12:\n\x07metrics\x18\x01 \x03(\x0b\x32).modelbox.GetMetricsResponse.MetricsEntry\x1a\x41\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.modelbox.Metrics:\x02\x38\x01\"_\n\x15TrackArtifactsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tobject_id\x18\x02 \x01(\t\x12%\n\x05\x66iles\x18\x03 \x03(\x0b\x32\x16.modelbox.FileMetadata\"$\n\x16TrackArtifactsResponse\x12\n\n\x02id\x18\x01 \x01(\t\")\n\x14ListArtifactsRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\">\n\x15ListArtifactsResponse\x12%\n\tartifacts\x18\x01 \x03(\x0b\x32\x12.modelbox.Artifact\"\xed\x01\n\x0c\x46ileMetadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tparent_id\x18\x02 \x01(\t\x12%\n\tfile_type\x18\x03 \x01(\x0e\x32\x12.modelbox.FileType\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\t\x12\x10\n\x08src_path\x18\x05 \x01(\t\x12\x13\n\x0bupload_path\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"&\n\x13\x44ownloadFileRequest\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\"d\n\x14\x44ownloadFileResponse\x12*\n\x08metadata\x18\x01 \x01(\x0b\x32\x16.modelbox.FileMetadataH\x00\x12\x10\n\x06\x63hunks\x18\x02 \x01(\x0cH\x00\x42\x0e\n\x0cstream_frame\"g\n\x11UploadFileRequest\x12\x30\n\x08metadata\x18\x01 \x01(\x0b\x32\x1c.modelbox.UploadFileMetadataH\x00\x12\x10\n\x06\x63hunks\x18\x02 \x01(\x0cH\x00\x42\x0e\n\x0cstream_frame\":\n\x12UploadFileResponse\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61rtifact_id\x18\x02 \x01(\t\"h\n\x12UploadFileMetadata\x12\x15\n\rartifact_name\x18\x01 \x01(\t\x12\x11\n\tobject_id\x18\x02 \x01(\t\x12(\n\x08metadata\x18\x03 \x01(\x0b\x32\x16.modelbox.FileMetadata\"^\n\x08\x41rtifact\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tobject_id\x18\x03 \x01(\t\x12%\n\x05\x66iles\x18\x04 \x03(\x0b\x32\x16.modelbox.FileMetadata\"\xc6\x01\n\x05Model\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x11\n\tnamespace\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0c\n\x04task\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"g\n\x12\x43reateModelRequest\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x11\n\tnamespace\x18\x04 \x01(\t\x12\x0c\n\x04task\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\"\x91\x01\n\x13\x43reateModelResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x65xists\x18\x02 \x01(\x08\x12.\n\ncreated_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xff\x01\n\x0cModelVersion\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08model_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12(\n\tframework\x18\x08 \x01(\x0e\x32\x15.modelbox.MLFramework\x12\x13\n\x0bunique_tags\x18\t \x03(\t\x12.\n\ncreated_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xb0\x01\n\x19\x43reateModelVersionRequest\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x11\n\tnamespace\x18\x05 \x01(\t\x12(\n\tframework\x18\x08 \x01(\x0e\x32\x15.modelbox.MLFramework\x12\x13\n\x0bunique_tags\x18\t \x03(\t\"\xa3\x01\n\x1a\x43reateModelVersionResponse\x12\x15\n\rmodel_version\x18\x01 \x01(\t\x12\x0e\n\x06\x65xists\x18\x02 \x01(\x08\x12.\n\ncreated_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xe7\x01\n\nExperiment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\r\n\x05owner\x18\x04 \x01(\t\x12(\n\tframework\x18\x05 \x01(\x0e\x32\x15.modelbox.MLFramework\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12.\n\ncreated_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x96\x01\n\x17\x43reateExperimentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12(\n\tframework\x18\x04 \x01(\x0e\x32\x15.modelbox.MLFramework\x12\x0c\n\x04task\x18\x05 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\"\xac\x01\n\x18\x43reateExperimentResponse\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\x12\x19\n\x11\x65xperiment_exists\x18\x02 \x01(\x08\x12.\n\ncreated_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"+\n\x16ListExperimentsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\"D\n\x17ListExperimentsResponse\x12)\n\x0b\x65xperiments\x18\x01 \x03(\x0b\x32\x14.modelbox.Experiment\")\n\x18ListModelVersionsRequest\x12\r\n\x05model\x18\x01 \x01(\t\"K\n\x19ListModelVersionsResponse\x12.\n\x0emodel_versions\x18\x01 \x03(\x0b\x32\x16.modelbox.ModelVersion\"&\n\x11ListModelsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\"5\n\x12ListModelsResponse\x12\x1f\n\x06models\x18\x01 \x03(\x0b\x32\x0f.modelbox.Model\"o\n\x08Metadata\x12\x32\n\x08metadata\x18\x01 \x03(\x0b\x32 .modelbox.Metadata.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"P\n\x15UpdateMetadataRequest\x12\x11\n\tparent_id\x18\x01 \x01(\t\x12$\n\x08metadata\x18\x02 \x01(\x0b\x32\x12.modelbox.Metadata\"\x18\n\x16UpdateMetadataResponse\"(\n\x13ListMetadataRequest\x12\x11\n\tparent_id\x18\x01 \x01(\t\"<\n\x14ListMetadataResponse\x12$\n\x08metadata\x18\x01 \x01(\x0b\x32\x12.modelbox.Metadata\"\x1b\n\x0b\x45ventSource\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x96\x01\n\x05\x45vent\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x06source\x18\x03 \x01(\x0b\x32\x15.modelbox.EventSource\x12\x32\n\x0ewallclock_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\x08metadata\x18\x05 \x01(\x0b\x32\x12.modelbox.Metadata\"D\n\x0fLogEventRequest\x12\x11\n\tparent_id\x18\x01 \x01(\t\x12\x1e\n\x05\x65vent\x18\x02 \x01(\x0b\x32\x0f.modelbox.Event\"B\n\x10LogEventResponse\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"Q\n\x11ListEventsRequest\x12\x11\n\tparent_id\x18\x01 \x01(\t\x12)\n\x05since\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"5\n\x12ListEventsResponse\x12\x1f\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x0f.modelbox.Event\"\"\n\x14GetExperimentRequest\x12\n\n\x02id\x18\x01 \x01(\t\"A\n\x15GetExperimentResponse\x12(\n\nexperiment\x18\x01 \x01(\x0b\x32\x14.modelbox.Experiment*Q\n\x0b\x43hangeEvent\x12\x1a\n\x16\x43HANGE_EVENT_UNDEFINED\x10\x00\x12\x12\n\x0eOBJECT_CREATED\x10\x01\x12\x12\n\x0eOBJECT_UPDATED\x10\x02*_\n\x08\x46ileType\x12\r\n\tUNDEFINED\x10\x00\x12\t\n\x05MODEL\x10\x01\x12\x0e\n\nCHECKPOINT\x10\x02\x12\x08\n\x04TEXT\x10\x03\x12\t\n\x05IMAGE\x10\x04\x12\t\n\x05\x41UDIO\x10\x05\x12\t\n\x05VIDEO\x10\x06*2\n\x0bMLFramework\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PYTORCH\x10\x01\x12\t\n\x05KERAS\x10\x02\x32\xc1\x0b\n\nModelStore\x12J\n\x0b\x43reateModel\x12\x1c.modelbox.CreateModelRequest\x1a\x1d.modelbox.CreateModelResponse\x12G\n\nListModels\x12\x1b.modelbox.ListModelsRequest\x1a\x1c.modelbox.ListModelsResponse\x12_\n\x12\x43reateModelVersion\x12#.modelbox.CreateModelVersionRequest\x1a$.modelbox.CreateModelVersionResponse\x12\\\n\x11ListModelVersions\x12\".modelbox.ListModelVersionsRequest\x1a#.modelbox.ListModelVersionsResponse\x12Y\n\x10\x43reateExperiment\x12!.modelbox.CreateExperimentRequest\x1a\".modelbox.CreateExperimentResponse\x12V\n\x0fListExperiments\x12 .modelbox.ListExperimentsRequest\x1a!.modelbox.ListExperimentsResponse\x12P\n\rGetExperiment\x12\x1e.modelbox.GetExperimentRequest\x1a\x1f.modelbox.GetExperimentResponse\x12I\n\nUploadFile\x12\x1b.modelbox.UploadFileRequest\x1a\x1c.modelbox.UploadFileResponse(\x01\x12O\n\x0c\x44ownloadFile\x12\x1d.modelbox.DownloadFileRequest\x1a\x1e.modelbox.DownloadFileResponse0\x01\x12S\n\x0eUpdateMetadata\x12\x1f.modelbox.UpdateMetadataRequest\x1a .modelbox.UpdateMetadataResponse\x12M\n\x0cListMetadata\x12\x1d.modelbox.ListMetadataRequest\x1a\x1e.modelbox.ListMetadataResponse\x12S\n\x0eTrackArtifacts\x12\x1f.modelbox.TrackArtifactsRequest\x1a .modelbox.TrackArtifactsResponse\x12P\n\rListArtifacts\x12\x1e.modelbox.ListArtifactsRequest\x1a\x1f.modelbox.ListArtifactsResponse\x12G\n\nLogMetrics\x12\x1b.modelbox.LogMetricsRequest\x1a\x1c.modelbox.LogMetricsResponse\x12G\n\nGetMetrics\x12\x1b.modelbox.GetMetricsRequest\x1a\x1c.modelbox.GetMetricsResponse\x12\x41\n\x08LogEvent\x12\x19.modelbox.LogEventRequest\x1a\x1a.modelbox.LogEventResponse\x12G\n\nListEvents\x12\x1b.modelbox.ListEventsRequest\x1a\x1c.modelbox.ListEventsResponse\x12U\n\x0eWatchNamespace\x12\x1f.modelbox.WatchNamespaceRequest\x1a .modelbox.WatchNamespaceResponse0\x01\x42-Z+github.com/tensorland/modelbox/sdk-go/protob\x06proto3')

_CHANGEEVENT = DESCRIPTOR.enum_types_by_name['ChangeEvent']
ChangeEvent = enum_type_wrapper.EnumTypeWrapper(_CHANGEEVENT)
_FILETYPE = DESCRIPTOR.enum_types_by_name['FileType']
FileType = enum_type_wrapper.EnumTypeWrapper(_FILETYPE)
_MLFRAMEWORK = DESCRIPTOR.enum_types_by_name['MLFramework']
MLFramework = enum_type_wrapper.EnumTypeWrapper(_MLFRAMEWORK)
CHANGE_EVENT_UNDEFINED = 0
OBJECT_CREATED = 1
OBJECT_UPDATED = 2
UNDEFINED = 0
MODEL = 1
CHECKPOINT = 2
TEXT = 3
IMAGE = 4
AUDIO = 5
VIDEO = 6
UNKNOWN = 0
PYTORCH = 1
KERAS = 2


_WATCHNAMESPACEREQUEST = DESCRIPTOR.message_types_by_name['WatchNamespaceRequest']
_WATCHNAMESPACERESPONSE = DESCRIPTOR.message_types_by_name['WatchNamespaceResponse']
_METRICS = DESCRIPTOR.message_types_by_name['Metrics']
_METRICSVALUE = DESCRIPTOR.message_types_by_name['MetricsValue']
_LOGMETRICSREQUEST = DESCRIPTOR.message_types_by_name['LogMetricsRequest']
_LOGMETRICSRESPONSE = DESCRIPTOR.message_types_by_name['LogMetricsResponse']
_GETMETRICSREQUEST = DESCRIPTOR.message_types_by_name['GetMetricsRequest']
_GETMETRICSRESPONSE = DESCRIPTOR.message_types_by_name['GetMetricsResponse']
_GETMETRICSRESPONSE_METRICSENTRY = _GETMETRICSRESPONSE.nested_types_by_name['MetricsEntry']
_TRACKARTIFACTSREQUEST = DESCRIPTOR.message_types_by_name['TrackArtifactsRequest']
_TRACKARTIFACTSRESPONSE = DESCRIPTOR.message_types_by_name['TrackArtifactsResponse']
_LISTARTIFACTSREQUEST = DESCRIPTOR.message_types_by_name['ListArtifactsRequest']
_LISTARTIFACTSRESPONSE = DESCRIPTOR.message_types_by_name['ListArtifactsResponse']
_FILEMETADATA = DESCRIPTOR.message_types_by_name['FileMetadata']
_DOWNLOADFILEREQUEST = DESCRIPTOR.message_types_by_name['DownloadFileRequest']
_DOWNLOADFILERESPONSE = DESCRIPTOR.message_types_by_name['DownloadFileResponse']
_UPLOADFILEREQUEST = DESCRIPTOR.message_types_by_name['UploadFileRequest']
_UPLOADFILERESPONSE = DESCRIPTOR.message_types_by_name['UploadFileResponse']
_UPLOADFILEMETADATA = DESCRIPTOR.message_types_by_name['UploadFileMetadata']
_ARTIFACT = DESCRIPTOR.message_types_by_name['Artifact']
_MODEL = DESCRIPTOR.message_types_by_name['Model']
_CREATEMODELREQUEST = DESCRIPTOR.message_types_by_name['CreateModelRequest']
_CREATEMODELRESPONSE = DESCRIPTOR.message_types_by_name['CreateModelResponse']
_MODELVERSION = DESCRIPTOR.message_types_by_name['ModelVersion']
_CREATEMODELVERSIONREQUEST = DESCRIPTOR.message_types_by_name['CreateModelVersionRequest']
_CREATEMODELVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['CreateModelVersionResponse']
_EXPERIMENT = DESCRIPTOR.message_types_by_name['Experiment']
_CREATEEXPERIMENTREQUEST = DESCRIPTOR.message_types_by_name['CreateExperimentRequest']
_CREATEEXPERIMENTRESPONSE = DESCRIPTOR.message_types_by_name['CreateExperimentResponse']
_LISTEXPERIMENTSREQUEST = DESCRIPTOR.message_types_by_name['ListExperimentsRequest']
_LISTEXPERIMENTSRESPONSE = DESCRIPTOR.message_types_by_name['ListExperimentsResponse']
_LISTMODELVERSIONSREQUEST = DESCRIPTOR.message_types_by_name['ListModelVersionsRequest']
_LISTMODELVERSIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListModelVersionsResponse']
_LISTMODELSREQUEST = DESCRIPTOR.message_types_by_name['ListModelsRequest']
_LISTMODELSRESPONSE = DESCRIPTOR.message_types_by_name['ListModelsResponse']
_METADATA = DESCRIPTOR.message_types_by_name['Metadata']
_METADATA_METADATAENTRY = _METADATA.nested_types_by_name['MetadataEntry']
_UPDATEMETADATAREQUEST = DESCRIPTOR.message_types_by_name['UpdateMetadataRequest']
_UPDATEMETADATARESPONSE = DESCRIPTOR.message_types_by_name['UpdateMetadataResponse']
_LISTMETADATAREQUEST = DESCRIPTOR.message_types_by_name['ListMetadataRequest']
_LISTMETADATARESPONSE = DESCRIPTOR.message_types_by_name['ListMetadataResponse']
_EVENTSOURCE = DESCRIPTOR.message_types_by_name['EventSource']
_EVENT = DESCRIPTOR.message_types_by_name['Event']
_LOGEVENTREQUEST = DESCRIPTOR.message_types_by_name['LogEventRequest']
_LOGEVENTRESPONSE = DESCRIPTOR.message_types_by_name['LogEventResponse']
_LISTEVENTSREQUEST = DESCRIPTOR.message_types_by_name['ListEventsRequest']
_LISTEVENTSRESPONSE = DESCRIPTOR.message_types_by_name['ListEventsResponse']
_GETEXPERIMENTREQUEST = DESCRIPTOR.message_types_by_name['GetExperimentRequest']
_GETEXPERIMENTRESPONSE = DESCRIPTOR.message_types_by_name['GetExperimentResponse']
WatchNamespaceRequest = _reflection.GeneratedProtocolMessageType('WatchNamespaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _WATCHNAMESPACEREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.WatchNamespaceRequest)
  })
_sym_db.RegisterMessage(WatchNamespaceRequest)

WatchNamespaceResponse = _reflection.GeneratedProtocolMessageType('WatchNamespaceResponse', (_message.Message,), {
  'DESCRIPTOR' : _WATCHNAMESPACERESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.WatchNamespaceResponse)
  })
_sym_db.RegisterMessage(WatchNamespaceResponse)

Metrics = _reflection.GeneratedProtocolMessageType('Metrics', (_message.Message,), {
  'DESCRIPTOR' : _METRICS,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.Metrics)
  })
_sym_db.RegisterMessage(Metrics)

MetricsValue = _reflection.GeneratedProtocolMessageType('MetricsValue', (_message.Message,), {
  'DESCRIPTOR' : _METRICSVALUE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.MetricsValue)
  })
_sym_db.RegisterMessage(MetricsValue)

LogMetricsRequest = _reflection.GeneratedProtocolMessageType('LogMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGMETRICSREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.LogMetricsRequest)
  })
_sym_db.RegisterMessage(LogMetricsRequest)

LogMetricsResponse = _reflection.GeneratedProtocolMessageType('LogMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGMETRICSRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.LogMetricsResponse)
  })
_sym_db.RegisterMessage(LogMetricsResponse)

GetMetricsRequest = _reflection.GeneratedProtocolMessageType('GetMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMETRICSREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.GetMetricsRequest)
  })
_sym_db.RegisterMessage(GetMetricsRequest)

GetMetricsResponse = _reflection.GeneratedProtocolMessageType('GetMetricsResponse', (_message.Message,), {

  'MetricsEntry' : _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETMETRICSRESPONSE_METRICSENTRY,
    '__module__' : 'service_pb2'
    # @@protoc_insertion_point(class_scope:modelbox.GetMetricsResponse.MetricsEntry)
    })
  ,
  'DESCRIPTOR' : _GETMETRICSRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.GetMetricsResponse)
  })
_sym_db.RegisterMessage(GetMetricsResponse)
_sym_db.RegisterMessage(GetMetricsResponse.MetricsEntry)

TrackArtifactsRequest = _reflection.GeneratedProtocolMessageType('TrackArtifactsRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRACKARTIFACTSREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.TrackArtifactsRequest)
  })
_sym_db.RegisterMessage(TrackArtifactsRequest)

TrackArtifactsResponse = _reflection.GeneratedProtocolMessageType('TrackArtifactsResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRACKARTIFACTSRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.TrackArtifactsResponse)
  })
_sym_db.RegisterMessage(TrackArtifactsResponse)

ListArtifactsRequest = _reflection.GeneratedProtocolMessageType('ListArtifactsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTARTIFACTSREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListArtifactsRequest)
  })
_sym_db.RegisterMessage(ListArtifactsRequest)

ListArtifactsResponse = _reflection.GeneratedProtocolMessageType('ListArtifactsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTARTIFACTSRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListArtifactsResponse)
  })
_sym_db.RegisterMessage(ListArtifactsResponse)

FileMetadata = _reflection.GeneratedProtocolMessageType('FileMetadata', (_message.Message,), {
  'DESCRIPTOR' : _FILEMETADATA,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.FileMetadata)
  })
_sym_db.RegisterMessage(FileMetadata)

DownloadFileRequest = _reflection.GeneratedProtocolMessageType('DownloadFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADFILEREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.DownloadFileRequest)
  })
_sym_db.RegisterMessage(DownloadFileRequest)

DownloadFileResponse = _reflection.GeneratedProtocolMessageType('DownloadFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADFILERESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.DownloadFileResponse)
  })
_sym_db.RegisterMessage(DownloadFileResponse)

UploadFileRequest = _reflection.GeneratedProtocolMessageType('UploadFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADFILEREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.UploadFileRequest)
  })
_sym_db.RegisterMessage(UploadFileRequest)

UploadFileResponse = _reflection.GeneratedProtocolMessageType('UploadFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADFILERESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.UploadFileResponse)
  })
_sym_db.RegisterMessage(UploadFileResponse)

UploadFileMetadata = _reflection.GeneratedProtocolMessageType('UploadFileMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADFILEMETADATA,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.UploadFileMetadata)
  })
_sym_db.RegisterMessage(UploadFileMetadata)

Artifact = _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), {
  'DESCRIPTOR' : _ARTIFACT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.Artifact)
  })
_sym_db.RegisterMessage(Artifact)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.Model)
  })
_sym_db.RegisterMessage(Model)

CreateModelRequest = _reflection.GeneratedProtocolMessageType('CreateModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODELREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.CreateModelRequest)
  })
_sym_db.RegisterMessage(CreateModelRequest)

CreateModelResponse = _reflection.GeneratedProtocolMessageType('CreateModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODELRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.CreateModelResponse)
  })
_sym_db.RegisterMessage(CreateModelResponse)

ModelVersion = _reflection.GeneratedProtocolMessageType('ModelVersion', (_message.Message,), {
  'DESCRIPTOR' : _MODELVERSION,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ModelVersion)
  })
_sym_db.RegisterMessage(ModelVersion)

CreateModelVersionRequest = _reflection.GeneratedProtocolMessageType('CreateModelVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODELVERSIONREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.CreateModelVersionRequest)
  })
_sym_db.RegisterMessage(CreateModelVersionRequest)

CreateModelVersionResponse = _reflection.GeneratedProtocolMessageType('CreateModelVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODELVERSIONRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.CreateModelVersionResponse)
  })
_sym_db.RegisterMessage(CreateModelVersionResponse)

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.Experiment)
  })
_sym_db.RegisterMessage(Experiment)

CreateExperimentRequest = _reflection.GeneratedProtocolMessageType('CreateExperimentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEEXPERIMENTREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.CreateExperimentRequest)
  })
_sym_db.RegisterMessage(CreateExperimentRequest)

CreateExperimentResponse = _reflection.GeneratedProtocolMessageType('CreateExperimentResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEEXPERIMENTRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.CreateExperimentResponse)
  })
_sym_db.RegisterMessage(CreateExperimentResponse)

ListExperimentsRequest = _reflection.GeneratedProtocolMessageType('ListExperimentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTEXPERIMENTSREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListExperimentsRequest)
  })
_sym_db.RegisterMessage(ListExperimentsRequest)

ListExperimentsResponse = _reflection.GeneratedProtocolMessageType('ListExperimentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTEXPERIMENTSRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListExperimentsResponse)
  })
_sym_db.RegisterMessage(ListExperimentsResponse)

ListModelVersionsRequest = _reflection.GeneratedProtocolMessageType('ListModelVersionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELVERSIONSREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListModelVersionsRequest)
  })
_sym_db.RegisterMessage(ListModelVersionsRequest)

ListModelVersionsResponse = _reflection.GeneratedProtocolMessageType('ListModelVersionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELVERSIONSRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListModelVersionsResponse)
  })
_sym_db.RegisterMessage(ListModelVersionsResponse)

ListModelsRequest = _reflection.GeneratedProtocolMessageType('ListModelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELSREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListModelsRequest)
  })
_sym_db.RegisterMessage(ListModelsRequest)

ListModelsResponse = _reflection.GeneratedProtocolMessageType('ListModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELSRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListModelsResponse)
  })
_sym_db.RegisterMessage(ListModelsResponse)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _METADATA_METADATAENTRY,
    '__module__' : 'service_pb2'
    # @@protoc_insertion_point(class_scope:modelbox.Metadata.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.Metadata)
  })
_sym_db.RegisterMessage(Metadata)
_sym_db.RegisterMessage(Metadata.MetadataEntry)

UpdateMetadataRequest = _reflection.GeneratedProtocolMessageType('UpdateMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMETADATAREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.UpdateMetadataRequest)
  })
_sym_db.RegisterMessage(UpdateMetadataRequest)

UpdateMetadataResponse = _reflection.GeneratedProtocolMessageType('UpdateMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMETADATARESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.UpdateMetadataResponse)
  })
_sym_db.RegisterMessage(UpdateMetadataResponse)

ListMetadataRequest = _reflection.GeneratedProtocolMessageType('ListMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMETADATAREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListMetadataRequest)
  })
_sym_db.RegisterMessage(ListMetadataRequest)

ListMetadataResponse = _reflection.GeneratedProtocolMessageType('ListMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMETADATARESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListMetadataResponse)
  })
_sym_db.RegisterMessage(ListMetadataResponse)

EventSource = _reflection.GeneratedProtocolMessageType('EventSource', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSOURCE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.EventSource)
  })
_sym_db.RegisterMessage(EventSource)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.Event)
  })
_sym_db.RegisterMessage(Event)

LogEventRequest = _reflection.GeneratedProtocolMessageType('LogEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGEVENTREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.LogEventRequest)
  })
_sym_db.RegisterMessage(LogEventRequest)

LogEventResponse = _reflection.GeneratedProtocolMessageType('LogEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGEVENTRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.LogEventResponse)
  })
_sym_db.RegisterMessage(LogEventResponse)

ListEventsRequest = _reflection.GeneratedProtocolMessageType('ListEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTSREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListEventsRequest)
  })
_sym_db.RegisterMessage(ListEventsRequest)

ListEventsResponse = _reflection.GeneratedProtocolMessageType('ListEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTSRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.ListEventsResponse)
  })
_sym_db.RegisterMessage(ListEventsResponse)

GetExperimentRequest = _reflection.GeneratedProtocolMessageType('GetExperimentRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEXPERIMENTREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.GetExperimentRequest)
  })
_sym_db.RegisterMessage(GetExperimentRequest)

GetExperimentResponse = _reflection.GeneratedProtocolMessageType('GetExperimentResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETEXPERIMENTRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:modelbox.GetExperimentResponse)
  })
_sym_db.RegisterMessage(GetExperimentResponse)

_MODELSTORE = DESCRIPTOR.services_by_name['ModelStore']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/tensorland/modelbox/sdk-go/proto'
  _GETMETRICSRESPONSE_METRICSENTRY._options = None
  _GETMETRICSRESPONSE_METRICSENTRY._serialized_options = b'8\001'
  _METADATA_METADATAENTRY._options = None
  _METADATA_METADATAENTRY._serialized_options = b'8\001'
  _CHANGEEVENT._serialized_start=4568
  _CHANGEEVENT._serialized_end=4649
  _FILETYPE._serialized_start=4651
  _FILETYPE._serialized_end=4746
  _MLFRAMEWORK._serialized_start=4748
  _MLFRAMEWORK._serialized_end=4798
  _WATCHNAMESPACEREQUEST._serialized_start=90
  _WATCHNAMESPACEREQUEST._serialized_end=147
  _WATCHNAMESPACERESPONSE._serialized_start=149
  _WATCHNAMESPACERESPONSE._serialized_end=252
  _METRICS._serialized_start=254
  _METRICS._serialized_end=316
  _METRICSVALUE._serialized_start=318
  _METRICSVALUE._serialized_end=436
  _LOGMETRICSREQUEST._serialized_start=438
  _LOGMETRICSREQUEST._serialized_end=528
  _LOGMETRICSRESPONSE._serialized_start=530
  _LOGMETRICSRESPONSE._serialized_end=550
  _GETMETRICSREQUEST._serialized_start=552
  _GETMETRICSREQUEST._serialized_end=590
  _GETMETRICSRESPONSE._serialized_start=593
  _GETMETRICSRESPONSE._serialized_end=740
  _GETMETRICSRESPONSE_METRICSENTRY._serialized_start=675
  _GETMETRICSRESPONSE_METRICSENTRY._serialized_end=740
  _TRACKARTIFACTSREQUEST._serialized_start=742
  _TRACKARTIFACTSREQUEST._serialized_end=837
  _TRACKARTIFACTSRESPONSE._serialized_start=839
  _TRACKARTIFACTSRESPONSE._serialized_end=875
  _LISTARTIFACTSREQUEST._serialized_start=877
  _LISTARTIFACTSREQUEST._serialized_end=918
  _LISTARTIFACTSRESPONSE._serialized_start=920
  _LISTARTIFACTSRESPONSE._serialized_end=982
  _FILEMETADATA._serialized_start=985
  _FILEMETADATA._serialized_end=1222
  _DOWNLOADFILEREQUEST._serialized_start=1224
  _DOWNLOADFILEREQUEST._serialized_end=1262
  _DOWNLOADFILERESPONSE._serialized_start=1264
  _DOWNLOADFILERESPONSE._serialized_end=1364
  _UPLOADFILEREQUEST._serialized_start=1366
  _UPLOADFILEREQUEST._serialized_end=1469
  _UPLOADFILERESPONSE._serialized_start=1471
  _UPLOADFILERESPONSE._serialized_end=1529
  _UPLOADFILEMETADATA._serialized_start=1531
  _UPLOADFILEMETADATA._serialized_end=1635
  _ARTIFACT._serialized_start=1637
  _ARTIFACT._serialized_end=1731
  _MODEL._serialized_start=1734
  _MODEL._serialized_end=1932
  _CREATEMODELREQUEST._serialized_start=1934
  _CREATEMODELREQUEST._serialized_end=2037
  _CREATEMODELRESPONSE._serialized_start=2040
  _CREATEMODELRESPONSE._serialized_end=2185
  _MODELVERSION._serialized_start=2188
  _MODELVERSION._serialized_end=2443
  _CREATEMODELVERSIONREQUEST._serialized_start=2446
  _CREATEMODELVERSIONREQUEST._serialized_end=2622
  _CREATEMODELVERSIONRESPONSE._serialized_start=2625
  _CREATEMODELVERSIONRESPONSE._serialized_end=2788
  _EXPERIMENT._serialized_start=2791
  _EXPERIMENT._serialized_end=3022
  _CREATEEXPERIMENTREQUEST._serialized_start=3025
  _CREATEEXPERIMENTREQUEST._serialized_end=3175
  _CREATEEXPERIMENTRESPONSE._serialized_start=3178
  _CREATEEXPERIMENTRESPONSE._serialized_end=3350
  _LISTEXPERIMENTSREQUEST._serialized_start=3352
  _LISTEXPERIMENTSREQUEST._serialized_end=3395
  _LISTEXPERIMENTSRESPONSE._serialized_start=3397
  _LISTEXPERIMENTSRESPONSE._serialized_end=3465
  _LISTMODELVERSIONSREQUEST._serialized_start=3467
  _LISTMODELVERSIONSREQUEST._serialized_end=3508
  _LISTMODELVERSIONSRESPONSE._serialized_start=3510
  _LISTMODELVERSIONSRESPONSE._serialized_end=3585
  _LISTMODELSREQUEST._serialized_start=3587
  _LISTMODELSREQUEST._serialized_end=3625
  _LISTMODELSRESPONSE._serialized_start=3627
  _LISTMODELSRESPONSE._serialized_end=3680
  _METADATA._serialized_start=3682
  _METADATA._serialized_end=3793
  _METADATA_METADATAENTRY._serialized_start=3746
  _METADATA_METADATAENTRY._serialized_end=3793
  _UPDATEMETADATAREQUEST._serialized_start=3795
  _UPDATEMETADATAREQUEST._serialized_end=3875
  _UPDATEMETADATARESPONSE._serialized_start=3877
  _UPDATEMETADATARESPONSE._serialized_end=3901
  _LISTMETADATAREQUEST._serialized_start=3903
  _LISTMETADATAREQUEST._serialized_end=3943
  _LISTMETADATARESPONSE._serialized_start=3945
  _LISTMETADATARESPONSE._serialized_end=4005
  _EVENTSOURCE._serialized_start=4007
  _EVENTSOURCE._serialized_end=4034
  _EVENT._serialized_start=4037
  _EVENT._serialized_end=4187
  _LOGEVENTREQUEST._serialized_start=4189
  _LOGEVENTREQUEST._serialized_end=4257
  _LOGEVENTRESPONSE._serialized_start=4259
  _LOGEVENTRESPONSE._serialized_end=4325
  _LISTEVENTSREQUEST._serialized_start=4327
  _LISTEVENTSREQUEST._serialized_end=4408
  _LISTEVENTSRESPONSE._serialized_start=4410
  _LISTEVENTSRESPONSE._serialized_end=4463
  _GETEXPERIMENTREQUEST._serialized_start=4465
  _GETEXPERIMENTREQUEST._serialized_end=4499
  _GETEXPERIMENTRESPONSE._serialized_start=4501
  _GETEXPERIMENTRESPONSE._serialized_end=4566
  _MODELSTORE._serialized_start=4801
  _MODELSTORE._serialized_end=6274
# @@protoc_insertion_point(module_scope)
