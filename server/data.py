from collections import namedtuple

# Represents the basic representations of domain objects that will be used in the system.



User = namedtuple("User", [
    "id",
    "username",
    "name",
    "passhash",
    "token",
    "balances"
])

AccountBalance = namedtuple("AccountBalance", [
    "businessid",
    "points",
])


Business = namedtuple("Business", [
    "name",
    "id"
])
