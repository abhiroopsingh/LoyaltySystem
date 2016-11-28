from genproto import consumer_client_pb2 as cpb
from genproto import base_pb2 as bpb
import util
import data
import uuid
import time

# Implementation of the CustomerServer service, that
# handles customer-facing requests.

# Time (seconds) between keep-alive messages
# when awaiting notifications.
KEEPALIVE_TIME = 0.1 

class CustomerServer(cpb.CustomerServerServicer):
    def __init__(self, db, logger, notifier):
        self.db = db
        self.log = logger
        self.notifier = notifier

    def GetBalances(self, request, context):
        cust_id = request.customer_id
        usr = self.db.users().where(id=cust_id).get()

        rsp = cpb.Balances()
        
        for balance in self.db.accounts().where(customerid=usr.id).all():
            bsn = self.db.businesses().where(id=balance.businessid).get()
            
            msg = rsp.balances.add()
            msg.business.CopyFrom(util.business_proto(bsn))
            msg.point_balance = balance.points
            
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

    def AwaitTransaction(self, request, context):
        x = []
        self.log.info("Starting await for user {}", request.user_id)
        def update_x(itm):
            self.log.info("Notifying awaiter on {}",request.user_id)
            x.append(itm)
        self.notifier.add_waiter(request.user_id, update_x)
        nones = 0
        while not x:
            time.sleep(KEEPALIVE_TIME)
            nones += 1
            if nones > 50:
                yield cpb.AwaitRsp(action=False)
                nones = 0
        businessid, name, change = x[0]
        self.log.info("Returning await answer.")
        yield cpb.AwaitRsp(
            action=True,
            point_change = change,
            business_id = businessid,
            business_name = name)
        
