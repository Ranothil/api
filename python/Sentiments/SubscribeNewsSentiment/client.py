import sys; sys.path.append('../../') # for correct types inclusion,

import grpc

import types_pb2
import types_pb2_grpc


SERVER_ADDRESS = 'SERVER'
PATH_TO_CERT_FILE = './cert.pem'

def main():
    # Create credentials for use with an secured channel
    credentials = grpc.ssl_channel_credentials(open(PATH_TO_CERT_FILE, 'rb').read())

    # uncomment commands below if token auth is required
    # call_credentials = grpc.access_token_call_credentials('YOUR_TOKEN')
    # credentials = grpc.composite_channel_credentials(credentials, call_credentials)

    channel = grpc.secure_channel(SERVER_ADDRESS, credentials)
    
    # create stub
    stub = types_pb2_grpc.SentimentsStub(channel)

    # create request
    req = types_pb2.AggregationCandleFilter(resolution='M1', assets_filter=types_pb2.AssetsFilter(assets = ['BTC'], all_assets = False))
   
    # Response-streaming RPC
    candle_stream = stub.SubscribeNewsSentiment(req)
    for candle in candle_stream:
        # attributes are same as defined in proto messages
        print(candle.id, candle.a)


if __name__ == '__main__':
    main()
