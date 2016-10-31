from genproto import consumer_client_pb2, auth_pb2, pos_client_pb2
import grpc
import customer_handler
import auth
import pos_server
import memory_persist
import log
import demo_data
from concurrent import futures

PORT = 50051

def run_debug_ephemeral():
    """ Runs the server in debugging configuration, with
    an in-memory database."""
    logger = log.PrintLogger()
    db = memory_persist.MemoryPersist()
    demo_data.add_demo_data(db)
    

    cust = customer_handler.CustomerServer(db, logger)
    auths = auth.FakeLoginSvc(db, logger)
    sales = pos_server.SaleServer(db, logger)

    serve(PORT, auths, cust, sales)



def serve(port, auth_server, cust_server, sales):
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  consumer_client_pb2.add_CustomerServerServicer_to_server(
      cust_server, server)
  auth_pb2.add_LoginServicer_to_server(
      auth_server, server)
  pos_client_pb2.add_PointOfSaleServicer_to_server(
      sales, server
      )
  server.add_insecure_port('[::]:{}'.format(port))
  server.start()
  print("Serving on {}".format(port))
  while True:
      pass

  
if __name__ == "__main__":
    run_debug_ephemeral()
