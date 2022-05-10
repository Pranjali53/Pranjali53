import requests
import json
def request():
    req = "https://saral.navgurukul.org/api/courses"
    a = requests.get(req)
    b = a.text
    with open("course.json","w") as file:
        dic=json.loads(b) 
        json.dump(dic,file,indent=4)
    with open("course.json","r") as file:
        file2=json.load(file)
    n=1
    id=[]
    for i in file2["availableCourses"]:
        print(n,i["name"],":-",i["id"])
        id.append(i["id"])
        n+=1
    course_id=int(input("enter number for course id:-"))
    req2=("http://saral.navgurukul.org/api/courses/"+str(id[course_id])+"/exercises")
    a2=requests.get(req2)
    course_detail=a2.json()
    n2=1
    slug=[]
    for name in course_detail["data"]:
        print(n2,"-",name["name"])
        slug.append(name["slug"])
        n2+=1
        slug_input=int(input("enter number for slug input:-"))
        slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug[slug_input])
        slug_json=slug_api.json()
        print(slug_json["content"])
        print("up':-for previous content")
        print("next':-for next content")
        print("same':-for same content")
        for s in range(4):
            step=input("enter for content:")
            if step=="next":
                slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug[slug_input+1]      )
                up_json=slug_api.json()
                print(slug_input+1,up_json["content"])
            elif step=="up":
                slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug[slug_input-1])
                next_json=slug_api.json()
                print(slug_input-1,next_json["content"])
            elif step=="same":
                slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug"+slug[slug_input])
                same_json=slug_api.json()
                print(slug_input,same_json["content"])
request()