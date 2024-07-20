import os
import tweepy
import requests

# Set up Twitter API credentials
auth = tweepy.OAuthHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

# Get a random word and its details
def get_random_word():
    # Example endpoint; you might need a different method for random words
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
    api.update_status(tweet_text)

if __name__ == "__main__":
    tweet_word()
