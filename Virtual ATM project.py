#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
Welcome to my virtual ATM machine, project will produce a menu screen allowing you to,enter your pin,
withdraw money,check your balance and deposit money.
'''
#note correct pin is 1234
#Task 1: inputting the correct pin
def int_check (pin):
    if pin.isdigit() and len(pin) == 4:
            return True
    else:
            return False
    
pin_req=input('Welcome to virtual project atm!Please enter your 4 digit pin:')
int_check(pin_req)
while not int_check(pin_req):   
    print("you must input four integers as the pin")
    pin_req=input('Try again!Please enter your 4 digit pin:')
pin_attempt=0
while pin_req !='1234' and pin_attempt<=3:
    pin_attempt +=1
    pin_req=input('Wrong pin try again. Please enter your 4 digit pin:') 
    if pin_attempt==3:
        print('Too many wrong attempts,please resart the program')
        break 
#Task 2: set up bank menu
#Each client is given a random money amount
import random
random_bal= round(random.uniform(0.0,2000.0),2)

#Function to check if correct data type is being inputted by user
def val_check (vall):
    if vall.isdigit():
            return True
    else:
            return False
#function contains 4 main conditions where 'q' leads to the end of the program , '1'allows users to view their account,
#'2' and '3'allow for cash deposit and withdrawl respectively
def welcome (number):
    global random_bal
    if number == 'q':
        return number
    
    if number == '1':
        user_input= input(f"your current balance is £{random_bal}.\n Press any key to return to the menu or q to quit\n")
        return user_input
    
    if number== '2':
        print(f'Welcome to cash deposit.Your current balance is £{random_bal}\n.Please note that we only accept notes (£5,£10,£20,£50) at this time.\n ')
        cash_in= input('Please enter the amount of cash you would like to add at this time')
        if cash_in == 'q':
            user_input= 'q'
            return user_input 
        else:
            while not val_check(cash_in): 
                print(f'At this time , we only accept notes,as £{cash_in} is not an integer we cannot take this amount')
                cash_in=input(f'Your current balance is £{random_bal}. \n Please enter the amount you would like to add')
                if cash_in == 'q':
                    user_input= 'q'
                    return user_input 
                
        cash_in=int(cash_in)
        while cash_in % 5 !=0:
            print(f'At this time , we only take notes,as £{cash_in} is not divisible by 5 we cannot take this amount')
            cash_in=input(f'Your current balance is £{random_bal}. \n Please enter the amount you would like to add')
            if cash_in == 'q':
                user_input= 'q'
                return user_input 
            elif not val_check(cash_in):
                continue
            else:
                cash_in=int(cash_in)
        random_bal=random_bal+cash_in
        print(f'Complete your new balance is £{random_bal}')
        user_input=input("Press any key to return to the menu or q to quit\n")
        return user_input
    
    if number=='3':
        print(f'Welcome to cash withdrawl.Your current balance is £{random_bal}\n.Please note that we only accept notes (£5,£10,£20,£50) at this time.\n ')
        cash_out= input('Please enter the amount of cash you would like to withdraw at this time')
        if cash_out == 'q':
            user_input= 'q'
            return user_input 
        else:
            while not val_check(cash_out): 
                print(f'At this time , we only accept notes,as £{cash_out} is not an integer we cannot take this amount')
                cash_out=input(f'Your current balance is £{random_bal}. \n Please enter the amount you would like to withdraw')
                if cash_out == 'q':
                    user_input= 'q'
                    return user_input 
                
        cash_out=int(cash_out)
        while cash_out % 5 !=0:
            print(f'At this time , we only accept notes,as £{cash_out} is not divisible by 5 cannot take this amount')
            cash_out=input(f'Your current balance is £{random_bal}. \n Please enter the amount you would like to withdraw')
            if cash_out == 'q':
                user_input= 'q'
                return user_input 
            elif not val_check(cash_out):
                continue
            else:
                cash_out=int(cash_out)
        random_bal=random_bal-cash_out
        if random_bal < 0:
            print('insuffient funds to withdraw this amount')
            random_bal=random_bal+cash_out
        else:
            print(f'Complete your new balance is £{random_bal}')
        user_input=input("Press any key to return to the menu or q to quit\n")
        return user_input
#End of function 
        
print('Welcome to your bank,please press a number to complete the following action. Press q to quit at any time')
user_input= input('1: Balance request \n2:Deposit money \n3:Withdraw money \n')
while True:
    user_input = welcome(user_input)
    if user_input == 'q':
        print('Thank you for using our services today.Goodbye')
        break
    else:
        print('Welcome to your bank,please press a number to complete the following action. Press q to quit at any time')
        user_input= input('1: Balance request \n2:Deposit money \n3:Withdraw money \n') 

#Some later improvements could be stopping the error message 

