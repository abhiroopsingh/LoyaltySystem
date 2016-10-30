import persistence
from data import *
from collections import defaultdict
import itertools

class IndexedItems(object):
    """ IndexedItems stores a set of 
    indices that allow for fast lookups on items.
    It allows multiple indices to be kept in sync."""
    
    def __init__(self):
        self.indices = []
        
    def add_indexer(self, indexer):
        self.indices.append(indexer)
        return indexer
    
    def add(self, item):
        for indexer in self.indices:
            indexer.update(item)

    def find(self, index_name, value):
        for indexer in self.indices:
            if indexer.name == index_name:
                return indexer.match_key(value)
        return []

    def all(self, query):
        sf = list(query.searchfor.items())
        
        if not sf:
            return self.indices[0].all()
        
        startname, val = sf[0]
        results = set(self.find(startname, val))
        for index, value in sf[1:]:
            results.intersection_update(set(self.find(index,value)))

        return results

    def len(self, query):
        return sum(1 for _ in self.all(query))

    def get(self, query):
        res = list(self.all(query))
        assert len(res) == 1
        return res[0]
        
        
            
class Indexer(object):
    """ An indexer stores one index and lookup
    function to be used in an IndexedItems group."""
    def __init__(self, name, lookupfunc, pkey_func):
        """ Takes a function that can extract the
        index from an object of this type. """
        self.indexer = lookupfunc
        self.primary_key = pkey_func
        self.name = name
        self.index = defaultdict(dict)
            
    def update(self, itm):
        matching_keys = self.index[self.indexer(itm)]
        matching_keys[self.primary_key(itm)] = itm

    def match_key(self, key):
        return self.index[key].values()

    def all(self):
        return itertools.chain(e.values() for e in self.index.values())
    

def attr_index(attribute,pkey = None):
    if pkey is None:
        pkey = attribute

    pfun = lambda x:x.__dict__[pkey.name]
    afun = lambda x:x.__dict__[attribute.name]
    return Indexer(attribute.name, afun, pfun)
        

class MemoryPersist(persistence.BasePersistence):
    """ MemoryPersist stores the entire database in 
    memory, which is suitable for tests. """
    
    def __init__(self):
        self._users = IndexedItems()
        self._users.add_indexer(attr_index(User.id))
        self._users.add_indexer(attr_index(User.username, User.id))

        self._businesses = IndexedItems()
        self._businesses.add_indexer(attr_index(Business.name,
                                               Business.id))
        self._businesses.add_indexer(attr_index(Business.id))

        self.point_accounts = IndexedItems()
        self.point_accounts.add_indexer(attr_index(
            AccountBalance.businessid,
            AccountBalance.id))
        self.point_accounts.add_indexer(attr_index(
            AccountBalance.customerid,
            AccountBalance.id))

    def update_user(self, user):
        self._users.add(user)
        
    def users(self):
        return persistence.Query(self._users)

    def update_business(self, bsn):
        self._businesses.add(bsn)
        
    def businesses(self):
        return persistence.Query(self._businesses)

    def accounts(self):
        return persistence.Query(self.point_accounts)

    def update_account(self, act):
        self.point_accounts.add(act)
        
