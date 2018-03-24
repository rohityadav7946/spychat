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
    if spy_age < 12:
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