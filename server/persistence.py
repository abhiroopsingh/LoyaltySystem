

# Persistence defines an abstraction for the persistence layer.
# For tests and local executions it can be run in memory,
# or it can scale outward to one (or more sharded) databases.

class MemoryPersist:
    def __init__(self):
        self.usernames = {}
        self.userids = {}
        self.tokens = {}
        self.businesses = {}

    def find_username(self, username):
        return self.usernames.get(username, None)

    def add_user(self, userinfo):
        self.usernames[userinfo.username] = userinfo
        self.userids[userinfo.userid] = userinfo
