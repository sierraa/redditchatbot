import requests
import requests.auth
import json
from reddit_auth import RedditAuthentication
from reddit_search import RedditSearch

def get_subreddit_name(result):
    return result.json()['data']['children'][0]['data']['display_name_prefixed']

if __name__ == '__main__':
    auth = RedditAuthentication('src/credentials.json')
    print("Hi! I'm a reddit chatbot. Enter q at any time to quit.")
    while True:
        topic = input("What would you like to learn about? ")
        if topic == "q":
            break
        access_token = auth.get_access_token()
        user_agent = auth.get_user_agent()
        search = RedditSearch(access_token, user_agent)
        result = search.search_for_subreddit(topic)
        subreddit_name = get_subreddit_name(result)
        question = input("What question do you have? ")
        result = search.search_subreddit(subreddit_name, question)
        print(result.json())
