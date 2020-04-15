from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials

class TwitterStreamer():

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        Listener = stdOutListener()
        auth = OAuthHandler()
        auth.set_access_token()

        stream = Stream(auth, listener))
        stream.filter(track=hash_tag_list)

class stdOutListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:

            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True

    def on_error(self, data):
        print(status)

if __name__ = "__main__":
    Listener = stdOutListener()
    auth = OAuthHandler()
    auth.set_access_token()

    stream = Stream(auth, listener))
    stream.filter(track=['WHO', "covid-19", "coronavirus"])
