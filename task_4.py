from bs4 import BeautifulSoup
import requests
# import os.path
import json
from task_1 import movies
# import pprint
def detail(text):
    return "".join(text.split())
def one_movie_detaile(url_for_movies):
    detail_dic={}
    all_detail=requests.get(url_for_movies)
    soup=BeautifulSoup(all_detail.text,"html.parser")
    container=soup.find("ul",class_="content-meta info")
    all=container.find_all("li",class_="meta-row clearfix")
    for i in range(len(all)):
        if i==1:
            detail_dic[detail((all[i].find("div",class_="meta-label subtle")).text)]=detail((all)[i].find("div",class_="meta-value genre").text)
        else:
            detail_dic[detail((all[i].find("div",class_="meta-label subtle")).text)]=detail((all)[i].find("div",class_="meta-value").text)
    with open("one_movie detail.json","w")as f:
        json .dump(detail_dic,f,indent=4)
    print(detail_dic)
one_movie_detaile("https://www.rottentomatoes.com/m/black_panther_2018")            
                    
    