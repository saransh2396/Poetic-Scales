# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 23:09:10 2023

@author: saransh.s
"""

stats=['stats_squads_standard_for','stats_squads_keeper_for','stats_squads_keeper_adv_for',
       'stats_squads_shooting_for','stats_squads_passing_for','stats_squads_passing_types_for',
       'stats_squads_gca_for','stats_squads_defense_for','stats_squads_possession_for',
       'stats_squads_misc_for']


import os
import pandas as pd
pd.set_option("display.max_columns", None)
from bs4 import BeautifulSoup
#from urllib.request import urlopen
import requests

scrape_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
 
os.chdir(r'D:\Personal\Football Analysis\Event Data\Team Analysis')

try:
    os.mkdir("EPL_23_24")
except OSError:
    print("Folder Results Already Exists")

os.chdir(r"D:\Personal\Football Analysis\Event Data\Team Analysis\EPL_23_24")



try:
    os.mkdir("data")
except OSError:
    print("Folder Results Already Exists")
    
os.chdir(r"D:\Personal\Football Analysis\Event Data\Team Analysis\EPL_23_24\data")

def get_df(url):
    content = requests.get(url)
    html_content = content.content
    soup=BeautifulSoup(html_content,'html.parser')
    for i in stats:
        table = soup.find('table',id = i)
        df = pd.read_html(str(table))
        data = df[0]
        data.columns = data.columns.droplevel()
        df=data.apply(pd.to_numeric, errors="ignore")
        file_name = str(i) + '.csv'
        df.to_csv(file_name)
        
get_df(scrape_url)  