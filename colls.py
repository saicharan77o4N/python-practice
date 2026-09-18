"""
#1 tuple
video=("Python programming",6,2000000)
title,duration,views=video
print(title,"-",duration,"-",views)
print(video[1])

#2 Sets
categories={"programming","Project","entertainment","sport","education"}
print(categories)
categories.add("news")
print(categories)
categories.remove("Project")
print(categories)
categories.discard("entertainment")
print(categories)
#categories.remove("element")
categories.discard("element")
print("news" in categories)
print("element" not in categories)
print("element" in categories)

#3 List comprehension
videos = [
    {"title": "Python Course", "views": 2000000},
    {"title": "Java Course", "views": 500000},
    {"title": "Python OOP", "views": 800000}
]
popular=[video["title"] for video in videos if video["views"]>700000]
print(popular)
titles=[video["title"] for video in videos]
print("Titles:",titles)
python_videos=[
    video["title"] for video in videos
    if "python" in video["title"].lower()
]
print("Python videos:",python_videos)

#4 Dictionary Comprehension
numbers = [1, 2, 3, 4]
squares={number:number*number for number in numbers}
print(squares)

#5 zip()
titles = ["Python", "Java", "C++"]
views = [2000000, 1500000, 900000]
videos=[]
video={}
for title,view in zip(titles,views):
    video["title"]=title
    video["views"]=view
    videos.append(video)
print(videos[0])

#6 enumerate()
for index,val in enumerate(views,start=2):
    print(index,":",val)

#7 sorted()
views = [2000000, 1500000, 900000]
views=sorted(views)
print(views)

videos = [
    {"title": "Python", "views": 2000000},
    {"title": "Java", "views": 500000},
    {"title": "AI", "views": 3000000}
]
videos=sorted(videos,
key=lambda video:video["views"]
              )
print(videos)

#8
videos = [
    {"title": "Python Full Course", "views": 2000000},
    {"title": "Java OOP", "views": 800000},
    {"title": "Python Projects", "views": 1500000},
    {"title": "AI Introduction", "views": 3000000},
    {"title": "Python APIs", "views": 600000}
]
results=[]
for video in videos:
    if "python" in video["title"].lower():
        results.append(video)
results=sorted(results,key=lambda video:video["views"],reverse=True)
for index,vid in enumerate(results,start=1):
    print(index,vid)
"""