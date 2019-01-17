# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 21:30:55 2019

@author: Kritesh
"""

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "swine flu vaccine"
  
for j in search(query, tld="co.in", num=50, stop=1, pause=2): 
    print(j)
