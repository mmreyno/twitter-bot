from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterRestPager
import tweepy


### WORD(S) TO SEARCH FOR ###
TRACK_TERM = 'word'


### API STUFF FOR TWITTERAPI ###
CONSUMER_KEY = 'KEY'
CONSUMER_SECRET = 'SECRET'
ACCESS_TOKEN_KEY = 'KEY'
ACCESS_TOKEN_SECRET = 'SECRET'
api = TwitterAPI(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)


### API STUFF FOR TWEEPY ###
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
withtweepy = tweepy.API(auth)


### SEARCH TWITTER FOR THE TERMS TO EXTRACT TWEET NUMBER AND USER ID ###
def twittersearch():
	pager = TwitterRestPager(api, 'search/tweets', {'q': TRACK_TERM, 'count' : 100})
	for item in pager.get_iterator(wait=6):
		userid = item['user']['id']
		tweetid = item['id']
		print userid
		print tweetid
		favorite(tweetid)
		follow(userid)


### FAVORITE THE TWEETS WITH THE SELECTED TERMS ###
def favorite(tweetid):
	withtweepy.create_favorite(tweetid)


### FOLLOW THE USER WHO TWEETED THE TERM ###
def follow(userid):
	try:
		withtweepy.create_friendship(userid)
	except tweepy.error.TweepError:
		pass
                
if __name__ == '__main__':
        twittersearch()                