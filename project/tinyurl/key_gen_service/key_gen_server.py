from concurrent import futures
import os
import time

import grpc

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
import keygen_pb2_grpc
import model as cql_model

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class KeyGenServicer(keygen_pb2_grpc.KeyGenServicer):
    def GetKeys(self, request, context):
        queryset = cql_model.Key.objects(available=True).limit(20)
        queryset.update(available=False)
        for item in queryset:
            yield keygen_pb2.Key(id=item['id'])


def serve():
    connection.setup(['127.0.0.1'], "tinyurl", lazy_connect=True,
        retry_connect=True, protocol_version=3)
    sync_table(cql_model.Key)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    keygen_pb2_grpc.add_KeyGenServicer_to_server(
        KeyGenServicer(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
        os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'
    serve()

