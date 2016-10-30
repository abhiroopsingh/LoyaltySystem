import attr

# Represents the basic representations of domain objects that will be used in the system.



@attr.s
class User(object):
    id = attr.ib()
    username = attr.ib()
    name = attr.ib()
    passhash = attr.ib()
    token = attr.ib(default="")
    balances = attr.ib(default=attr.Factory(list))
    
@attr.s
class AccountBalance(object):
    businessid = attr.ib()
    points = attr.ib(default=0)

@attr.s
class Business(object):
    name = attr.ib()
    id = attr.ib()
