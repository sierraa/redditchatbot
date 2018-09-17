import requests
import requests.auth
import json
from reddit_auth import RedditAuthentication
from reddit_search import RedditSearch

if __name__ == '__main__':
    # TODO: read from input
    auth = RedditAuthentication('src/credentials.json')
    access_token = auth.get_access_token()
    user_agent = auth.get_user_agent()
    search = RedditSearch(access_token, user_agent)
    result = search.search_for_subreddit("fitness")
    print(result.json())
