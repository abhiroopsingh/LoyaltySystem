import attr
import uuid
# Represents the basic representations of domain objects that will be used in the system.



@attr.s
class User(object):
    id = attr.ib()
    username = attr.ib()
    name = attr.ib()
    passhash = attr.ib()
    token = attr.ib(default="")
    authorized_business = attr.ib(default=None)
    
@attr.s
class AccountBalance(object):
    id = attr.ib()
    businessid = attr.ib()
    customerid = attr.ib()
    points = attr.ib(default=0)

@attr.s
class Business(object):
    name = attr.ib()
    id = attr.ib()
    thumbnail = attr.ib()
