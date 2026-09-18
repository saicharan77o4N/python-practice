"""
student={
    "Name":"Michael",
    "Age": 20,
    "Branch":"SE"
}
for key in student:
    print(key)
print("\n")
for val in student.values():
    print(val)
print("\n")
for key,val in student.items():
    print(key,":",val)

videos=[
    {"title":"Python Full Course","duration":10,"views":2000000},
    {"title":"Python OOP","duration":3,"views":800000},
    {"title":"Python Projects","duration":5,"views":500000},
    {"title":"Python basics","duration":2,"views":900000}
]
print("\n")
m_views=0
views=0
m_viewed=""
lst_views=videos[0]["views"]
l_viewed=""
longest=""
max_length=0
for video in videos:
    views+=video["views"]
    if video["views"]>m_views:
        m_views=video["views"]
        m_viewed=video["title"]
    if video["views"]<lst_views:
        lst_views=video["views"]
        l_viewed=video["title"]
    if video["duration"]>max_length:
        max_length=video["duration"]
        longest=video["title"]
print("Least viewd video:")
print(l_viewed,"-",lst_views/1000000,"M views")
print("Most viewed video:")
print(m_viewed,"-",m_views/1000000,"M views")
print("Longest video:",longest,"-",max_length)
print("\n")
for video in videos:
    if video["duration"]<=3:
        print(video["title"],":short")
    elif video["duration"]<=5:
        print(video["title"],":medium")
    else:
        print(video["title"],":long")

print("\n")
count=0
for video in videos:
    if video["duration"]<=5 and video["views"]>600000:
        count+=1
        print(video["title"],"-",(video["views"]/1000000),"M views")
print("Count=",count)
print("Total views:",views)
print("average views:",views/len(videos))
print("\n")
def print_video(video):
    print(video["title"],"-",video["duration"],"-",video["views"])
print_video(videos[1])
def is_popular(video):
    if video["views"]>600000:
        return True
    else: return False
print("\n")
print("Popular videos:")
for video in videos:
    if is_popular(video):
        print(video["title"],"-",video["views"]/1000000,"M views")
print("\n")
def analyze_video(video):
    print("Title:",video["title"])
    print("Duration:",video["duration"],)
    print("Views:",video["views"]/1000000,"M views")
    if is_popular(video):
        print("Popular:YES")
    else:
        print("Popular:NO")
titles=[]
def get_titles(videos):
    for video in videos:
        titles.append(video["title"])
for video in videos:
    analyze_video(video)
get_titles(videos)
print("\nTitles:",titles)
def add_catgry(videos):
    for video in videos:
        video["category"]="Programming"
add_catgry(videos)
for video in videos:
    print(video)

"""

videos1 = [
    {"title": "Python Full Course", "duration": 10, "views": 2000000, "category": "Programming"},
    {"title": "Python OOP", "duration": 3, "views": 800000, "category": "Programming"},
    {"title": "Python Projects", "duration": 5, "views": 500000, "category": "Projects"},
    {"title": "Python Basics", "duration": 2, "views": 900000, "category": "Programming"},
    {"title": "Python APIs", "duration": 4, "views": 700000, "category": "Backend"},
    {"title": "Python Advanced", "duration": 8, "views": 300000, "category": "Programming"}
]

def get_programming_vids(videos):
    for video in videos:
        if video["category"] == "Programming":
            print(video["title"])
get_programming_vids(videos1)

cats=set()
for video in videos1:
    if video["category"] not in cats:
        cats.add(video["category"])
print("No. of categories:",len(cats))
print(cats)

count_cats={
    "Programming":0,
    "Backend":0,
    "Projects":0
}
for video in videos1:
    if video["category"] in count_cats:
        count_cats[video["category"]]+=1

for key,value in count_cats.items():
    print(key,":",value)

view_by_cat={
    "Programming":0,
    "Backend":0,
    "Projects":0
}
for video in videos1:
    if video["category"] in view_by_cat:
        view_by_cat[video["category"]]+=video["views"]
print("\n")
for key,value in view_by_cat.items():
    print(key,":",value)


def m_viewed_in_cat(videos,catgry):
    most_viewed=None
    for video in videos:
        if video["category"]==catgry:
            if most_viewed is None or video["views"]>most_viewed["views"]:
                most_viewed=video
    return most_viewed
res=m_viewed_in_cat(videos1,"Programming")
print("Most viewed video in PROGRAMMING:")
print(res["title"],"-",res["views"]/1000000,"M views")
print("\n")
relevant=[]
def find_rel(videos,keyword):
    for video in videos:
        if keyword.lower() in video["title"].lower():
            relevant.append(video["title"])
find_rel(videos1,"PyTHon")
print("\n",relevant)

def smart_search(videos,keyword):
    for video in videos:
        if keyword.lower() in video["title"].lower() or keyword.lower() in video["category"].lower():
            return video["title"]
res_title=smart_search(videos1,"BackeNd")
print("\n",res_title)

avg_views=(sum(video["views"] for video in videos1))/len(videos1)
print(avg_views)

def get_vids(videos):
    for video in videos:
        if video["views"]>avg_views:
            print(video["title"])
get_vids(videos1)
def most_viewed(videos):
    m_viewed=None
    for video in videos:
        if m_viewed is None or video["views"]>m_viewed["views"]:
            m_viewed=video
    return m_viewed

def shortest_vid(videos):
    shortest=None
    for video in videos:
        if shortest is None or video["duration"]<shortest["duration"]:
            shortest=video
    return shortest

def vid_report(videos):
    print("Total videos:",len(videos1))
    print("Total views:",sum(video["views"] for video in videos1))
    print("Average views:",avg_views)
    print("Most viewed:",most_viewed(videos)["title"],"-",most_viewed(videos)["views"]/1000000,"M views")
    print("Shortest video:",shortest_vid(videos1)["title"],"-",shortest_vid(videos1)["duration"],"hours")
    cats=set()
    for video in videos:
        cats.add(video["category"])
    print("Categories:",cats)

vid_report(videos1)