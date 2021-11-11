from task_1 import movies
name=movies()
import json
def ten_yers_group_movie(movies ):
    years=[]
    for i in movies:
        year=i["Year"]%10
        four_no_year=i["Year"]-year
        if four_no_year not in years:
            years.append(four_no_year)
    years.sort()
    four_no_year={}
    for i in years:
        movielist=[]
        for x in movies:
            if x["Year"]>=i and x["Year"]<=i+10:
                movielist.append(x)
                four_no_year[i]=movielist
                with open("ten_year_group.json","w")as file:
                    json.dump(four_no_year,file,indent=3)
    return  four_no_year                   
ten_yers_group_movie(name)    


