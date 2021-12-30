import json
def directors_of_movies():
    directors=open("movie.json")
    li=json.load(directors)
    print(li)
    
    li2=[]
    dict={}
    for i in li:
        if (i["Director:"]) not in li2:
            li2.append(i["Director:"])
            # print(li)
    dict={}
            # li2=[]
    for j in li2:
        i=0
        c=0
        while i<len(li):
            if j==li[i]["Director:"]:
                c=c+1
            i=i+1
        dict[j]=c
        # dict.update({j:c})  
    li2.append(dict)         
    with open("Directors.json","w")as f:
        json.dump(li2,f,indent=4) 
directors_of_movies()             