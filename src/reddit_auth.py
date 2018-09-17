import json
import requests

class RedditAuthentication(object):

    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        self.credentials = self.get_credentials()
        self.user_agent = self.credentials['user_agent']
        self.client_secret = self.credentials['client_secret']
        self.client_id = self.credentials['client_id']
        self.username = self.credentials['username']
        self.password = self.credentials['password']
        self.access_token_url = "https://www.reddit.com/api/v1/access_token"

    def get_credentials(self):
        with open(self.credentials_file) as f:
            return json.load(f)

    def get_access_token(self):
        client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        post_data = {"grant_type": "password", "username": self.username, "password": self.password}
        headers = {"User-Agent": self.user_agent}
        response = requests.post(self.access_token_url, auth=client_auth, data=post_data, headers=headers)
        return response.json()['access_token']

    def get_user_agent(self):
        return self.user_agent
