# #question 2
# print("Enter triangle sides")
# x = input("x: ")
# y = input("y: ")
# z = input("z: ")

# if x==y==z:
#     print("The triangle is an equilateral")
# elif x==y or y==z or z==x:
#     print("The triangle is an isosceles triangle")
# else:
#     print("the triangle is scalene")    


#question 3
# models = [{'make':'Nokia','model':216,'color':'Black'},{'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
# print('Original list of dictionaries :')
# print(models)
# sorted_models = sorted(models, key = lambda x: x['color'])
# print("\nSorting the list of dictionaries :")
# print(sorted_models)

#question 1

# special_char = ['$','#','@']
# isvalid = True
# pass_input = input("Enter a password:\n")

# if len(pass_input) < 6:
#     print('password should be at least 6')
#     isvalid = False

# if len(pass_input) >16:
#     print('Your password should not be greater than 16')
#     isvalid = False

# if not any(char.isdigit()for char in pass_input):
#     print('password should have at least one number from [0-9]')
#     isvalid = False

# if not any(char.isupper()for char in pass_input):
#     print("Your password should have at least one upper case")
#     isvalid = False

# if not any(char.islower() for char in pass_input):
#     print('your password should have at least one lowercase letter from [a-z]')
#     isvalid = False