from genproto import transactions_pb2 as tpb

class TransactionLog(object):
    def __init__(self, db):
        self.db = db
        
    def add_transaction(self, trans):
        self.db.update_transaction(trans)

    def get_customer_trans(self, customerid):
        return self.db.transactions().where(customerid=customerid).all()

    def get_business_trans(self, businessid):
        return self.db.transactions().where(businessid=businessid).all()

class TransactionProvider(tpb.TransactionProviderServicer):
    def __init__(self, db, tlog):
        self.db = db
        self.transaction_log = tlog

    def CustomerTransactions(self, request, context):
        ts = self.transaction_log.get_customer_trans(request.customer_id)
        return util.transactions(ts, self.db)

    def BusinessTransactions(self, request, context):
        ts = self.transaction_log.get_business_trans(request.business_id)
        return util.transactions(ts, self.db)
    
    
