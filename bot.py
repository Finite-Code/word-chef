import os
import tweepy
import requests

# Set up Twitter API credentials
auth = tweepy.OAuthHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

# Get a random word and its details
def get_random_word():
    response = requests.get("https://api.wordnik.com/v4/words.json/randomWord", params={"api_key": os.getenv("WORDNIK_API_KEY")})
    word = response.json()["word"]
    return word

def get_word_details(word):
    response = requests.get(f"https://api.wordnik.com/v4/word.json/{word}/definitions", params={"api_key": os.getenv("WORDNIK_API_KEY")})
    definitions = response.json()
    return definitions[0]['text'] if definitions else "No definition found."

def tweet_word():
    word = get_random_word()
    definition = get_word_details(word)
    tweet_text = f"Word: {word}\nMeaning: {definition}\nExample Usage: [Example usage here]"
    api.update_status(tweet_text)

if __name__ == "__main__":
    tweet_word()
