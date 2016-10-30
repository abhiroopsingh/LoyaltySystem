# Provides utilities for common tasks in the codebase,
# such as serializing data types to proto.

from gen_proto import base_pb2 as bpb
from data import *

def business_proto(business):
    return bpb.Business(
        name  = business.name,
        id = business.id
    )
