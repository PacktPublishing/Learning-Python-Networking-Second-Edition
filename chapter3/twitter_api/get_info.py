#! /usr/bin/python3

import twitter 
 
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
	 
def get_info_twitter(tw):
	query = tw.search.tweets(q="#python", lang="en", count="10")["statuses"]
	for q in query:
		for key,value in q.items():
			if(key=='text'):
				print(value+'\n')

def main():
	try:
		tw = twitter_connection("credentials.txt")
		get_info_twitter(tw)
	except Exception as e:
		print(str(e))
		
if __name__ == "__main__":
	main()