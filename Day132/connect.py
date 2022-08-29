import pprint
from urllib import request
import requests
import pandas as pd

from _kluce import *

movie_id = 551
api_version = 3

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "Matrix"
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
            #print(result['original_title'], _id)
            movie_ids.add(_id)
        #print(list(movie_ids))

output = 'movies.csv'
movie_data = []
# Tu vytahujem info ku vsetkým najdeným filmom
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
print(df.head(6))
df.to_csv(output, index=False)

# what is http method that we need