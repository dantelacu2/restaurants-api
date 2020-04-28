import urllib
import requests
import json
import os

with open('new_output.json', mode='w', encoding='utf-8') as f:
    json.dump([], f)

for i in range(0, 20):
    with open('new_output.json', mode='w', encoding='utf-8') as feedsjson:
        entry = {'name': 2, 'url': 2}
        feeds = json.load(feedsjson)
        json.dump(feeds, feedsjson)



# TOKEN = 'f968j45AW9N93xfVurKyQLePSHDrzOJoc1iGKLRYu4Nw2lUKkcN6ByJi6osRt9rV_Rl9dsxX8XJQXXnOOH18ELAc3KmxCVWxLY_vgFQEawUA13JC9kUVMZhMepanXnYx'
# headers = {'Authorization': 'bearer %s' % TOKEN}
#
#
#     with requests.Session() as s:
#         s.headers.update(headers)
#         resp = s.get('https://api.yelp.com/v3/businesses/search?term=food&location=Novato+California&limit=50&offset=350')
#         print(resp.json())
# # r = requests.get('https://api.yelp.com/v3/businesses/search?term=food&location=Novato+California&limit=50&offset=350',
# #                 headers={'Authorization': 'TOK:f968j45AW9N93xfVurKyQLePSHDrzOJoc1iGKLRYu4Nw2lUKkcN6ByJi6osRt9rV_Rl9dsxX8XJQXXnOOH18ELAc3KmxCVWxLY_vgFQEawUA13JC9kUVMZhMepanXnYx'})
