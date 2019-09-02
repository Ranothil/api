# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import types_pb2 as types__pb2


class MessagesProxyStub(object):
  """*
  Service for entries streaming
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SubscribeBaseArticle = channel.unary_stream(
        '/MessagesProxy/SubscribeBaseArticle',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.PublicModel.FromString,
        )
    self.SubscribeBaseTweet = channel.unary_stream(
        '/MessagesProxy/SubscribeBaseTweet',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.PublicModel.FromString,
        )
    self.SubscribeBaseReddit = channel.unary_stream(
        '/MessagesProxy/SubscribeBaseReddit',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.PublicModel.FromString,
        )
    self.SubscribeBaseTelegram = channel.unary_stream(
        '/MessagesProxy/SubscribeBaseTelegram',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.PublicModel.FromString,
        )
    self.SubscribeBaseBitmex = channel.unary_stream(
        '/MessagesProxy/SubscribeBaseBitmex',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.PublicModel.FromString,
        )
    self.SubscribeArticle = channel.unary_stream(
        '/MessagesProxy/SubscribeArticle',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.Article.FromString,
        )
    self.SubscribeTweet = channel.unary_stream(
        '/MessagesProxy/SubscribeTweet',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.Tweet.FromString,
        )
    self.SubscribeReddit = channel.unary_stream(
        '/MessagesProxy/SubscribeReddit',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.RedditPost.FromString,
        )
    self.SubscribeTelegram = channel.unary_stream(
        '/MessagesProxy/SubscribeTelegram',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.TelegramUserMessage.FromString,
        )
    self.SubscribeBitmex = channel.unary_stream(
        '/MessagesProxy/SubscribeBitmex',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.BitmexUserMessage.FromString,
        )


class MessagesProxyServicer(object):
  """*
  Service for entries streaming
  """

  def SubscribeBaseArticle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeBaseTweet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeBaseReddit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeBaseTelegram(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeBaseBitmex(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeArticle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeTweet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeReddit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeTelegram(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeBitmex(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessagesProxyServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SubscribeBaseArticle': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeBaseArticle,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.PublicModel.SerializeToString,
      ),
      'SubscribeBaseTweet': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeBaseTweet,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.PublicModel.SerializeToString,
      ),
      'SubscribeBaseReddit': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeBaseReddit,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.PublicModel.SerializeToString,
      ),
      'SubscribeBaseTelegram': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeBaseTelegram,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.PublicModel.SerializeToString,
      ),
      'SubscribeBaseBitmex': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeBaseBitmex,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.PublicModel.SerializeToString,
      ),
      'SubscribeArticle': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeArticle,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.Article.SerializeToString,
      ),
      'SubscribeTweet': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeTweet,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.Tweet.SerializeToString,
      ),
      'SubscribeReddit': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeReddit,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.RedditPost.SerializeToString,
      ),
      'SubscribeTelegram': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeTelegram,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.TelegramUserMessage.SerializeToString,
      ),
      'SubscribeBitmex': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeBitmex,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.BitmexUserMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MessagesProxy', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class DatasetStub(object):
  """*
  Service for requesting data from dataset
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Assets = channel.unary_unary(
        '/Dataset/Assets',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=types__pb2.AssetItems.FromString,
        )


