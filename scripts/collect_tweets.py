"""
This script collects tweets that contain the keyword

argv[1]: keyword to search
argv[2]: number of tweets
argv[-1]: filename of output

"""
import utils
import tweepy
import json
import sys

if __name__ == "__main__":
    logger = utils.get_logger(__name__)

    # parse the input parameters
    keyword = sys.argv[1]
    n_tweets = int(sys.argv[2])
    output_filename = sys.argv[-1]

    logger.info(f"Searching {n_tweets} tweets with keyword: {keyword}")

    # load the Twitter app keys
    with open("keys.json") as f:
        keys = json.load(f)

    # authenticate the app
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True)


    logger.info("Start to fetch the tweets")
    tweets = []
    for status in tweepy.Cursor(
        api.search,
        keyword,
        count=100
    ).items(n_tweets):
        tweets.append(status._json)
        if len(tweets) % 100 == 0:
            logger.info(f"Fetched {len(tweets)} tweets")

    logger.info("Start to dump the tweets")
    with open(output_filename, "w") as f:
        for tweet in tweets:
            tweet_str = json.dumps(tweet) + "\n"
            f.write(tweet_str)