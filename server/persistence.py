

# Persistence defines an abstraction for the persistence layer.
# For tests and local executions it can be run in memory,
# or it can scale outward to one (or more sharded) databases.

class Query(object):
    def __init__(self, executor, search = {}):
        self.searchfor = search.copy()
        self.executor = executor
        
    def where(self, **kwargs):
        q = Query(self.executor, self.searchfor)
        q.searchfor.update(kwargs)
        return q
    
    def get(self):
        return self.executor.get(self)

    def all(self):
        return self.executor.all(self)

    def len(self):
        return self.executor.len(self)
    

class BasePersistence(object):

    def users(self):
        """ Return a query object to search for
        users."""
        raise NotImplementedError()

    def update_user(self, user):
        raise NotImplementedError()

    def businesses(self):
        """ Return a query object to search for
        businesses. """
        raise NotImplementedError()

    def update_business(self, business):
        raise NotImplementedError()

    def accounts(self):
        raise NotImplementedError()

    def update_account(self, account):
        raise NotImplementedError()
