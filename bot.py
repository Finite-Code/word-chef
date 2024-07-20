import os
import requests
import json

# Set up Twitter API credentials
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

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

    url = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "text": tweet_text
    })

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 201:
        print(f"Successfully tweeted: {tweet_text}")
    else:
        print(f"Error occurred: {response.status_code} - {response.text}")

if __name__ == "__main__":
    tweet_word()
