# Provides utilities for common tasks in the codebase,
# such as serializing data types to proto.

from genproto import base_pb2 as bpb
from genproto import transactions_pb2 as tpb
from data import *
from datetime import datetime

def business_proto(business):
    return bpb.Business(
        name  = business.name,
        id = business.id,
        thumbnailurl = business.thumbnail,
    )

def time_sec():
    return int(datetime.now().strftime("%s"))

def transaction(trans, db):
    tproto = tpb.Transaction()

    bus = db.businesses().where(id=trans.businessid).get()
    cus = db.users().where(id=trans.customerid).get()
    tproto.customer.id = cus.id
    tproto.point_change = trans.points
    tproto.customer.name = cus.name
    tproto.customer.username = cus.username
    tproto.business.CopyFrom(
        business_proto(bus))
    tproto.time_ms = trans.time
    return tproto

def transactions(trans, db):
    tproto = tpb.Transactions()
    tproto.transactions.extend([
        transaction(tran, db) for
        tran in trans
        ])
    return tproto


def exists(basequery, idval):
    return basequery.where(id=idval).len() > 0
