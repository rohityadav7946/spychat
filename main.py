def spy_details_input():
##function which will take details from the new user
    print("Welcome to Spy Chat")
## Welcome Greet to the User##
    spy_name = raw_input("What is your spy_name")
##asking user for the spy name and storing the input in the variable spy_name##
    if len(spy_name) > 0:
    #checking whether spy name is valid or not
        print('Welcome '+spy_name+', good to see you here.')
## greeting the spy with his/her name##
        spy_salutation = raw_input ("What should i call you Mr. or Ms. ?")
##asking the spy for the salutation and storing the input in the variable spy_salutation##
        spy_name = spy_salutation + ' '+ spy_name
##merging the salutation and the spy name to form the complete name and updating the complete spy name##
        print('Alright ' +spy_name+ ' I would like to know a little bit more about you...')
##conversation with the spy##
        spy_age = int(raw_input("What is your age ? "))
        if spy_age < 12 or spy_age >50:
            print("sorry! your age is invalid to be a spy")
        else:
            spy_experience = raw_input("For how many years you are working as a spy ?")
        ##asking spy for his/her experience

            spy_rating= float(raw_input("What is your rating [out of 5]"))
        ##asking spy for his/her experience
            if spy_rating >= 4.5:
                print("Good Ace")
            elif spy_rating < 4.5 and spy_rating >=3.5:
            ##else if statement
                print("You are one of the good ones")
            elif spy_rating <3.5 and spy_rating >=2.5:
                print ("You can do better")
            else:
                print("You can always take help of someone in the office")
            print("Thanks for providing information about yourself")
            print("Authentication complete!\nProud to have you on board \n " +spy_name + " of " + str(spy_age) + " years with a experience of " + spy_experience + " years and a rating of " +str(spy_rating))
    else:
        print("Please enter a valid name")
        spy_details_input()
    ###function will run again if user input invalid name and will ask user to enter details again

##################################################################
from steganography.steganography import Steganography
###importing steganography package
def send_message():
    ###function to send secret message
  friend_choice = select_friend()

  original_image = raw_input("What is the name of the image?")
  output_path = 'output.jpg'
    ##giving the new name to the encided image
  text = raw_input("What do you want to say?")
  Steganography.encode(original_image, output_path, text)
    ##encoding process
  new_chat = {
      "message": text,
      "time": datetime.now(),
      "sent_by_me": True
  }
    ###storing date and time of function

  ##friends[friend_choice]['chats'].append(new_chat)
  print "Your secret message is ready!"

def read_message():
    ##function to read secret message
  sender = select_friend()

  output_path = raw_input("What is the name of the file?")
  secret_text = Steganography.decode(output_path)
    ##decoding process
  print(secret_text)

  new_chat = {
      "message": secret_text,
      "time": datetime.now(),
      "sent_by_me": False
  }

  ##friends[sender]['chats'].append(new_chat)
  print "Your secret message has been saved!"


#####################################################################




friends = []

from datetime import datetime
time= datetime.now()
print(time)

def select_friend():
    ###function to select friend from spy friend list
  item_number = 0

  for friend in friends:
    print ('%d. %s' % (item_number + 1, friend['name']))

    item_number = item_number + 1

  friend_choice = int(input("Choose from your friends(index number)"))
    ##asking spy for friend to whom he/she wants to do chat
  friend_choice_position = friend_choice - 1

  return friend_choice_position




friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []
####empty list
######################################NEW METHOD TO ADD A FREIND################################

def add_friend():
    ###function to add details of friends
    new_friend = {
        'name':"",
        'salutation':'',
        'age':0,
        'rating':0.0
#####dictionary

    }

    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")
    ##new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = int(raw_input("Age?"))
    new_friend['rating'] = float(raw_input("Spy rating?"))
    ####asking spy to enter details of his freiends




    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy_rating:
        friends.append(new_friend)
        ###appending details to list

    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)



########################### OLD METHOD TO ADD A FRIEND#######################


##def add_friend():
    ###function to add details of friends
  ##  new_name = raw_input("Please add your friend's name:")
    ##new_salutation = raw_input("Are they Mr. or Ms.?: ")
    ##new_name = new_name + " " + new_salutation
 ##   new_age = raw_input("Age?")
 ##   new_rating = raw_input("Spy rating?")
   ## if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
     ##   ####validating the details of friend entered
       ## friends_name.append(new_name)
        ##friends_age.append(new_age)
        ##friends_rating.append(new_rating)
     ##   return len(friends_name)

   ## else:
     ##   print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
   ## return len(friends_name)


###################################################################################





def add_status(current_status_message):
    ####function to add status
    if current_status_message != None:
        ###initiallly current status will be none
        print (" Your current status is " + current_status_message + "\n")
    else:
        print (" You dont have any status message currently \n")

    default = raw_input ("Do you want to select from the older status [Y/N] ?")
    ##status_messages = ['My name is Rohit', 'I am very relaible', 'Mood off', 'Over the Moon', 'Piece of Cake']
    if default.upper() == "N":
        new_status_message =raw_input(" What status message do you want to set ?")
######asking user to write status of his own and storing message in the variable new_status message
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            ####the message stored in new_status_message will get copied in the new variable updated_status_message
            print("Your updated status is " + updated_status_message)
            ##printing the updated status message
            status_messages.append(updated_status_message)
            ###appending newly entered status in the list
    elif default.upper() == "Y":
        item_position = 1
        for message in status_messages:
            ###use of for loop in the list
            print(str(item_position) + " " + message)
            ##printing status list
            item_position = item_position +1
        message_selection = int(input("\n Choose from the above messages"))
        ##asking user which status u want to add
        if len (status_messages) >= message_selection:
            updated_status_message= status_messages[message_selection-1]
            ##new status message will be updated
            print("Your updated status is " + updated_status_message)
            ##printing the updated status message
    return updated_status_message

status_messages = ['My name is Rohit', 'I am very relaible', 'Mood off', 'Over the Moon', 'Piece of Cake']
### pre stored statuses in the list





def start_chat(spy_name, spy_age, spy_rating):
    #### calling of start_chat function
    show_menu = True
    current_status_message=None
    ###current status set to none initially
    while show_menu==True:
        ###chekcing condition
        menu_choices = (" What do you want to do ? \n 1. Add a status update \n2. Add a friend \n3. Show friends \n4.Send a secret message \n5.Read a Secret message \n6.Read chats from a user \n7.Close Application \n")
        menu_choice = int(raw_input(menu_choices))
        ###asking user for his choice


        if menu_choice == 1:
            print (" You choose to update the status")
            current_status_message = add_status(current_status_message)
            ####passing current_status_message as argument in the add_status function

        elif menu_choice ==2:
            number_of_friends = add_friend()
            print("you have %d friends. " % (number_of_friends))
            ##printing number of friends spy has

        elif menu_choice ==3:
            select_friend()

        elif menu_choice ==4:
            send_message()

        elif menu_choice ==5:
            read_message()


        elif menu_choice == 7:
            show_menu = False








spy_name = "Rohit"
spy_age = 20
spy_rating = 4.4
spy_salutation = "Mr."
####default user details

question = "do you want to continue as default user (Y/N)?"

existing = raw_input(question)

if existing == "Y":
        ####from spy_details import spy_name, spy_salutation, spy_rating, spy_age
    print(" Welcome %s %s" % (spy_salutation, spy_name))
    start_chat(spy_name, spy_age, spy_rating)
else:
    spy_details_input()
    ###ask the user to enter details
    start_chat(spy_name, spy_age, spy_rating)
    ##calling of start_chat function








