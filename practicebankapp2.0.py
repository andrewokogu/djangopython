import random
import time
user_data = {}
transaction_record = {}
isvalid = True
keep_running = True

while keep_running:
    #user signs up and acount number is generated and put in a dictionary with user details
    user_activity = input("enter s to signup, l to login and any key to quit\n>>").lower()
    if user_activity == 's':
        name = input('enter your name\n>>')
        pin = input('enter your pin')

        num = [str(i) for i in range(10)]
        acc = ['9']
        acc.extend([random.choice(num) for i in range(9)])
        account_num = "".join(acc)
        data = [('name',name),('pin',pin),('balance',0)]
        user_data[account_num] = {}
        user_data[account_num].update(data)
        # print(user_data)

        #empty transaction record list
        transaction_record[account_num]= []

        # print(transaction_record)
        print(f'Your account has been successfully activated.\n\nYour account number is {account_num}.\n\nYour current balance is NGN 0.00.\n\nPlease log in to deposit or perform other transactions\n')

        progress = input("Enter p to do something else and any key to quit.\n>>").lower()
        if progress == 'p':
            continue
        else:
            break
    elif user_activity == 'l':
        print("Enter login details below".title())
        account_num = input('Account num:\n>>')
        pin = input("Enter your 4 digit pin\n>>")
        
        #checks if password in dictionary is the same with the input acc num and pin

        account_details = user_data.get(account_num, False)    
        if account_details and account_details.get('pin') == pin:
            logged_in = True
            while logged_in:
                action = input(f"""Welcome, {account_details.get('name')}!
what would you like to do?
            a for account statement
            b for balance
            d for deposit
            t for transfer
            w for withdrawal
press any other key to logout\n>>""").lower()  

                if action == 'w':
                    amount = float(input("Enter amount to withdraw\n>>"))

                    if amount >= account_details.get('balance', 0):
                        time.sleep(2)
                        print('Insufficient funds\n')   
                    else:
                        account_details['balance']-=amount #ask someone
                        print('Please take your cash')

                        transaction_data = {
                            'amount':amount,
                            'trans_type':'debit',
                            'transaction':'withdrawal'
                        }
                          
                        transaction_record[account_num].append(transaction_data)
                        # print(transaction_record)
                        progress = input("Enter p to do something else and any key to logout").lower()
                        if progress == 'p':
                            continue
                        else:
                            break


                elif action == 'd':  
                    amount = float(input('Please enter amount to deposit\n>>')) 

                    account_details['balance'] += amount
                    print('deposit is complete')

                    transaction_data = {
                        'amount':amount,
                        'trans_type': 'credit',
                        'transaction':'Deposit'
                    }

                    transaction_record[account_num].append(transaction_data)

                    progress = input("Enter p to do something else and any key to logout\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break

                elif action == 't':
                    amount = float(input('Enter transfer amount\n>>')) 
                    recepient_account = input('Enter recepient account number\n>>')

                    recepient = user_data.get(recepient_account, False)
                    
                    if recepient:
                        if amount >= account_details.get('balance', 0):
                            print("Insufficient funds.")
                        else:
                            account_details['balance']-=amount   

                            #save transaction details
                            transaction_data = {
                                'amount':amount,
                                'trans_type':'Debit',
                                'transaction':'Transfer'
                            } 
                            transaction_record[account_num].append(transaction_data)
                    
                            recepient['balance'] += amount 

                            beneficiary_transaction_data = {
                                'amount':amount,
                                'trans_type':'Credit',
                                'transaction':'Transfer'
                            } 
                            transaction_record[recepient_account].append(beneficiary_transaction_data)
                            print("Transfer successful")
                            
                            progress = input("Enter p to do something else and any key to logout\n>>").lower()
                            if progress == 'p':
                                continue
                            else:
                                break
                    else:

                        print('No active customer for this account number')
                        progress = input("Enter p to do something else and any key to logout\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                
                
                elif action == 'b':
                    print(f"Your current balance is NGN{account_details['balance']}\n")

                elif action == 'a':
                    if len(transaction_record[account_num]) > 0:
                        last_5_transactions = transaction_record[account_num][-5:]
                        print("Here are your last 5 transactions")
                        for transaction in last_5_transactions:
                            print('Amount:', transaction['amount'])
                            print('Transaction type', transaction['trans_type'])
                            print('Transaction Ref:',transaction['transaction'])
                            print()

                    else:
                        print('You have not made any recent transactions. Please make a transaction')

                else:
                    break        
        else:
    
            print('Please enter a valid account number and pin')

    else:
        print('sorry to see you go.')
        break        

print(user_data)
print(transaction_record)                            







                    
                     

                

