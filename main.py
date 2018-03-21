print("Welcome to Spy Chat")
## Welcome Greet to the User##
spy_name = raw_input("What is your spy_name")
##asking user for the spy name and storing the input in the variable spy_name##
print('Welcome '+spy_name+', good to see you here.')
## greeting the spy with his/her name##
spy_salutation = raw_input ("What should i call you Mr. or Ms. ?")
##asking the spy for the salutation and storing the input in the variable spy_salutation##
spy_name = spy_salutation + ' '+ spy_name
##merging the salutation and the spy name to form the complete name and updating the complete spy name##
print('Alright ' +spy_name+ ' I would like to know a little bit more about you...')
##conversation with the spy##
