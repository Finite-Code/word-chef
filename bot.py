import os
import tweepy
import requests

# Set up Twitter API credentials for OAuth 1.0a
auth = tweepy.OAuth1UserHandler(
    consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
    consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
)
api = tweepy.API(auth)

# Get a random word and its details
def get_random_word():
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/hello")
    word_data = response.json()
    word = word_data[0]['word']
    return word

def get_word_details(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}")
    details = response.json()
    if 'meanings' in details:
        meaning = details['meanings'][0]['definitions'][0]['definition']
        return meaning
    return "No definition found."

def tweet_word():
    word = get_random_word()
    definition = get_word_details(word)
    tweet_text = f"Word: {word}\nMeaning: {definition}\nExample Usage: [Example usage here]"
    try:
        api.update_status(status=tweet_text)
        print(f"Successfully tweeted: {tweet_text}")
    except tweepy.TweepError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    tweet_word()
