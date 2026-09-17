list=["Java","Python","C++","Javascript","SQL"]
print(list)
print(list[3])
list.append("Spring Boot")
list.remove("C++")
list.pop(1)
print(list)
list.insert(1,"Python")
print(list)

for course in list:
    print(course)
durations=[10,3,2,6,1]
print(durations)
print("\n\n")
print(max(durations))
print(min(durations))
print("Total duration: ",sum(durations))
average=(sum(durations)/len(durations))
print("Average runtime:",average)
for i in range(3):
    print(list[i])

videos=[
    {"title":"Java Full course","duration":10},
    {"title":"Java OOP","duration":3},
    {"title":"Java Collections","duration":2},
    {"title":"Spring Boot","duration":6}
]
print("\n\n")
for video in videos:
    print(video["title"],"-",video["duration"]," hours")

student={
    "Name":"Micheal",
    "Age":20,
    "College":"MIT"
}
print(student["Name"])
student["Grade"]="O"
print(student)
student["Age"]=21
print(student)

video={
    "title":"Python Full Course",
    "duration":10,
    "views":1500000
}
print("Title: ",video["title"])
print("Duration: ",video["duration"])
print("Views: ",video["views"])