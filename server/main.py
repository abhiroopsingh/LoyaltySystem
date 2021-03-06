from genproto import consumer_client_pb2, auth_pb2, pos_client_pb2, transactions_pb2
import grpc
import customer_handler
import auth
import pos_server
import memory_persist
import log
import demo_data
import notification_system
import transaction_log
from concurrent import futures
import util

from analytics import dashboard

PORT = 50051
AN_PORT = 80

def run_debug_ephemeral():
    """ Runs the server in debugging configuration, with
    an in-memory database."""
    logger = log.PrintLogger()
    db = memory_persist.MemoryPersist()
    tlog = transaction_log.TransactionLog(db)
    demo_data.add_demo_data(db)

    notifier = notification_system.NotificationServer()
    
    cust = customer_handler.CustomerServer(db, logger, notifier)
    auths = auth.FakeLoginSvc(db, logger)
    sales = pos_server.SaleServer(db, logger, notifier)
    trans = transaction_log.TransactionProvider(db, tlog)

    serve(PORT, db, auths, cust, sales, trans)

def show_analytics(port, auth, database):
    dashboard.start(database, port, util)

def serve(port, database, auth_server, cust_server, sales, transprov):
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  consumer_client_pb2.add_CustomerServerServicer_to_server(
      cust_server, server)
  auth_pb2.add_LoginServicer_to_server(
      auth_server, server)
  pos_client_pb2.add_PointOfSaleServicer_to_server(
      sales, server
      )
  transactions_pb2.add_TransactionProviderServicer_to_server(
      transprov, server)
  server.add_insecure_port('[::]:{}'.format(port))
  server.start()
  print("Serving on {}".format(port))

  show_analytics(AN_PORT, auth_server, database)
  while True:
      pass

  
if __name__ == "__main__":
    run_debug_ephemeral()
