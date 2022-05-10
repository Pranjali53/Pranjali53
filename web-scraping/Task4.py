import requests
import json
from bs4 import BeautifulSoup
movie_url="https://www.rottentomatoes.com/m/toy_story_3"
def movies_detailes(movie_url):
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,"html.parser")
    movie_name=soup.find("h1",class_="scoreboard__title").get_text()
    main_div=soup.find_all("li",class_="meta-row clearfix")
    dict={}
    # l=[]
    dict["movie_name"]=movie_name
    dict["Url"]=movie_url
    # print(dict)
    for i in main_div:
        l=[]
        a=i.text
        b=a.split()
        # print(b)
        if "Rating:" in b:
            dict["Rating"]=b[1]
            # print(dict)
        elif "Language:" in b:
            dict["Language"]=b[-1]
            # print(dict)
        elif "Genre:"in b:
            dict["Genre"]=b[1:]
            # print(dict)
        elif "Director:" in b:
            dict["Director"]=b[1:]          
        elif "Producer:" in b:
            dict["Producer"]=b[1:]
            # print(dict)
        elif "Runtime:" in b:
            run_time=[]
            for j in b:
                if j!="Runtime:":
                    t=j.strip()[:-1]
                    run_time.append(int(t))
                for i in range(len(run_time)):
                    if i==0:
                        min=run_time[i]*60
                    elif i==1:
                        min=run_time[0]*60+run_time[i]
            dict["Runtime"]=min
            # print(dict)
        
    with open ("Task4.json", 'w+') as Task4_file:
        json.dump(dict, Task4_file, indent=6)
        return(dict)
movies_detailes(movie_url)