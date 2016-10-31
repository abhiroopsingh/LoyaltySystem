from genproto import auth_pb2 as apb
from os import urandom
import hashlib

NONCE_LEN = 256/8

def get_nonce():
    return urandom(NONCE_LEN)


class FakeLoginSvc(apb.LoginServicer):
    """ Fake implementation that accepts any crypto. """
    def __init__(self, db, logger):
        self.db = db
        self.log = logger

    def StartAuth(self, request, context):
        user = self.db.users().where(username=request.username).get()
        user.token = 'FAKE'
        self.db.update_user(user)

        return apb.StartAuthResponse(
            username = user.username,
            id = user.id,
            nonce = 'FAKE'
        )

    def DoAuth(self, request, context):
        user = self.db.users().where(id=request.id).get()
        if not user:
            return apb.DoAuthResponse(success=False)

        return apb.DoAuthResponse(
            auth = apb.UserAuth(
                id = user.id,
                token = "FAKE",
                authorized_business = user.authorized_business
            ),
            success = True
        )
        

class LoginSvc(apb.LoginServicer):
    """ Implementation of the authenication and login service
    that checks tokens for the users. """
    def __init__(self, db, logger):
        self.db = db
        self.log = logger
        
    def StartAuth(self, request, context):
        user = self.db.users().where(username=request.username).get()
        nonce, token = self.generate_token(user)
        user.token = token
        self.db.update_user(user)

        return apb.StartAuthResponse(
            username = user.username,
            id = user.id,
            nonce = nonce
        )

    
    def DoAuth(self, request, context):
        user = self.db.users().where(id=request.id).get()
        if not user:
            return apb.DoAuthResponse(success = False)
        
        req_token = request.hash_token
        good_token = user.token
        if good_token == req_token:
            # auth passes
            return apb.DoAuthResponse(
                auth = apb.UserAuth(
                    id = user.id,
                    token = good_token
                ),
                success = True
            )
        
        return apb.DoAuthResponse(success = False)
                
    def generate_token(self, user):
        nonce = get_nonce()
        salted = (str(nonce) + user.passhash)
        hashedtoken = hashlib.sha256(salted)
        return nonce, hashedtoken.hexdigest()
        
