import requests
import os
import pandas as pd
from bs4 import BeautifulSoup

url=["https://www.shiksha.com/online-courses/articles/constructors-in-python-definition-types-and-rules/#:~:text=Constructors%20in%20Python%20is%20a,value%20to%20the%20object's%20members."]

def extract(url):
    webpage=requests.get(url)
    web=webpage.content
    soup=BeautifulSoup(web,"html.parser")
    value=soup.find("strong",{"class":"_03a2"})
    m=value.text
    print(m)

result=[extract(url) for url in url1]
