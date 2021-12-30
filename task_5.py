


from task_1 import screpped
import json
import requests
from bs4 import BeautifulSoup
import pprint
# from task_4 import one_movie_detaile
# num=movies()
# print(num)
def movie_list(movies):
    i=0
    years=[]
    while i<len(movies):
        # print(i)
        # year=movie[i]["url"]
        url=movies[i]["Movie URL"]
        # print(url)
        # i=i+1
        # a=one_movie_detaile(url)
        # for a in url: 
        # # k=url
        p=requests.get(url)
        # # print(a)
        soup=BeautifulSoup(p.text,"html.parser")
        # print(soup)
        movie_detail=soup.find("ul",class_="content-meta info")
        find_movie=movie_detail.find_all("li",class_="meta-row clearfix")
        # print(find_movie)
        deta={}
        for k in find_movie:
            deta[" ".join((k.find("div",class_="meta-label subtle").text).split())]=" ".join((k.find("div",class_="meta-value").text).split())
        deta["name"]=movies[i]["Movie Name"]
        years.append(deta)
        i=i+1
    with open("movie.json","w")as f:
        json.dump(years,f,indent=4)
    return years
pprint.pprint(movie_list(screpped))
               
