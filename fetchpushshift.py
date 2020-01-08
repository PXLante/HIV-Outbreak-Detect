import requests
import json

response = requests.get("https://api.pushshift.io/reddit/search/comment/?q=HIV&after=1389140680&before=1420676680&aggs=created_utc&frequency=month&size=0")
print(response.status_code)
print(response.json())

with open('data.txt', 'w') as outfile:
    json.dump(response.json(), outfile)