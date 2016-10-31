import customer_handler
import memory_persist
import log

PORT = 5051

def run_debug_ephemeral():
    """ Runs the server in debugging configuration, with
    an in-memory database."""
    log = log.PrintLogger()
    db = memory_persist.MemoryPersist()

    cust = customer_handler.CustomerServer(db, log)

    serve(PORT, cust)



def serve(port, cust_server):
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  route_guide_pb2.add_CustomerServerServicer_to_server(
      cust_server, server)
  server.add_insecure_port('[::]:{}'.format(port))
  server.start()
