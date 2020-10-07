# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pingpong_pb2 as pingpong__pb2


class PingPongServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.pingPong = channel.unary_unary(
                '/pingpong.PingPongService/pingPong',
                request_serializer=pingpong__pb2.PingRequest.SerializeToString,
                response_deserializer=pingpong__pb2.PongResponse.FromString,
                )


class PingPongServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def pingPong(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PingPongServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'pingPong': grpc.unary_unary_rpc_method_handler(
                    servicer.pingPong,
                    request_deserializer=pingpong__pb2.PingRequest.FromString,
                    response_serializer=pingpong__pb2.PongResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pingpong.PingPongService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PingPongService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def pingPong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pingpong.PingPongService/pingPong',
            pingpong__pb2.PingRequest.SerializeToString,
            pingpong__pb2.PongResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)