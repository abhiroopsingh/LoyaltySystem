import pos_server as ps
import unittest
import test_harness
import pos_server
import transaction_log
from genproto import pos_client_pb2 as ppb
from datetime import datetime

class TestPosServer(unittest.TestCase):
    def setUp(self):
        db, logger, notifier = test_harness.setup()
        self.db = db
        self.logger = logger
        self.notifier = notifier
        self.trans_log = transaction_log.TransactionLog(db)
        self.pos = pos_server.SaleServer(db, logger, notifier)

    def test_accrue(self):
        x = []
        def changex(act):
            if act == (0, 'Flourish And Botts', 10):
                x.append(True)

        self.notifier.add_waiter(0, changex)
            
        resp = self.pos.Accrue(
            ppb.AccrualRequest(
                customer_id = 0,
                business_id = 0,
                point_amount = 10
                ),
            None
            )
        self.assertEquals(resp.success, True)

        # make sure the balance has been incremented.
        balance = self.db.accounts().where(customerid=0).where(businessid=0).get()
        self.assertEquals(balance.points, 10)

        # make sure we were notified.
        self.assertTrue(x[0])

        # check the log.
        last_trans = list(self.trans_log.get_customer_trans(0))[-1]
        self.assertEquals(last_trans.time/10, int(datetime.now().strftime("%s"))/10)
        self.assertEquals(last_trans.points, 10)

    def test_getinfo(self):
        resp = self.pos.GetBusinessInfo(
            ppb.InfoReq(
                id=0
                ),
            None
        )
        self.assertEquals(u"Flourish And Botts", resp.name)
