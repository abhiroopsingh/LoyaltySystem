from genproto import consumer_client_pb2 as cpb
from genproto import base_pb2 as bpb
import unittest
import test_harness
import customer_handler as custhand

class TestCustomerServer(unittest.TestCase):
    def setUp(self):
        db, logger, notifier = test_harness.setup()
        self.db = db
        self.logger = logger
        self.notifier = notifier

        self.cust = custhand.CustomerServer(db, logger, notifier)

    def test_balances(self):
        rsp = self.cust.GetBalances(
            cpb.BalanceRequest(customer_id=7)
            , None)

        sortedb = sorted(rsp.balances, key=lambda s:s.business.name)
        self.assertEquals([s.point_balance for s in sortedb], [8,10])
        self.assertEquals([s.business.name for s in sortedb], [u"Flourish And Botts",
                                                               u"Ollivander's"])

    def test_await_transaction(self):
        from concurrent import futures
        tp = futures.ThreadPoolExecutor(4)
        # Shorten keepalive so that this test goes faster.
        oldtime = custhand.KEEPALIVE_TIME
        custhand.KEEPALIVE_TIME = 0.001
        ft = tp.submit(self.cust.AwaitTransaction,
                       cpb.AwaitReq(user_id=0),
                       None)

        items = ft.result()
        still_waiting = next(items)
        self.notifier.notify(0, (1,"Foo",1))
        response = next(items)
        self.assertFalse(still_waiting.action)
        self.assertTrue(response.action)
        self.assertEquals(response.point_change, 1)
        custhand.KEEPALIVE_TIME = oldtime
