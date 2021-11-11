     
from task_1 import movies
name=movies()
print(name)
import json
def group_of_same_year(movie):
    years=[]
    for i in movie:
        year=i["Year"]
        # print(i)
        if year not in years:
            years.append(year)
    # print(years)
    dict_fMovies={i:[]for i in years}
    # print(dict_fMovies)  
    for i in movie:
        year=i["Year"]
        for x in dict_fMovies:
            if (x)==(year):
                dict_fMovies[x].append(i)
        with open("grup of movie.json","w")as file:
            json.dump(dict_fMovies,file,indent=3)
    return(dict_fMovies)
group_of_same_year(name)

                                                                






































  
