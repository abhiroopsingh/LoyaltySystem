from genproto import consumer_client_pb2, auth_pb2
import grpc
import customer_handler
import auth
import memory_persist
import log
import demo_data
from concurrent import futures

PORT = 5051

def run_debug_ephemeral():
    """ Runs the server in debugging configuration, with
    an in-memory database."""
    logger = log.PrintLogger()
    db = memory_persist.MemoryPersist()
    demo_data.add_demo_data(db)
    

    cust = customer_handler.CustomerServer(db, logger)
    auths = auth.FakeLoginSvc(db, logger)

    serve(PORT, auths, cust)



def serve(port, auth_server, cust_server):
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  consumer_client_pb2.add_CustomerServerServicer_to_server(
      cust_server, server)
  auth_pb2.add_LoginServicer_to_server(
      auth_server, server)
  server.add_insecure_port('[::]:{}'.format(port))
  server.start()
  print("Serving on {}".format(port))
  while True:
      pass

  
if __name__ == "__main__":
    run_debug_ephemeral()
