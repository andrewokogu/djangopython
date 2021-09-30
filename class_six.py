# Dictionaries  (the keys in this dictionary is "pet", "colour")
# "pet" becpmes Black
# my_diction = {"pet":"Dog","Colour":"Brown"}
# my_diction["pet"] = "Black"
# print(my_diction)

#dictionary get methods
# my_diction = {"pet":"Dog","Colour":"Brown"}
# pets = my_diction.get("pet")
# print(pets)

#adding another un-existing key to the dictionary
my_diction = {"pet":"Dog","Colour":"Brown"}
my_diction["ejiro"] = "Black"
print(my_diction)

#get am input from the user to ask for his course and score. Add his course to the course and his score
# user_course = input("Enter a course\n")
# user_score= input("Enter a score\n")
# my_list = {"name":"Jerry","courses":["Data science", "Backend"],
#  "Scores":{"Data science":20,
#  "Backend":15.7,}}
# my_list["courses"].append(user_course)
# my_list["Scores"][user_course]= user_score #this will update 
# #print(my_list)
# print(my_list.items()) #this will group all the items in a tuple

#Update
# my_dictionary = {"name":"ejiro",
# "gender":"male"}
# my_dictionary.update({"key":"value"})# takes in key value pair
# list_of_tuples = [("ejiro","Abuja"),("Nigeria","Canada")]

# my_dictionary.update(list_of_tuples)
# print(my_dictionary)

#pop
# my_dict= {"name":"Jerry","courses":["Data science", "Backend"],
#  "Scores":{"Data science":20,
#  "Backend":15.7,}}
# var = my_dict.pop("Scores")
# my_dict.update({"result":var})# it pops the value and saves it in var
# my_dict["result"]=var # same as the above step
# print(my_dict)

# a = my_dict["result"]
# print(type(a))
# print(my_dict.keys())
# print(type(my_dict.keys()))

# question 0 
# change brads salary from 6500 to 8500
# sampleDict = {
# 'emp1':{'name':'john','salary':7500},
# 'emp2':{'name':'emma','salary':8000},
# 'emp3':{'name':'brad','salary':6500}
# }
# sampleDict['emp3']['salary']= 8500
# print(sampleDict)

#question 1
# users = {}
# first_name = input("please enter your firstname: ")
# last_name = input("please enter your lastname: ")
# username = first_name[:2] + last_name[-2:]
# users[username]={}
# users[username]["firstname"] = first_name
# users[username]["lastname"] = last_name
# print(users)


#question 1
#write a program that takes in the user details and saves it in the user dictionary following the format above
#{username:{'firstname': 'firstname','lastname':'lastname'}}
# user_dict = {'username':{}}
# user_firstname = input("enter your firstname\n")
# user_lastname= input("enter your lastname\n")
# user_dict['username'].update({'firstname':user_firstname})
# user_dict['username'].update({'lastname':user_lastname})
# print(user_dict)

#question 2
#given the list below
#[2,2,4,6,7,2,4,4,3,6,2,1] write a program to remove duplicates from the list and sorts it

# list1 = [2,2,4,6,7,2,4,4,3,6,2,1]
# list_to_set = set(list1)
# list1.sort()
# new_list = list(list_to_set)
# print(new_list)

#question 3
#write a program to convert a list of multiple integers to a single integer
# list1 = ['11','55','33']
# list_to_string = list1[0] +list1[1]+list1[2]# changes list to string
# print(type(list1))#to check the type
# string_to_list = int(list_to_string)
# print(string_to_list)

#question 4
#write a program to unpack a tupple into several variables
#unpacking means 
# tupple1 = ('ejiro','okogu','paul','tosin')
# a,b,c,d = tupple1
# print(a)
# print(b)
# print(c)
# print(d)

#question 5
#write a program to convert the tupple bellow to string
#("u","n","i","v","e","l","c","i","t","y")

# tupple1 = ('u',"n","i","v","e","l","c","i","t","y")
# tupple_to_string = str(tupple1)
# str = "".join(tupple1)
# #str = "".join(tupple1)
# print(tupple_to_string)
# print(str)

#hacckerant question on set using symmetric differrence
# num_english = int(input())
# english = input()
# num_french = int(input())
# french = input()
# words_english = set(english.split())
# words_french = set(french.split())
# final = words_english.symmetric_difference(words_french)
# print(final)

