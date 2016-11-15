from genproto import consumer_client_pb2, auth_pb2, pos_client_pb2
import grpc
import customer_handler
import auth
import pos_server
import memory_persist
import log
import demo_data
import notification_system
from concurrent import futures

from analytics import dashboard

PORT = 50051
AN_PORT = 80

def run_debug_ephemeral():
    """ Runs the server in debugging configuration, with
    an in-memory database."""
    logger = log.PrintLogger()
    db = memory_persist.MemoryPersist()
    demo_data.add_demo_data(db)

    notifier = notification_system.NotificationServer()
    
    cust = customer_handler.CustomerServer(db, logger, notifier)
    auths = auth.FakeLoginSvc(db, logger)
    sales = pos_server.SaleServer(db, logger, notifier)

    serve(PORT, db, auths, cust, sales)

def show_analytics(port, auth, database):
    dashboard.start(database, port)

def serve(port, database, auth_server, cust_server, sales):
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

  show_analytics(AN_PORT, auth_server, database)
  while True:
      pass

  
if __name__ == "__main__":
    run_debug_ephemeral()
