# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transactions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import base_pb2 as base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transactions.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x12transactions.proto\x1a\nbase.proto\"z\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x1b\n\x08\x63ustomer\x18\x02 \x01(\x0b\x32\t.Customer\x12\x1b\n\x08\x62usiness\x18\x03 \x01(\x0b\x32\t.Business\x12\x0f\n\x07time_ms\x18\x04 \x01(\x03\x12\x14\n\x0cpoint_change\x18\x05 \x01(\x05\"2\n\x0cTransactions\x12\"\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x0c.Transaction\"&\n\x0f\x43ustomerRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\x03\"&\n\x0f\x42usinessRequest\x12\x13\n\x0b\x62usiness_id\x18\x01 \x01(\x03\x32\x8b\x01\n\x13TransactionProvider\x12\x39\n\x14\x43ustomerTransactions\x12\x10.CustomerRequest\x1a\r.Transactions\"\x00\x12\x39\n\x14\x42usinessTransactions\x12\x10.BusinessRequest\x1a\r.Transactions\"\x00\x42 \n\x1e\x63om.loyaltysystem.transactionsb\x06proto3')
  ,
  dependencies=[base__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Transaction.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='customer', full_name='Transaction.customer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='business', full_name='Transaction.business', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_ms', full_name='Transaction.time_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_change', full_name='Transaction.point_change', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=34,
  serialized_end=156,
)


_TRANSACTIONS = _descriptor.Descriptor(
  name='Transactions',
  full_name='Transactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='Transactions.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=158,
  serialized_end=208,
)


_CUSTOMERREQUEST = _descriptor.Descriptor(
  name='CustomerRequest',
  full_name='CustomerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='CustomerRequest.customer_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=210,
  serialized_end=248,
)


_BUSINESSREQUEST = _descriptor.Descriptor(
  name='BusinessRequest',
  full_name='BusinessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='business_id', full_name='BusinessRequest.business_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=250,
  serialized_end=288,
)

_TRANSACTION.fields_by_name['customer'].message_type = base__pb2._CUSTOMER
_TRANSACTION.fields_by_name['business'].message_type = base__pb2._BUSINESS
_TRANSACTIONS.fields_by_name['transactions'].message_type = _TRANSACTION
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['Transactions'] = _TRANSACTIONS
DESCRIPTOR.message_types_by_name['CustomerRequest'] = _CUSTOMERREQUEST
DESCRIPTOR.message_types_by_name['BusinessRequest'] = _BUSINESSREQUEST

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'transactions_pb2'
  # @@protoc_insertion_point(class_scope:Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

Transactions = _reflection.GeneratedProtocolMessageType('Transactions', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONS,
  __module__ = 'transactions_pb2'
  # @@protoc_insertion_point(class_scope:Transactions)
  ))
_sym_db.RegisterMessage(Transactions)

CustomerRequest = _reflection.GeneratedProtocolMessageType('CustomerRequest', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMERREQUEST,
  __module__ = 'transactions_pb2'
  # @@protoc_insertion_point(class_scope:CustomerRequest)
  ))
_sym_db.RegisterMessage(CustomerRequest)

BusinessRequest = _reflection.GeneratedProtocolMessageType('BusinessRequest', (_message.Message,), dict(
  DESCRIPTOR = _BUSINESSREQUEST,
  __module__ = 'transactions_pb2'
  # @@protoc_insertion_point(class_scope:BusinessRequest)
  ))
_sym_db.RegisterMessage(BusinessRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036com.loyaltysystem.transactions'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class TransactionProviderStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CustomerTransactions = channel.unary_unary(
        '/TransactionProvider/CustomerTransactions',
        request_serializer=CustomerRequest.SerializeToString,
        response_deserializer=Transactions.FromString,
        )
    self.BusinessTransactions = channel.unary_unary(
        '/TransactionProvider/BusinessTransactions',
        request_serializer=BusinessRequest.SerializeToString,
        response_deserializer=Transactions.FromString,
        )


class TransactionProviderServicer(object):

  def CustomerTransactions(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BusinessTransactions(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TransactionProviderServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CustomerTransactions': grpc.unary_unary_rpc_method_handler(
          servicer.CustomerTransactions,
          request_deserializer=CustomerRequest.FromString,
          response_serializer=Transactions.SerializeToString,
      ),
      'BusinessTransactions': grpc.unary_unary_rpc_method_handler(
          servicer.BusinessTransactions,
          request_deserializer=BusinessRequest.FromString,
          response_serializer=Transactions.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'TransactionProvider', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaTransactionProviderServicer(object):
  def CustomerTransactions(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def BusinessTransactions(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaTransactionProviderStub(object):
  def CustomerTransactions(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  CustomerTransactions.future = None
  def BusinessTransactions(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  BusinessTransactions.future = None


def beta_create_TransactionProvider_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('TransactionProvider', 'BusinessTransactions'): BusinessRequest.FromString,
    ('TransactionProvider', 'CustomerTransactions'): CustomerRequest.FromString,
  }
  response_serializers = {
    ('TransactionProvider', 'BusinessTransactions'): Transactions.SerializeToString,
    ('TransactionProvider', 'CustomerTransactions'): Transactions.SerializeToString,
  }
  method_implementations = {
    ('TransactionProvider', 'BusinessTransactions'): face_utilities.unary_unary_inline(servicer.BusinessTransactions),
    ('TransactionProvider', 'CustomerTransactions'): face_utilities.unary_unary_inline(servicer.CustomerTransactions),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_TransactionProvider_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('TransactionProvider', 'BusinessTransactions'): BusinessRequest.SerializeToString,
    ('TransactionProvider', 'CustomerTransactions'): CustomerRequest.SerializeToString,
  }
  response_deserializers = {
    ('TransactionProvider', 'BusinessTransactions'): Transactions.FromString,
    ('TransactionProvider', 'CustomerTransactions'): Transactions.FromString,
  }
  cardinalities = {
    'BusinessTransactions': cardinality.Cardinality.UNARY_UNARY,
    'CustomerTransactions': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'TransactionProvider', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
