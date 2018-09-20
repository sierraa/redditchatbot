import requests
import urllib

class RedditSearch(object):

    def __init__(self, access_token, user_agent):
        self.headers = {'Authorization': 'bearer ' + access_token, 'User-Agent': user_agent}
        self.url = "https://oauth.reddit.com"

    def search_for_subreddit(self, keyword):
        endpoint = self.url + "/subreddits/search.json?" + urllib.parse.urlencode({'q': keyword})
        return requests.get(endpoint, headers=self.headers)

    def search_subreddit(self, subreddit, question):
        endpoint = self.url + "/" + subreddit + "/search.json?" + urllib.parse.urlencode({'q': question})
        return requests.get(endpoint, headers=self.headers)

    def query_comments(self, subreddit, post):
        endpoint = self.url + "/r/" + subreddit + "/comments/" + post
        return requests.get(endpoint, headers=self.headers)
