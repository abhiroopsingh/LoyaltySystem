from genproto import pos_client_pb2 as ppb
from genproto import base_pb2 as bpb
import data
import util


class SaleServer(ppb.PointOfSaleServicer):
    def __init__(self, db, logger):
        self.db = db
        self.log = logger


    def Redeem(self, request, context):
        return None

    def Accrue(self, request, context):
        cust_id = request.customer_id
        bsn_id = request.business_id
        
        failure = ppb.AccrualResponse(success=False)

        if not util.exists(self.db.users(), cust_id):
            return failure

        if not util.exists(self.db.businesses(), bsn_id):
            return failure
        
        
        act = self.db.accounts().where(customerid=cust_id).where(businessid=bsn_id).get()

        if not act:
            return failure

        self.log.info("Accruing {} points to customer {}", request.point_amount, cust_id)
        act.points += request.point_amount
        self.db.update_account(act)
        
        return ppb.AccrualResponse(success=True)
