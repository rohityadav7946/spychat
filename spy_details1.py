from datetime import datetime


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

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


# define spy_name, age, rating)
spy_1=Spy('Rohit','Mr',20,4.4)

# details of existing friends
friend_one=Spy('Deepak','Ms',20,4.5)
friend_two=Spy('Nikhil','Mr',21,4.6)
friend_three=Spy('Krishan','Mr',22,4.7)

# lists of friends
friends=[friend_one,friend_two,friend_three]