# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='base.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nbase.proto\"6\n\x08\x43ustomer\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\":\n\x08\x42usiness\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\x12\x14\n\x0cthumbnailurl\x18\x03 \x01(\t\"D\n\x0e\x41\x63\x63ountBalance\x12\x1b\n\x08\x62usiness\x18\x01 \x01(\x0b\x32\t.Business\x12\x15\n\rpoint_balance\x18\x02 \x01(\x05\"J\n\x15RedemptionOpportunity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0frequired_points\x18\x02 \x01(\x05\x12\n\n\x02id\x18\x03 \x01(\x03\x42\x18\n\x16\x63om.loyaltysystem.baseb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CUSTOMER = _descriptor.Descriptor(
  name='Customer',
  full_name='Customer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Customer.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Customer.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='Customer.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=68,
)


_BUSINESS = _descriptor.Descriptor(
  name='Business',
  full_name='Business',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Business.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Business.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumbnailurl', full_name='Business.thumbnailurl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=128,
)


_ACCOUNTBALANCE = _descriptor.Descriptor(
  name='AccountBalance',
  full_name='AccountBalance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='business', full_name='AccountBalance.business', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_balance', full_name='AccountBalance.point_balance', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=198,
)


_REDEMPTIONOPPORTUNITY = _descriptor.Descriptor(
  name='RedemptionOpportunity',
  full_name='RedemptionOpportunity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RedemptionOpportunity.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required_points', full_name='RedemptionOpportunity.required_points', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='RedemptionOpportunity.id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=274,
)

_ACCOUNTBALANCE.fields_by_name['business'].message_type = _BUSINESS
DESCRIPTOR.message_types_by_name['Customer'] = _CUSTOMER
DESCRIPTOR.message_types_by_name['Business'] = _BUSINESS
DESCRIPTOR.message_types_by_name['AccountBalance'] = _ACCOUNTBALANCE
DESCRIPTOR.message_types_by_name['RedemptionOpportunity'] = _REDEMPTIONOPPORTUNITY

Customer = _reflection.GeneratedProtocolMessageType('Customer', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMER,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Customer)
  ))
_sym_db.RegisterMessage(Customer)

Business = _reflection.GeneratedProtocolMessageType('Business', (_message.Message,), dict(
  DESCRIPTOR = _BUSINESS,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Business)
  ))
_sym_db.RegisterMessage(Business)

AccountBalance = _reflection.GeneratedProtocolMessageType('AccountBalance', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTBALANCE,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:AccountBalance)
  ))
_sym_db.RegisterMessage(AccountBalance)

RedemptionOpportunity = _reflection.GeneratedProtocolMessageType('RedemptionOpportunity', (_message.Message,), dict(
  DESCRIPTOR = _REDEMPTIONOPPORTUNITY,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:RedemptionOpportunity)
  ))
_sym_db.RegisterMessage(RedemptionOpportunity)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.loyaltysystem.base'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
