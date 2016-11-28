# Tests the inner machinery of the notification system.

import unittest
import notification_system


class TestNotificationSystem(unittest.TestCase):
    def setUp(self):
        self.ns = notification_system.NotificationServer()

    def test_empty_notify(self):
        try:
            self.ns.notify(0, None)
        except Exception as e:
            self.fail("Empty notify failed: {}".format(e))

    def test_one_waiter(self):
        resp = []
        def update_resp(x):
            resp.append(x)

        self.ns.add_waiter(0, update_resp)
        self.ns.notify(0, 50)
        self.assertEquals(sum(resp), 50)

    def test_many_waiters(self):
        resp = []
        def update_resp(x):
            resp.append(x)

        for x in range(10):
            self.ns.add_waiter(0, update_resp)
        self.ns.notify(0, 50)
        # All 10 should have fired.
        self.assertEquals(sum(resp), 500)

    def test_many_notifications(self):
        resp = []
        def update_resp(x):
            resp.append(x)
        self.ns.add_waiter(0, update_resp)
        for x in range(100):
            self.ns.notify(0, 50)
        # Only one should have fired.
        self.assertEquals(sum(resp), 50)
        
