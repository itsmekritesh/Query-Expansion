# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 21:30:55 2019

@author: Kritesh
"""


subscription_key = 'create your api key'
assert subscription_key
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
search_term = "swine flu"

import requests

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML","count":"25"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()
#print(response)
#print(search_results)
for v in search_results["webPages"]["value"]:
    print(v["url"])
    print(" ")
