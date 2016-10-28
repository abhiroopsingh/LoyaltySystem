from genproto import auth_pb2 as apb
from os import urandom

NONCE_LEN = 256/8
RAND = random.SystemRandom()

def get_nonce():
    return urandom(NONCE_LEN)
    

class LoginSvc(apb.LoginServicer):
    """ Implementation of the authenication and login service
    that checks tokens for the users. """
    def __init__(self, db):
        self.db = db
        
    def StartAuth(self, request, context):
        pass

    def DoAuth(self, request, context):
        pass

    def check_validity(self, metadata):
        """ Check to ensure this request metadata has
        the correct token. """
        pass

    def generate_token(self, user):
        pass
