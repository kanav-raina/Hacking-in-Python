#!/usr/bin/env python

import requests

#function to get the response status
def request(url):
   try:
      get_response=requests.get("https://"+url)
      return(get_response)
   except requests.exceptions.ConnectionError:
      pass

target_url="google.com"
with open("/home/kira/Desktop/info_gathering/subdomains.txt","r") as wordlist_file:
    for line in wordlist_file:
       word=line.strip()                   #by default every line has a \n character at the end strip() function is used to remove it
       test_url=word+"."+target_url        
       response=request(test_url)
       if response:
           print("Discovered subdomain are -->{0}".format(test_url))
