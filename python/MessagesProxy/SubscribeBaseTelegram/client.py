import sys; sys.path.append('../../') # for correct types inclusion,

import grpc

import types_pb2
import types_pb2_grpc

SERVER_ADDRESS = 'SERVER'
PATH_TO_CERT_FILE = './cert.pem'


def main():
    # Create credentials for use with an secured channel
    creds = grpc.ssl_channel_credentials(open(PATH_TO_CERT_FILE, 'rb').read())

    # Initialize GRPC channel
    channel = grpc.secure_channel(SERVER_ADDRESS, creds)
    
    # create stub
    stub = types_pb2_grpc.MessagesProxyStub(channel)

    # create request
    assets_filter = types_pb2.AssetsFilter(assets = ['BTC'], all_assets = False)

    # Response-streaming RPC
    telegram_stream = stub.SubscribeBaseTelegram(assets_filter)
    for telegram in telegram_stream:
        # attributes are same as defined in proto messages
        print(telegram.id, telegram.content)


if __name__ == '__main__':
    main()