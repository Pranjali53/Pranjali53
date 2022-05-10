import json
from Task1 import scrape_top_list
from Task4 import movies_detailes

Top_movies=scrape_top_list()
top_movies=Top_movies[:100]
def get_movie_detailes():
    movies_list=[]
    for i in Top_movies:
        for j in i:
            if j=="URL":
                movies_list.append(movies_detailes(i[j]))
                
    with open("Task5.json", 'w+') as Task5_file:
        json.dump(movies_list, Task5_file, indent=6)
    return movies_list     
     
get_movie_detailes()