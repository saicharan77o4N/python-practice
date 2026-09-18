"""
#1
class Video:
    def display(self):
        print(self.title)
        print(self.views)
        print(self.category)
vid=Video()
vid.title="Python Programming"
vid.views=2000000
vid.category="Programming"
vid.display()
#2
class Video:
    def __init__(self,title,duration,views,category):
        self.title=title
        self.duration=duration
        self.views=views
        self.category=category
    def inc_views(self,amt):
        self.views+=amt
    def display(self):
        print(self.title,"-",self.duration,"-",self.views)
vid1=Video("Python OOP",5,2000000,"Programming")
vid2=Video("Python APIs",3,500000,"Backend")
vid1.display()
vid2.display()
vid1.inc_views(100000)
vid1.display()
print(vid1.category)
"""
"""
#3
class Video:
    def __init__(self,title,views):
        self.__title=title
        self.views=views
       
    def play(self):
        print("playing video")
        #print(self.__title)

class EduVideo(Video):
    def __init__(self,title,views,subject):
        super().__init__(title,views)
        self.subject=subject
    def display(self):
        print(self.title,"-",self.views,"-",self.subject)
    def play(self):
        super().play()
        print("Playing educational video")
class MusicVideo(Video):
    def __init__(self,title,views,artist):
        super().__init__(title,views)
        self.artist=artist
    def play(self):
        print("Playing music video")
    def display(self):
        print(self.title,"-",self.artist,"-",self.views/1000000,"M views")
edv=EduVideo("Python OOP",800000,"Programming")
edv1=EduVideo("FastAPI",500000,"Coding")
mvid=MusicVideo("I lied to you",20000000,"Miles Caton")
edv1.play()
mvid.play()
mvid.display()
vid=Video("PyTorch",200000)
vid.play()

#4
class BankAcc:
    def __init__(self,balance):
        self.__balance=balance
    @property
    def bal(self):
        return self.__balance
acc=BankAcc(10000)
print(acc.bal)

#5 Encapsulation
class Video:

    def __init__(self, views):
        self.__views = views

    def increase_views(self, amount):
        if amount > 0:
            self.__views += amount

    def get_views(self):
        return self.__views
    @property
    def views(self):
        return self.__views
    @views.setter
    def views(self,amount):
        if amount>=0:
            self.__views=amount
obj=Video(100000)
obj.increase_views(15000)
print(obj.get_views())
print(obj.views)
obj.views=200000
print(obj.views)
"""

"""
#6 Abstraction
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("paying using upi")
class Card(Payment):
    def pay(self):
        print("paying using card")
upi=UPI()
card=Card()
upi.pay()
card.pay()

class ContentFilter(ABC):
    @abstractmethod
    def filter(self,content):
        pass
class KeywordFilter(ContentFilter):
    def filter(self,content):
        print(content)
kf=KeywordFilter()
kf.filter("Filtering using keywords")

#7
class Content(ABC):
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def get_info(self):
        pass
    @abstractmethod
    def inc_views(self):
        pass
class Video(Content):
    def __init__(self,title,views,duration):
        self.title=title
        self.__views=views
        self.duration=duration
    def play(self):
        print("Playing a video")
    def get_info(self):
        print("Title:",self.title)
        print("Duration:",self.duration/3600)
        print("Views:",self.__views)
    def inc_views(self,amt):
        self.__views+=amt
    def get_views(self):
         return self.__views
    @property
    def views(self):
         return self.__views
    @views.setter
    def views(self,amt):
         if amt>=0:
              self.__views=amt
class ShortVideo(Content):
    def __init__(self,title,views,duration):
            self.title=title
            self.views=views
            self.duration=duration
    def play(self):
        print("playing a short")
    def get_info(self):
            print("Title:",self.title)
            print("Duration:",self.duration)
            print("Views:",self.views)
    def inc_views(self,amt):
            self.views+=amt
class Metadata(Video):
    def __init__(self,title,views,duration,category):
        super().__init__(title,views,duration)
        self.category=category
        self.obj=ShortVideo(self.title,self.views,self.duration)
    def get_info(self):
         super().get_info()
         print("Category:",self.category)
vid=Video("Python Data Structers",15000000,15*60*60)
s_vid=ShortVideo("Mobius Strip",30000000,47)
data=Metadata("Pandas",2000000,2*60*60,"Python Libraries")
print("Class Video")
vid.get_info()
print("\nVIEWS:",vid.views)
vid.views=500000
print("\nSet views:",vid.views)
vid.inc_views(100000)
print("\n")
vid.get_info()
print("Composition:")
data.obj.play()
"""