# #a = [8,7,2,4]
# #b = [4,2,9,0]
# #a.extend(b)
# #print(a)

# #question 1
# #username_list = []
# #first_name = input("Tell me your first name\n")
# #second_name = input("Tell me your last name\n")
# #new_name = second_name[0:3]
# #new_name1 = first_name[-2:
# #usernames = new_name + new_name1
# #username_list.append (usernames)
# #print(username_list)
# #output = "hello, " + first_name.title() + "\nThank you for signing up. your accout has successfully been created/n Your account ID is " + usernames + "\n\tCheers\n\tAdmin"
# #print(output)

# #question 2
list_numbers = [500,200,[200,500,700,[250,800],250],[1000]]
new_number = list_numbers[2][2] + list_numbers[2][3][1]
print(new_number)
list_numbers[3].append(new_number)
print(list_numbers)

# #question 3
# #str1 = "Emma is a data scientist who knows python. Emma works at  google."
# #search = str1.rindex("Emma")# you can use rfind or rindex
# #print(search)

# #Question 4
# #a = [200,300,400]
# #b=a
# #c=a.copy() #returns a copy of the list
# #a[0]=500
# #print(a)
# #print(b)
# #print(c) 

# #remove method (list methods)

# #a = [0,1,2,3,4]
# #b = a.remove(3)
# #print(a)

# # pop method(list)
# #a = [0,1,2,3,4]
# #b = a.pop(-1)
# #print(a)
# #print(b) 

# #Insert method(List)
# #List_ = [3136,3249,3364,3481,3600,3721,3844,3969,4096]
# #print(List_)
# #List_.insert(3,"I just got inserted")
# #print(List_)
# #print(List_.index(3136))# returns the index of the value 3136

# # sort() method in lists
# List_ = [70,34,100,36,50]
# List_.sort() #sorts in ascending order
# print(List_)
# List_.reverse() #sorts in decending 
# print(List_)


