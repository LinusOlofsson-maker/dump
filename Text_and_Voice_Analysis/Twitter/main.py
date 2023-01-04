from textblob import TextBlob
import tweepy
import sys

mykeys = open('twitterkeys.txt', 'r').read().splitlines()

api_key = mykeys[0]
api_key_secret = mykeys[1]
access_token = mykeys[3]
access_token_secret = mykeys[4]

#print(f'api:{api_key}\napi_sec:{api_key_secret}\naccess:{access_token}\naccess_sec:{access_token_secret}')

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'joe'
tweet_ammount = 200
tweets = tweepy.Cursor(api.search, q=search_term, lang = 'en').items(tweet_ammount)

polarity = 0
positive = 0
neutural = 0
negative = 0


for tweet in tweets:
    final_text = tweet.text.replace('RT', ' ')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position+2:]
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0.00:
        positive +=1
    elif tweet_polarity < 0.00:
        negative +=1
    elif tweet_polarity == 0.00:
        neutural +=1
    polarity+= tweet_polarity
    #print(final_text)

print(polarity)
print(f'Ammount of positive tweets:{positive}')
print(f'Ammount of neautral tweets:{neutural}')
print(f'Ammount of negatiev tweets:{negative}')