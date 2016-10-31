from genproto import consumer_client_pb2 as cpb
from genproto import base_pb2 as bpb
import util
import data
import uuid

# Implementation of the CustomerServer service, that
# handles customer-facing requests.

class CustomerServer(cpb.CustomerServerServicer):
    def __init__(self, db, logger):
        self.db = db
        self.log = logger

    def GetBalances(self, request, context):
        cust = request.customer
        usr = self.db.users().where(id=cust.id).get()

        rsp = cpb.Balances()
        
        for balance in self.db.accounts().where(customerid=usr.id):
            bsn = self.db.businesses().where(id=balance.businessid).get()
            
            rsp.balances.append(
                business = util.business_proto(bsn),
                point_balance = balance.points
            )
        return rsp

    def EnrollInBusiness(self, request, context):
        # If this customer is already enrolled,
        if self.db.accounts().where(customerid=request.customer.id,
                                    businessid=request.business_id).len():
            self.log.warn("Customer {}  already has an account with this business {}.", request.customer.id, request.business_id)
            return cpb.EnrollInBusinessResponse(success=False)
        
        if (self.db.users().where(id=request.customer.id).len() > 0 and
            self.db.businesses().where(id=request.business_id).len() > 0):
            new_acct = data.AccountBalance(
                id=uuid.uuid4(),
                businessid=request.business_id,
                customerid=request.customer.id)
            self.db.update_account(new_acct)
            self.log.info("Enrolled user {} in business {}.", request.customer.id,request.business.id)
            return cpb.EnrollInBusinessResponse(success=True)

        self.log.warn("Couldn't find the user ({}) or business ({}) to enroll.", request.customer,id, request.business.id)
        return cpb.EnrollInBusinessResponse(success=False)
