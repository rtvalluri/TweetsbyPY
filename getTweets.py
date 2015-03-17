import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

print "Please Enter Twitter username to retrieve first 5 tweets : "
name = raw_input()

api = tweepy.API(auth)

user_tweets = api.user_timeline(name)

for i in range(5) : 
 	print user_tweets[i].text