from check_tweets import check_tweets
import unittest
from tweepy import TweepError

class TestTweetalyse(unittest.TestCase):
    def test_checktweets(self):
        self.assertTrue(check_tweets('realDonaldTrump'))
        self.assertEqual(check_tweets('realDonaldTrump'), check_tweets('realdonaldtrump'))
        with self.assertRaises(TweepError):
            check_tweets('fakername119567')

if __name__ == '__main__':
        unittest.main()

