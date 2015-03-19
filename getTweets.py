import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #Add your consumer_key and consumer_secret here
auth.set_access_token(access_token, access_token_secret) #Add your access_token and token_secret here

print "Please Enter Twitter username to retrieve first 5 tweets : "
name = raw_input()

api = tweepy.API(auth)

user_tweets = api.user_timeline(name) # "api.home_timeline()" for public timeline

for i in range(5) : 
 	print user_tweets[i].text