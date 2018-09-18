import requests
import re
import urlparse
from BeautifulSoup import BeautifulSoup

class Scanner:
    def __init__(self,url,ignore_links):
        self.target_url=url
        self.target_links=[]
        self.session=requests.Session()
        self.links_to_ignore=ignore_links

    def extract_links_from(self,url):
        response=self.session.get(url)
        return(re.findall('(?:href=")(.*?)"',response.content))           #regex to find the links in page

    def crawl(self,url=None):
        if url==None:
            url=self.target_url
        href_links=self.extract_links_from(url)
        for link in href_links:
            link=urlparse.urljoin(url,link)
            if '#' in link:
                link=link.split("#")[0]                                   #dont use links with # because they load the same page

            if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore:     #only unique links
                self.target_links.append(link)
                print(link)
                self.crawl(link)

    def extract_forms(self,url):
        response=self.session.get(url)
        parsed_html=BeautifulSoup(response.content)
        return parsed_html.findAll("form")

    def submit_form(self,form,value,url):
        action=form.get("action")         #get method returns the value of attribute
        method=form.get("method")
        post_url=urlparse.urljoin(self.target_url,action)          #to join relative and target_url
        post_data={}
        input_list=form.findAll("input")
        for input in input_list:
            input_name=input.get("name")
            input_type=input.get("type")
            input_value=input.get("value")
            if input_type=="text":
                input_value="test"
            post_data[input_name]=input_value
        if method=="post":
            return requests.post(post_url,data=post_data)
        return self.session.get(post_url,params=post_data)
    
    def run_scanner(self):
        for link in self.target_links:
            forms=self.extract_forms(link)
            for form in forms:
                print("[+] Testing form in "+link)
            if "=" in link:
                print("[+] Testing "+link)
