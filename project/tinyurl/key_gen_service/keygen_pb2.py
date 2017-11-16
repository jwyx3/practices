# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keygen.proto

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
  name='keygen.proto',
  package='keygen',
  syntax='proto3',
  serialized_pb=_b('\n\x0ckeygen.proto\x12\x06keygen\"\x07\n\x05\x45mpty\"\x11\n\x03Key\x12\n\n\x02id\x18\x01 \x01(\t24\n\x06KeyGen\x12*\n\x08ListKeys\x12\r.keygen.Empty\x1a\x0b.keygen.Key\"\x00\x30\x01\x42+\n\x14jwyx3.tinyurl.keygenB\x0bKeyGenProtoP\x01\xa2\x02\x03KGSb\x06proto3')
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='keygen.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=24,
  serialized_end=31,
)


_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='keygen.Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='keygen.Key.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=33,
  serialized_end=50,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Key'] = _KEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'keygen_pb2'
  # @@protoc_insertion_point(class_scope:keygen.Empty)
  ))
_sym_db.RegisterMessage(Empty)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), dict(
  DESCRIPTOR = _KEY,
  __module__ = 'keygen_pb2'
  # @@protoc_insertion_point(class_scope:keygen.Key)
  ))
_sym_db.RegisterMessage(Key)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\024jwyx3.tinyurl.keygenB\013KeyGenProtoP\001\242\002\003KGS'))

_KEYGEN = _descriptor.ServiceDescriptor(
  name='KeyGen',
  full_name='keygen.KeyGen',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=52,
  serialized_end=104,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListKeys',
    full_name='keygen.KeyGen.ListKeys',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_KEY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYGEN)

DESCRIPTOR.services_by_name['KeyGen'] = _KEYGEN

# @@protoc_insertion_point(module_scope)
