import requests

ngrok_url = 'https://689a-87-197-123-28.eu.ngrok.io'
endpoint = f'{ngrok_url}/box-office-mojo-scraper'

r = requests.post(endpoint, json={})
#print (r.text)
print (r.json()['data'])
