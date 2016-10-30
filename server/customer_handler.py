from genproto import consumer_client_pb2 as cpb
from genproto import base_pb2 as bpb
import util

# Implementation of the CustomerServer service, that
# handles customer-facing requests.

class CustomerServer(cpb.CustomerServerServicer):
    def __init__(self, db):
        self.db = db

    def Redeem(self, request, context):
        return None

    def GetBalances(self, request, context):
        cust = request.customer
        usr = self.db.find_user(id=cust.id)

        rsp = cpb.Balances()
        
        for balance in usr.balances:
            bsn = self.db.find_business(id=balance.businessid)
            
            rsp.balances.append(
                business = util.business_proto(bsn)
                point_balance = balance.points
            )
            
        return rsp

    def EnrollInBusiness(self, request, context):
        return None
