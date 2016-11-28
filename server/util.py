# Provides utilities for common tasks in the codebase,
# such as serializing data types to proto.

from genproto import base_pb2 as bpb
from genproto import transactions_pb2 as tpb
from data import *

def business_proto(business):
    return bpb.Business(
        name  = business.name,
        id = business.id,
        thumbnailurl = business.thumbnail,
    )

def transaction(trans, db):
    tproto = tpb.Transaction()
    tproto.id = trans.id.int

    bus = db.businesses().where(id=trans.businessid).get()
    cus = db.users().where(id=trans.customerid).get()
    tproto.customer.id = cus.id
    tproto.customer.name = cus.name
    tproto.customer.username = cus.username
    tproto.business.copy_from(
        business_proto(bus))
    tproto.time_ms = trans.time
    return tproto

def transactions(trans, db):
    tproto = tpb.Transactions()
    tproto.extend([
        transaction(tran, db) for
        tran in trans
        ])
    return tproto


def exists(basequery, idval):
    return basequery.where(id=idval).len() > 0
