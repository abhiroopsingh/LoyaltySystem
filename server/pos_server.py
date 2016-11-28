from genproto import pos_client_pb2 as ppb
from genproto import base_pb2 as bpb
import data
import util
from datetime import datetime

class SaleServer(ppb.PointOfSaleServicer):
    def __init__(self, db, logger, notifier):
        self.db = db
        self.log = logger
        self.notifier = notifier


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

        bsn_name = self.db.businesses().where(id=bsn_id).get().name
        
        act = self.db.accounts().where(customerid=cust_id).where(businessid=bsn_id).get()

        if not act:
            return failure

        self.log.info("Accruing {} points to customer {}", request.point_amount, cust_id)
        act.points += request.point_amount
        trans = data.Transaction(bsn_id, cust_id, request.point_amount, int(datetime.now().strftime("%s")))
        self.db.update_transaction(trans)
        self.db.update_account(act)
        self.notifier.notify(cust_id, (bsn_id, bsn_name, request.point_amount))
        return ppb.AccrualResponse(success=True)

    def GetBusinessInfo(self, req, context):
        if not util.exists(self.db.businesses(), req.id):
            raise Exception("No such business {}".format(req.id))

        bs = self.db.businesses().where(id=req.id).get()
        return ppb.BusinessInfo(
            id = bs.id,
            name = bs.name)

        
