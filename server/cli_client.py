from genproto.auth_pb2 import *
from genproto.base_pb2 import *
from genproto.consumer_client_pb2 import *


# This is a special client for the system that connects using python
# and provides a command line interface to try out different tasks.

PORT = 50051

channel = grpc.insecure_channel('localhost:{}'.format(PORT))


authstub = LoginStub(channel)
userstub = CustomerServerStub(channel)


def balance(userid):
    return userstub.GetBalances(BalanceRequest(customer_id=userid))
