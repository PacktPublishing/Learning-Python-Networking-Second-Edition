#! /usr/bin/python3

import twitter, json

def twitter_connection(file):
	'''Create the object from which the Twitter API will be consumed,
	reading the credentials from a file, defined in path parameter.'''
	(CONSUMER_KEY,
     CONSUMER_SECRET,
     OAUTH_TOKEN,
     OAUTH_TOKEN_SECRET) = open(file, 'r').read().splitlines()
	auth = twitter.oauth.OAuth(OAUTH_TOKEN,
                               OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY,
                               CONSUMER_SECRET)
	return twitter.Twitter(auth=auth)

def recently_tweets(tw, search_term):
	'''Get the last 10 tweets in English from a specific search.'''
	search = tw.search.tweets(q=search_term, lang="en", count="10")["statuses"]
	return search

def save_tweets(tweets, file):
	'''Store the tweets in JSON format in the specified file.'''
	with open(file, "w") as f:
		json.dump(tweets, f, indent=1)


def main(file='tweets.json'):
	try:
		search_term = input("Enter the search term in twitter : ")
		tw = twitter_connection("credentials.txt")
		tweets = recently_tweets(tw, search_term)
		save_tweets(tweets, file)
	except Exception as e:
		print(str(e))

if __name__ == "__main__":
	main()