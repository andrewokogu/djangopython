import random
import time

user_data = {}
balance = 0
isvalid = True

#log in
for i in range(1000):
    activity  = input("login or signup?\n>>>").lower()

    if activity == "login":
       acc_num = input("Enter your account number:\n>>>")
       pin = input("Enter your pin:\n>>")

       if acc_num in user_data.keys():
         actual_acc_num = user_data.get(acc_num)
         
         if actual_acc_num== pin:
           print("login successful\t\t")
         
         else:
            print("Please enter a valid pin") 
            continue
       else:
        print("there is no active user with this pin")  
        break  
    
#sign up
    if activity == "signup":
        for i in range(100):
            pin = input("Enter 4 digits:\n>>")
            confirm_pin = input("confirm pin:\n>>")
            if len(pin) != 4:
                print("pin should be 4 digits ")
                isvalid = False

            elif pin != confirm_pin:
                print("pin doesnt match")
                isvalid = False

            else:
                isvalid = True
                user_account_number = random.sample(range(0,10),9)
                account_no_str = [str(i) for i in user_account_number]
                acc_num = "".join(account_no_str)
                time.sleep(1)
                print("generating your number.......")
                time.sleep(2)
                print("Your account number was generated sucessfully!")
                print("Your account number is:", acc_num)
                user_data[acc_num] = pin
                print(user_data)
                break
#continue option to login/create account
        con_tinue = input("Press 'y' to login and any key to Quit!\n>>").lower()  
        if con_tinue =='y':
            continue
        else:
            break
        
                    
#atm options
      
    print('Please Press 1 For Your Balance\n')
    print('Please Press 2 To Make a Withdrawal\n')
    print('Please Press 3 To Deposit money\n')
    print('Please Press 3 To Transfer money\n')

    option = int(input('What Would you like to choose?\n>>'))

    if option == 1:
            print('Your Balance is now Naira',balance)
            restart = input("would you like to go back y/n ?").lower()
             
    
            if restart in ('n'):
                 print('Thank You for using our ATM')
                 break
        
            else:
                 continue
      
    elif option == 2:
       withdraw = int(input('enter the amount you want to withdrawal\n>>'))
       if withdraw > balance:
                print("Insufficient funds")
                break
       else:
                print("processing..................\n\n please take your cash") 
                break

#For deposit
    elif option == 3:  
        deposit = int(input('Enter deposit amount:\n>>')) 
        balance = balance + deposit
        print(f"Transaction Successful!\nYour account balance is ${balance}")
        break



    elif option == 4:
                for i in range(5):
                 recipient = input('enter the reciepients name') 
                 recipient_acc_no = input('enter the recipients account number\n>>')
                 transfer_amount = int(input('enter transfer ammount\n>>'))
                 if len(recipient_acc_no) < 9:
                   print("The account number is incorrect")

                 elif transfer_amount > balance:
                     print("Insufficient funds") 
                     time.sleep(2)
                     print("try again with an amount lower than your balance")
                     continue
                 else:
                   print("your transfer is processing.......") 
                   time.sleep(2)
                   print("your transfer was successful")
                   break   
      