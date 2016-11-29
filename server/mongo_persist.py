import persistence
import data
from pymongo import MongoClient
import attr

def dictify(obj):
    return {'$set':attr.asdict(obj)}

def idquery(obj):
    return {'id': obj.id}

def deserialize(obj, atrtype):
    del obj['_id']
    return atrtype(**obj)

class MongoQueryExecutor(object):
    def __init__(self, collection, typ):
        self.db = collection
        self.typ = typ

    def get(self, query):
        return deserialize(self.db.find_one(query.searchfor), self.typ)

    def all(self, query):
        return (deserialize(d, self.typ) for d in self.db.find(query.searchfor))
    
    def len(self, query):
        return self.db.find(query.searchfor).count()
    
class MongoPersist(object):
    def __init__(self, db_address='mongodb://localhost:27017/', dbname = 'loyalty_sys', clear_old = False):
        client = MongoClient(db_address)
        if clear_old:
            client.drop_database(dbname)
        db = client[dbname]
        self._transactions = db.transactions
        self._accounts = db.accounts
        self._businesses = db.businesses
        self._users = db.users
        
    def users(self):
        return persistence.Query(MongoQueryExecutor(self._users, data.User))
    
    def update_user(self, user):
        self._users.update_one(idquery(user), dictify(user), True)

        
    def accounts(self):
        return persistence.Query(MongoQueryExecutor(self._accounts, data.AccountBalance))

    def update_account(self, act):
        self._accounts.update_one(idquery(act), dictify(act),True)
    
    def businesses(self):
        return persistence.Query(MongoQueryExecutor(self._businesses, data.Business))
    
    def update_business(self, bsn):
        self._businesses.update_one(idquery(bsn), dictify(bsn), True)

    def transactions(self):
        return persistence.Query(MongoQueryExecutor(self._transactions, data.Transaction))

    def update_transaction(self, trns):
        self._transactions.update_one(idquery(trns), dictify(trns))
