# API - ThemovieDB importy
import pprint
import requests

# Scrape - Box Office Mojo importy
from ast import parse
from cgitb import html
import datetime
import requests
from requests_html import HTML
import pandas as pd
import re

# Environement premenne
from _kluce import *


class Movie():
    najdi_str = None
    api_version = None
    api_base_url = None
    endpoint_path = None
    movie_data = None                       # List s údajmi z The Movie DB
    mov_ext_data = None                     # List s údajmi z Box Office Mojo
    endpoint = None
    
    # premenne scrapying
    now = None
    url = None
    url_bom = None

    has_html = False
    test_send = False
    
    def __init__(self, api_version = None, api_base_url = None, endpoint_path = None, najdi_str = None, movie_data = None, url = None, url_bom = None, mov_ext_data = None):
        if api_version == None:
            self.api_version = 3
        if api_base_url == None:
            self.api_base_url = f"https://api.themoviedb.org/{self.api_version}"
        if endpoint_path == None:
            self.endpoint_path = f"/search/movie"
        if najdi_str == None:
            raise Exception("You must set a search string")
        else:
            self.najdi_str = najdi_str
            self.endpoint = f"{self.api_base_url}{self.endpoint_path}?api_key={api_key}&query={najdi_str}"
        self.movie_data = []
        self.mov_ext_data = []
        self.now = datetime.datetime.now()
        self.url = "https://www.boxofficemojo.com/search/?q=matrix"
        self.url_bom = "https://www.boxofficemojo.com"
        #print ("Som v init ")
        #print (self.najdi_str)

    def load_data(self):
        print(self.endpoint)
        r = requests.get(self.endpoint)
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
        
        # Tu vytahujem info ku vsetkým najdeným filmom
        for movie_id in movie_ids:
            endpoint_path = f"/movie/{movie_id}"
            endp = f"{self.api_base_url}{endpoint_path}?api_key={api_key}"
            print("Som v detailoch : " + endp)
            r = requests.get(endp)
            if r.status_code in range(200,299):
                data = r.json()
                self.movie_data.append(data)
        return

    def List_movies(self):
        pprint.pprint(self.movie_data)
        return

    # Scrapy

    def url_to_txt(self, url, file="world.html", save = False):
        r = requests.get(url)
        if r.status_code == 200:
            html_text = r.text
            if save:
                with open("world.html", 'w', encoding='utf-8') as f:
                    f.write(html_text)
            return html_text
        return None

    def find_bom(self):
        html_text = self.url_to_txt(url=self.url)
        #print (html_text)
        if html_text == None:
            return False
        r_html = HTML(html = html_text)
        #print(r_html)
        #print(self.najdi_str)
        links = r_html.find('a', containing=self.najdi_str)
        
        """
        print(links)
        print(type(links))
        print(str(len(links)))
        """
        
        mov_lnk = []
        for tag in links:
            mov_lnk.append(tag.xpath('//a/@href'))      #'//a/@href'
        #print (mov_lnk)
        flat_list = [item for cc in mov_lnk for item in cc]     # spravili sme z toho jednoduchy zoznam
        #print (flat_list)
        return flat_list

    def bom_list(self):
        url_det = self.find_bom()
        for i in url_det:
            url = f"{self.url_bom}{i}/"
            finished = self.parse_and_extract(url)
            if finished:
                print(f"Finished {i}")
                self.mov_ext_data.append(finished)
            else:
                print(f"For {i} there was not datas....")
        print ("Cele zoznam : ", self.mov_ext_data)

    def parse_and_extract(self, url):
        # extrahujem data k jednotlivym filmom
        movie_inf = []
        #print("Parse and extrast")
        #print(url)
        url_sep = re.split("/", url)
        #print("Title is : ", url_sep[4])
        movie_inf.append(url_sep[4])
        html_text = self.url_to_txt(url=url)
        if html_text == None:
            return False
        r_html = HTML(html = html_text)
        div_class = ".mojo-performance-summary-table .money"
        r_div = r_html.find(div_class, first=False)
        print(r_div)
        for tag in r_div:
            #print(tag.text)
            movie_inf.append(tag.text)
        
        div_class = ".mojo-performance-summary-table .a-size-small"
        r_div = r_html.find(div_class, first=False)
        print(r_div)
        for tag in r_div:
            #print(tag.text)
            movie_inf.append(tag.text)
        
        print ("Záznam k filmu je : ", movie_inf)
        return movie_inf