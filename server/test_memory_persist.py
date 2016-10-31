import unittest
import memory_persist as mp
import data

class TestMemoryPersist(unittest.TestCase):
    def setUp(self):
        db = mp.MemoryPersist()
        self.db = db

        self.fake_usrs = [
            data.User(*d) for d in [
            [1, "foo", "Foo McFoo", "*****"],
            [2, "bar", "Bar McBar", "*****"],
            [3, "baz", "Baz McBaz", "*****"],
            [4, "mcfly", "Marty McFly", "****"],
            [5, "einstein", "Albert Einstein", "****"]]
        ]
        self.fake_businesses = [
            data.Business(*d) for d in [
            ["Gringotts", 1],
            ["Flourish and Blotts", 2]
        ]]

        self.fake_accts = [
            data.AccountBalance(*ab) for ab in [
                [1, 1, 4, 10],
                [2, 1, 5, 5],
                [3, 2, 4, 0],
        ]]

    def populate(self):
        for usr in self.fake_usrs:
            self.db.update_user(usr)
        for bsn in self.fake_businesses:
            self.db.update_business(bsn)
        for act in self.fake_accts:
            self.db.update_account(act)
        

    def test_update_add(self):
        self.db.update_user(self.fake_usrs[0])
        self.assertEquals(self.db.users().len(),1)

        # Changing the name should update this user.
        self.fake_usrs[0].name = "Foo Bar McFoo"
        self.db.update_user(self.fake_usrs[0])
        self.assertEquals(self.db.users().len(), 1)

        # Now we add another user.
        self.db.update_user(self.fake_usrs[1])
        self.assertEquals(self.db.users().len(), 2)

        # Now we add all the users.
        self.populate()
        self.assertEquals(self.db.users().len(), len(self.fake_usrs))
        
    def test_searching(self):
        self.populate()

        mfly = self.db.users().where(username="mcfly").get()
        self.assertEquals(mfly, self.fake_usrs[3])

        self.assertEquals(self.db.accounts().where(businessid=1).len(),2)
        self.assertEquals(self.db.accounts().where(customerid=4).len(),2)
        self.assertEquals(self.db.accounts()
                          .where(businessid=1)
                          .where(customerid=4).len(), 1)

        
            
