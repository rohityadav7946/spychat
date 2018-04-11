from datetime import datetime
import csv
from termcolor import colored



# creating class
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name= name
        self.salutation = salutation
        self.age= age
        self.rating= rating
        self.is_online=True
        self.chats=[]
        self.current_status_message= None


class ChatMessage:
    def __init__(self, spy_name, friend_name, time, message):
        self.spy_name = spy_name
        self.friend_name = friend_name
        self.time = datetime.now()
        self.message = message


# define spy_name, age, rating)
spy_1=Spy('Rohit','Mr',20,4.4)

# lists of friends
friends=[]
# list of chats
chats = []