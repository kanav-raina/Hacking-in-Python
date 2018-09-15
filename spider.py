#!/usr/bin/env python

import requests
import re
import urlparse

target_url="http://www.dmoz.org.in/"                                  #you can enter any site
target_links=list()
def extract_links_from(url):
     response=requests.get(target_url)
     return(re.findall('(?:href=")(.*?)"',response.content))           #regex to find the links in page

def crawl(url):
    href_links=extract_links_from(url)
    for link in href_links:
        link=urlparse.urljoin(url,link)
        if '#' in link:
             link=link.split("#")[0]                                   #dont use links with # because they load the same page

        if target_url in link and link not in target_links:                   #only unique links
             target_links.append(link)
             print(link)
             crawl(link)


crawl(target_url)
#urlparse is used to join relative links which does not contain target_url
#print(href_links)
#print(response.content)
