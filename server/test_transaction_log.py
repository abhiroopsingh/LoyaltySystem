import unittest
import transaction_log
import test_harness
import data
import util

class TestTransactionLog(unittest.TestCase):
    def setUp(self):
        db, logger, notifier = test_harness.setup()
        self.tlog = transaction_log.TransactionLog(db)
        self.db = db

    def test_get_customer_trans(self):
        # test on the demo data that's in there.
        trans = self.tlog.get_customer_trans(7)
        self.assertEquals(len(trans), 3)
        # Test for internal consistency, sum of transactions
        # equals the balance.
        self.assertEquals(sum(t.points for t in trans),
                          self.db.accounts().where(customerid=7,businessid=0).get().points)

    def test_business_trans(self):
        trans = self.tlog.get_business_trans(0)
        self.assertEquals(len(trans), 3)

    def test_add(self):
        self.tlog.add_transaction(data.Transaction(
            businessid=0,
            customerid=7,
            points=10,
            time=util.time_sec()))
        self.assertEquals(len(self.tlog.get_business_trans(0)),4)
        self.assertEquals(len(self.tlog.get_customer_trans(7)),4)
        
        
