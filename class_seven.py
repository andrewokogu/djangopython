# Built in functions
#Built in functions already used by python at
# len()
# input()
# sum()
# min()
# max()
# zip()
 



#write a program that takes in input from the user asking him for a list of the total prices of items bought in 7days seperated by a comma

# calculate the sum
# calculate the average

# return a stdout(standard output telling him how much he has spent and the total amount)

# user_input = input("enter list of total items bought in ...")
# user_input1 = input("enter the prices of items :\n").split(",")
# print(user_input1)
# length = len(user_input1)
# print(length)

# #########total_sum = sum(int(user_input1))
# numbers = list(map(lambda string: int(string),user_input1)) #using lambda and mapping it takes in a string and returns the int of the string
# print(sum(numbers))
# avg = print(sum(numbers)/len(numbers))

#using zip() funtion
# customer = ["002","014","029"] #if both strings are not of the same length it cuts out the excess
# price = [2000,4000,2015]
# d = dict(zip(customer,price))
# l1 = list(zip(customer,price))
# print(d)
# print(l1)

#using enumerator enum() function
#enum gives the index and the value
# names = ["Ejiro", "Andrew", "Okogu"]
# output = enumerate(names)
# print(list(output))

#using filter()
# mylist = [2,3,5,7,8,20,4,1,9]
# my_filter = filter(lambda x : x % 2!=0,mylist)
# #my_filter = list(filter(lambda x : x % 2,mylist))# another method
# print(list(my_filter))


# #using range()
# my_num = range(1, 8)
# print(list(my_num))

# import time
# print(time.gmtime())
# #gives time in real time (present time)

# print(time.time())
# #returns the time in seconds

# print(time.localtime())
# #this gives the local time at our location

# print(time.sleep(5))
# #stops time in python by the specified seconds(5secs)

# user = input("Enter your name:\n>")
# print("creating account, please wait...")
# time.sleep(3)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print("almost there..")
# time.sleep(2)
# print(f"Welcome {user},your account has been created")

#using rnadom function
import random
# my_list = [2,3,5,3,1,4,56,3]
# random.shuffle(my_list) #shuffles the list
# print(random.sample(my_list,3)) #pick 3 numbers from shuffled numbers
# print(my_list)

# random.seed(2)
# print(random.randrange(3,10))

#########learning datetime()##########

# from datetime import datetime
# print(datetime.now())

# from datetime import datetime
# # slide 47
# date = datetime.now()
# #tells us the present time
# print(datetime.strftime(date,"%A,%d,%B,%Y")) 
# #strf helps converts time to a string to be more readable

#conditional statements (if, else, elif)
#conditions are rules that guide an operation

#import random

# def random_nums(n):
#   return[random.randrange(n) for i in range(n)] 
# #self created function to generate random numbers  

import random
from typing_extensions import ParamSpecArgs
# print("Welcome to this game")
# list_of_numbers = [0,34,23,12,5,67,4,24,79,33,7,8,2]
# choice = int(input(f"Guess number from:\n{list_of_numbers}\n>>"))
# random.shuffle(list_of_numbers)
# com_choice = random.choice(list_of_numbers)
# if choice==com_choice:
#     print("You win")
# else:
#     print("E be like say you no win. Sorry")    
# game using random

#rock paper scissors game
# print("Welcome to this game")
# list_choices = ['Rock','Paper','Scissors']
# choice = input(f"Pick something from the list:\n{list_choices}\n>>").title()
# print(choice)
# random.shuffle(list_choices)
# comp_choice = random.choice(list_choices)

# if choice == comp_choice:
#     print("draw")
# elif choice == list_choices[0] and comp_choice == list_choices[1]:
#     print("computer wins")

# elif choice == list_choices[0] and comp_choice == list_choices[2]:
#     print("user wins")

# elif choice == list_choices[1] and comp_choice == list_choices[0]:
#     print("computer wins")

# elif choice == list_choices[1] and comp_choice == list_choices[2]:
#     print("computer wins")

# elif choice == list_choices[2] and comp_choice == list_choices[0]:
#     print("user wins")

# elif choice == list_choices[2] and comp_choice == list_choices[1]:
#     print("computer wins")

# else:
#     print("wrong input value") 
    

print("welcome to the game")
print("Rock Paper Scissors")
choice = input("Enter 'h' for help or 'p' to play:\n>").lower()

help = """
This is a simple game that follows the rule below:
Rock wins Scissors
Paper wins Rock
Scissors wins Paper
"""

print(help)

player_choice = input("what do you choose?\n>").lower()
choices = ['r','p','s']
random.shuffle(choices)
com_choice = random.choice(choices)

if player_choice in choices:
    if(player_choice=='r' and com_choice=='s') or (player_choice=='p' and com_choice=='r') or (player_choice=='s'and com_choice=='p'):
     print("you win")

    elif (com_choice=='r' and player_choice=='s') or (com_choice=='p' and player_choice=='r') or (com_choice=='s' and player_choice=='p'):
     print("computer win")

    else:
     print('its a tie')

else:
    print("invalid input. you lose!")




