import persistence
from data import *


class IndexedItems(object):
    """ IndexedItems stores a set of 
    indices that allow for fast lookups on items.
    It allows multiple indices to be kept in sync."""
    
    def __init__(self):
        self.indices = []
        
    def add_indexer(self, indexer):
        self.indices.append(indexer)
        return indexer
    
    def add_index_func(self, name, indexer_func):
        ind = Indexer(name, indexer_func)
        return self.add_indexer(ind)
    
    def add(self, item):
        for name, indexer in self.indices:
            indexer.update(item)

    def find(self, **kwargs):
        for indexer in self.indices:
            if indexer.name in kwargs:
                return indexer.find(kwargs[name])
            
class Indexer(object):
    """ An indexer stores one index and lookup
    function to be used in an IndexedItems group."""
    def __init__(self, name, lookupfunc):
        """ Takes a function that can extract the
        index from an object of this type. """
        self.indexer = lookupfunc
        self.name = name
        self.index = {}
        
    def find(self, indx):
        return self.index.get(indx)
    
    def update(self, itm):
        self.index[self.indexer[itm]] = itm

def attr_index(attribute):
    return Indexer(attribute.name, lambda x: x.__dict__[attribute.name])
        

class MemoryPersist(persistence.BasePersistence):
    """ MemoryPersist stores the entire database in 
    memory, which is suitable for tests. """
    
    def __init__(self):
        self.users = IndexedItems()
        self.users.add_indexer(attr_index(User.id))
        self.users.add_indexer(attr_index(User.username))

        # delegate user funcs.
        self.find_user = self.users.find
        self.update_user = self.users.add

        self.businesses = IndexedItems()
        self.businesses.add_indexer(attr_index(Business.name))
        self.businesses.add_indexer(attr_index(Business.id))
