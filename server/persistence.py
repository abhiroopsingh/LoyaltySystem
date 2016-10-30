

# Persistence defines an abstraction for the persistence layer.
# For tests and local executions it can be run in memory,
# or it can scale outward to one (or more sharded) databases.

class BasePersistence(object):

    def find_user(self, **kwargs):
        """ Find a user by looking for the
        matching value for the attribute
        specified in kwargs. Return None if not found."""
        raise NotImplementedError()

    def update_user(self, user):
        raise NotImplementedError()

    def find_business(self, **kwargs):
        """ Find a business by looking for the
        matching value for the attribute in kwargs.
        Returns None if not found."""
        raise NotImplementedError()

    def update_business(self, business):
        raise NotImplementedError()
    
