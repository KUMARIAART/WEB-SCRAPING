from bs4 import BeautifulSoup
import json
import requests
from task05 import movie_list

list=[]
def analyse_movies_genre(movie_genre):
    for i in movie_genre:
        genre=i["Genre"]
        list.append(genre)
    # print(list)
    Genre=[]
    for i in list:
        for j in i:
            Genre.append(j)

    dict_Genre={}
    for i in Genre:
        count=0
        for j in Genre:
            if i==j:
                count+=1
        dict_Genre[i]=count
    
    file=open("task11.json","w")
    json.dump(dict_Genre,file,indent=4)
    return dict_Genre


analyse_movies_genre(movie_list)