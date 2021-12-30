import  json
def movie_language():
    language=open("movie.json","r")
    h=json.load(language)
    # print(liist)
    list=[]
    dict={}
    for i in h:
        if i["Original Language:"]not in list:
            list.append(i["Original Language:"])
            # print(li)
    dic={}
            # li2=[]
    for j in list:
        i=0
        c=0
        while i<len(h):
            if j==h[i]["Original Language:"]:
                c=c+1
            i=i+1
        dict.update({j:c})
    list.append(dic)
    with open("movi_lang.json","w")as file:
        json.dump(dict,file,indent=4)  
movie_language()                         
    