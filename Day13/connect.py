from urllib import request
import requests
import pprint
import pandas as pd
from _kluce import *

# HTTP requests methods
"""
GET -> grab data
POST ->add/update data

PATCH
PUT
DELETE
"""


# what's our endpoint (or a url)

"""
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=369c6e9ab2910057cd7e27523f302be8
"""
movie_id = 551
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
#print (endpoint)

#r = requests.get(endpoint)
    # niekedy pasnut data do r = requests.get(endpoint, 
    # data={"api_key": api_key})
    #alebo
    # json={"api_key": api_key})
#print (r.status_code)
#print (r.text)


# Using V4
movie_id = 552
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
}
#print (endpoint)

#r = requests.get(endpoint, headers = headers)
    # niekedy pasnut data do r = requests.get(endpoint, 
    # data={"api_key": api_key})
    #alebo
    # json={"api_key": api_key})
#print (r.status_code)
#print (r.text)

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
#print (endpoint)
r = requests.get(endpoint)
#pprint.pprint(r.json())
if r.status_code in range(200,299):
    data = r.json()
    results = data['results']
    if len(results)>0:
        #print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            #print(result['title'], _id)
            movie_ids.add(_id)
        #print(list(movie_ids))

output = 'movies.csv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200,299):
        data = r.json()
        movie_data.append(data)


df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)
    
    
    
    
    
# what is http method that we need