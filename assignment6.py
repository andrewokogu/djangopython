import random
first_name = input("enter your first name\n>>")
last_name = input("enter your last name\n>>")
pin = int(input("enter a pin"))

#generate account number
balance = 20000
user_data = {}
random_num = random.sample(range(0, 10), 10)
acc_num_str = [str(i) for i in random_num]
acc_num= "".join(acc_num_str)
print("Your account number is:\n",acc_num)

user_data[acc_num] = pin
print(user_data)

#log in
if acc_num in user_data.keys():
    user_name = input("enter account number\n>>")
    password= input("enter your password\n>>")

    actual_password = user_data.get(acc_num)
    if actual_password == pin:
        print("login successful")
    else:
      print("wrong login details") 

#atm options

print('Please Press 1 For Your Balance\n')
print('Please Press 2 To Make a Withdrawal\n')
print('Please Press 3 To transfer money\n')

#while True: 	
option = int(input('What Would you like to choose?'))

if option == 1:
      print('Your Balance is now Naira',balance)
      restart = input("would you like to go back ?")
    
      while restart in ('n','NO','no','No','nO'):
       print('Thank You for using our ATM')
       break
	   
      		
elif option == 2:
     withdraw = int(input('enter the amount you want to withdrawal\n>>'))
     if withdraw > balance:
        print("Insufficient funds")
     else:
        print("processing..................\n\n please take your cash") 


if option == 3:
     recipient = input('enter the reciepients name') 
     recipient_acc_no = int(input('enter the recipients account number\n>>')) 
     if recipient_acc_no < 10:
         print("The account number is incorrect")
     else:
         print(f"  {first_name}, your transfer was successful")    
      
             


     



#atm transaction
# check balance
# withdraw
# transfer




#print(joined)
#print(type(random))

