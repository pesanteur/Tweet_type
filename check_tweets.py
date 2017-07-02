from oauth import login
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweepy

analyzer = SentimentIntensityAnalyzer()
api = login()[2]

def check_tweets(username):
    pos_stats = []
    neg_stats = []

    page_list = []

    for page in tweepy.Cursor(api.user_timeline,count=200, id=username).pages(16): # gets all pages with tweets up to 3200 tweet maximum
        page_list.append(page)

    for page in page_list:
        for tweet in page:
            if "RT" in tweet.text:
                continue
            vs = analyzer.polarity_scores(tweet.text)
            negative = vs['neg']
            positive = vs['pos']
            neg_stats.append(negative)
            pos_stats.append(positive)

    pos_score = sum(pos_stats)/len(pos_stats)
    neg_score = sum(neg_stats)/len(neg_stats)

    return pos_score, neg_score
