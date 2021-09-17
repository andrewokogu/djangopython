#question 1
# my_list= ['this', True, 'Student', 45, 66.43]
# cloned_list = my_list
# my_list.copy()
# print(" The cloned list is :\t\t",cloned_list)

#question 2
# sample_list = ['Red','Green','White','Black','Pink','yellow']
# new_list = sample_list.pop(0), sample_list.pop(3), sample_list.pop(-1)
# print("The new list components after removing the 0th,4th,5th element of the list is:\n\n",sample_list)

#question 3
# color_list = ['Red', 'Green','White','Black','Pink','Yellow']
# user_input = input("enter your favourite color")
# color_list.append(user_input)
# print(color_list)

#question 3 (using insert)
# color_list = ['Red', 'Green','White','Black','Pink','Yellow']
# user_input = input("enter your favourite color")
# color_list.insert(2,user_input)
# print(color_list)

#question 4
list1=[10,20,[300,400,[5000,6000],30,40]]
print(list1)
new_number = 7000
list1[2][2].append(new_number)
print(list1)

