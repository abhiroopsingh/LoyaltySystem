# Provides utilities for common tasks in the codebase,
# such as serializing data types to proto.

from genproto import base_pb2 as bpb
from data import *

def business_proto(business):
    return bpb.Business(
        name  = business.name,
        id = business.id,
        thumbnailurl = business.thumbnail,
    )

def exists(basequery, idval):
    return basequery.where(id=idval).len() > 0
