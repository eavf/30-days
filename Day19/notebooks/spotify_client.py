#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import requests
import base64
from _kluce import client_id, client_secret
from urllib.parse import urlencode


# In[27]:


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
        
    def get_client_credentials(self):
        """
        Returns a base64encoded string 
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_id == None or client_secret ==None:
            raise Exception("You must set client_id a client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
    
    def get_token_header(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }
    
    def get_token_data(self):
        return {
            "grant_type": 'client_credentials'
        }
    
    def perform_auth(self):
        token_url = self.token_url
        token_data = self. get_token_data()
        token_header = self.get_token_header()
        r = requests.post(token_url, data=token_data, headers=token_header)
        if r.status_code not in range(200, 299):
            raise Exception("Authentification failed!")
            #return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expire_in = data['expires_in']         # seconds
        expires = now + datetime.timedelta(seconds=expire_in)
        self.access_token = access_token
        self.access_token_expires = expires
        access_token_did_expire = expires < now
        return True
    
    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires<now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token()
        return token
    
    def get_resources_headers(self):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        return headers
    
    def get_resources(self, lookup_id, resource_type='albums', version = 'v1'):
        base_url = "https://api.spotify.com/v1/"
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        headers = self.get_resources_headers()
        r = requests.get(endpoint, headers = headers)
        if r.status_code not in range (200,299):
            return {}
        return r.json()
    
    def get_album(self, _id):
        return self.get_resources(_id, resource_type = 'albums', version = 'v1')
    
    def get_artist(self, _id):
        return self.get_resources(_id, resource_type = 'artists', version = 'v1')
    
    def base_search(self, query_params):
        headers = self.get_resources_headers()
        endpoint = "https://api.spotify.com/v1/search"
        lookup_url = f"{endpoint}?{query_params}"
        r = requests.get(lookup_url, headers = headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()
    
    def search(self, query=None, operator=None, operator_query=None, search_type = 'artist'):
        if query == None :
            raise Exception ("A query is required!")
        if isinstance (query, dict):
            # haluz, vylistuje páry kluc hodnota a spojí ich medzerou
            query = " ".join([f"{k}:{v}" for k,v in query.items()])
            #query = "%20".join([f"{k}:{v}" for k,v in query.items()])
        if operator != None and operator_query != None:
            if operator.lower() == "or" or operator.lower() == "not":
                operator = operator.upper()
                if isinstance (operator_query, str):
                    query = f"{query} {operator} {operator_query}"
        query_params = urlencode({"q": query, "type": search_type.lower()})
        print (query_params)
        return self.base_search(query_params)

