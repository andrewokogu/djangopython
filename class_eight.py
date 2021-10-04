
#list comprehention

# a=[1,2,3,4,5,6,7]
# # b= [i for i in a if i%2==0]
# b=[]
# for i in a:
#     if i%2==0:
#      b.append(i)
# print(b)


# a= [(0,'sheldon'),(1,'penny')]
# for e in a:
#     print(e[0])# it will print all the first element un the tupple
#     print(e)#it will brint all elements of the tupple

# a=[0,1,2]
# b=[2,4,6]
# c=[]
# for i in a :
#     for x in b:
#      c.append(i+x)
# print(c)     

# list1 = [10,20,30,40]
# list2 = [100,200,300,400]
# list2.reverse()
# for x,y in zip(list1,list2):
#     print(x, y)

# Classwork
# Email =input("Enter your email address")
# password = input("Enter your password")
# store_email = ['ejiro','andrew']
# store_password = ['paul','john']

# if Email in store_email:
#     print("User already has an account")
 
# else:
#     # print("sign up")
    
#     Name = input("Enter your name")
#     Email =input("Enter your email address")
#     password = input("Enter your password")

#     special_char = ['$','#','@']
#     isvalid = True
#     if len(password) < 6:
#         print('password should be at least 6')
#         isvalid = False

#     if len(password) >16:
#         print('Your password should not be greater than 16')
#         isvalid = False

#     if not any(char.isdigit()for char in password):
#         print('password should have at least one number from [0-9]')
#         isvalid = False

#     if not any(char.isupper()for char in password):
#         print("Your password should have at least one upper case")
#         isvalid = False

#     if not any(char.islower() for char in password):
#         print('your password should have at least one lowercase letter from [a-z]')
#         isvalid = False

#     appending_email = store_email.append(Email)
#     appending_password = store_email.append(password)

#     print("successfully logged in")
#     print(store_email)
#     print(store_password)

#classwork correction
user_data = {}
activity = input("lo")



    