class DatasetServicer(object):
  """*
  Service for requesting data from dataset
  """

  def Assets(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatasetServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Assets': grpc.unary_unary_rpc_method_handler(
          servicer.Assets,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=types__pb2.AssetItems.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Dataset', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class HistoricDataStub(object):
  """*
  Service for requesting historic data
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HistoricBaseTweets = channel.unary_stream(
        '/HistoricData/HistoricBaseTweets',
        request_serializer=types__pb2.HistoricRequest.SerializeToString,
        response_deserializer=types__pb2.PublicModel.FromString,
        )
    self.HistoricBaseArticles = channel.unary_stream(
        '/HistoricData/HistoricBaseArticles',
        request_serializer=types__pb2.HistoricRequest.SerializeToString,
        response_deserializer=types__pb2.PublicModel.FromString,
        )
    self.HistoricBaseRedditPosts = channel.unary_stream(
        '/HistoricData/HistoricBaseRedditPosts',
        request_serializer=types__pb2.HistoricRequest.SerializeToString,
        response_deserializer=types__pb2.PublicModel.FromString,
        )
    self.HistoricTweets = channel.unary_stream(
        '/HistoricData/HistoricTweets',
        request_serializer=types__pb2.HistoricRequest.SerializeToString,
        response_deserializer=types__pb2.Tweet.FromString,
        )
    self.HistoricArticles = channel.unary_stream(
        '/HistoricData/HistoricArticles',
        request_serializer=types__pb2.HistoricRequest.SerializeToString,
        response_deserializer=types__pb2.Article.FromString,
        )
    self.HistoricRedditPosts = channel.unary_stream(
        '/HistoricData/HistoricRedditPosts',
        request_serializer=types__pb2.HistoricRequest.SerializeToString,
        response_deserializer=types__pb2.RedditPost.FromString,
        )


class HistoricDataServicer(object):
  """*
  Service for requesting historic data
  """

  def HistoricBaseTweets(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricBaseArticles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricBaseRedditPosts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricTweets(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricArticles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricRedditPosts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HistoricDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HistoricBaseTweets': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricBaseTweets,
          request_deserializer=types__pb2.HistoricRequest.FromString,
          response_serializer=types__pb2.PublicModel.SerializeToString,
      ),
      'HistoricBaseArticles': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricBaseArticles,
          request_deserializer=types__pb2.HistoricRequest.FromString,
          response_serializer=types__pb2.PublicModel.SerializeToString,
      ),
      'HistoricBaseRedditPosts': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricBaseRedditPosts,
          request_deserializer=types__pb2.HistoricRequest.FromString,
          response_serializer=types__pb2.PublicModel.SerializeToString,
      ),
      'HistoricTweets': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricTweets,
          request_deserializer=types__pb2.HistoricRequest.FromString,
          response_serializer=types__pb2.Tweet.SerializeToString,
      ),
      'HistoricArticles': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricArticles,
          request_deserializer=types__pb2.HistoricRequest.FromString,
          response_serializer=types__pb2.Article.SerializeToString,
      ),
      'HistoricRedditPosts': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricRedditPosts,
          request_deserializer=types__pb2.HistoricRequest.FromString,
          response_serializer=types__pb2.RedditPost.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'HistoricData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SentimentsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HistoricSocialSentiment = channel.unary_stream(
        '/Sentiments/HistoricSocialSentiment',
        request_serializer=types__pb2.SentimentHistoricRequest.SerializeToString,
        response_deserializer=types__pb2.AggregationCandle.FromString,
        )
    self.HistoricNewsSentiment = channel.unary_stream(
        '/Sentiments/HistoricNewsSentiment',
        request_serializer=types__pb2.SentimentHistoricRequest.SerializeToString,
        response_deserializer=types__pb2.AggregationCandle.FromString,
        )
    self.SubscribeSocialSentiment = channel.unary_stream(
        '/Sentiments/SubscribeSocialSentiment',
        request_serializer=types__pb2.AggregationCandleFilter.SerializeToString,
        response_deserializer=types__pb2.AggregationCandle.FromString,
        )
    self.SubscribeNewsSentiment = channel.unary_stream(
        '/Sentiments/SubscribeNewsSentiment',
        request_serializer=types__pb2.AggregationCandleFilter.SerializeToString,
        response_deserializer=types__pb2.AggregationCandle.FromString,
        )


class SentimentsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def HistoricSocialSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricNewsSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeSocialSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeNewsSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SentimentsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HistoricSocialSentiment': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricSocialSentiment,
          request_deserializer=types__pb2.SentimentHistoricRequest.FromString,
          response_serializer=types__pb2.AggregationCandle.SerializeToString,
      ),
      'HistoricNewsSentiment': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricNewsSentiment,
          request_deserializer=types__pb2.SentimentHistoricRequest.FromString,
          response_serializer=types__pb2.AggregationCandle.SerializeToString,
      ),
      'SubscribeSocialSentiment': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeSocialSentiment,
          request_deserializer=types__pb2.AggregationCandleFilter.FromString,
          response_serializer=types__pb2.AggregationCandle.SerializeToString,
      ),
      'SubscribeNewsSentiment': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeNewsSentiment,
          request_deserializer=types__pb2.AggregationCandleFilter.FromString,
          response_serializer=types__pb2.AggregationCandle.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Sentiments', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
