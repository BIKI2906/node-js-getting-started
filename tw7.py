
import tweepy
import random
API_KEY = '97fFbX46iAhYDqiSmxOsrV6k1'
API_SECRET = 'NlzfhhVa8lMCRmCW3UymZeTxGkYj8QCFxnlvBuC0o1lzIWfEgh'
ACCESS_TOKEN = '1471680375240130561-IU4AuWiPU0Apkpj0zBiqbRGu3d7m1g'
ACCESS_TOKEN_SECRET = 'ATuVj82OKJLoEXvWRtQP2jVvWNNKe0GYAvG2WqeKHo3Rk'


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 

ramint = random.randint(0,999)
api.update_status(ramint)
