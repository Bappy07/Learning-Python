num = int(input("enter the number: "))
if num > 0:
    print("Positive")
else:
    print("Not Positive")
    
Login system
username = input("Enter name: ")
password = input("Enter password: ")
if username ==  "admin":
    if password == "1234":
        print("Login successfully")        
    else:
        print("worng password")
else:
    print("User not found")

Movie ticket
age = int(input("Enter the age: "))
has_ticket = input("do  you have ticket: ")
if age >= 18:
    if has_ticket == "yes":
        print("You may enter")
    else:
        print("Buy a ticker first")
else:
    print("Your are not allowed to enter")
    
Atm withdrawal
balance = int(input("Enter you balance: "))
withdraw_amount = int (input("Enter your withdrawal ammount: "))
if balance >= withdraw_amount:
    if withdraw_amount > 0:
        print("Transaction successful")
    else:
        print("Invalid amount")
else:
    print("Insufficien balance")

scolership eligibility
marks = int(input("Enter your mark: "))
family_income = int(input ("Enter the amount: "))
if marks >= 80:
    if family_income <= 50000:
        print("Scholership approved")
    else:
        print("Marks are good, but income is too high.")
else:
    print("Not Eligible")

chalange harder
username = input("Enter the name: ")
password = input("Enter the password: ")
otp = int(input("The otp is: "))
if username == "Bappy":
    if password == "py123":
        if otp == "9876":
            print("Login successful")
        else:
            print("Invalid OTP")
    else:
        print("Wrong Password")
else:
    print("User not found")


***************
pin = int(input())
balance = int(input())
withdraw = int(input())
if pin == 1234:
    if withdraw <= balance:
        if withdraw > 0:
            print("Transaction Successful")
            print("Remaining Balance:", balance - withdraw)
        else:
            print("Invalid withdrawal Amount")
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")

gpa counting
gpa = float(input())
english_marks = int(input())
age = int(input())
if gpa >= 3.50:
    if english_marks >= 70:
        if age <= 25:
            print("Admission Approved")
        else:
            print("Age limited exceeeded")
    else:
        print("English mark too low")
else:
    print("GPA too low")  
    
online shopping discount
total_price = int(input("enter the price: "))
is_member = input("do you have  mambership yes/not: ")
coupon = input("do you have coupon code: ")
if total_price >= 5000:
    if is_member == "yes":
        if coupon == "yes":
            print("20% disocunt applied.")
        else:
            print("10% member discount applied.")
    else:
        print("No member discount.")
else:
    print("Minimum purchase not reached.")
    
game level unlock
level = int(input())
coins = int(input())
boss_defeated = input("Player defeted ? yes/not:")
if level >= 10:
    if coins >= 1000:
        if boss_defeated == "yes":
            print("secret level unlocked")
        else:
            print("Defeat the boss first")
    else:
        print("Not enough coin")
else:
    print("Reach level 10 first")

employee bonus
years_of_service = int(input())
performance = input("Bhalo nakie kharap? good/bad: ")
attendance = int(input())
if years_of_service >= 5:
    if performance == "good":
        if attendance >= 90:
            print("Bonus Approved")
        else:
            print("Attendance too low for bonus")
    else:
        print("Performance not eligible")
else:
    print("not enough years of service")

Grade calculator using elif
mark = int(input("enter your mark: "))
if mark >= 80:
    print("Grade A")
elif mark >= 70:
    print("Grade B")
elif mark >= 60:
    print("Grade C")
elif mark >= 50:
    print("Grade D")
else:
    print("Fail")
    
example of elif
color = input("Select a color: ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ger Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid signal")
    
example of day of the week
day = int(input("Enter the day : "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Staurday")
elif day == 7:
    print("Invalid Day")

calculator 
temperature = int(input("What is the temp: "))
if temperature >= 35:
    print("Very Hot")
elif temperature >= 24 and temperature <= 34:
    print("Warm")
elif temperature >= 15 and temperature <= 24:
    print("Pleasent")
elif temperature >= 5 and temperature <= 14:
    print("Cold")
else:
    print("Very Cold")
    
movie ticket price
age = int(input("Enter age number: "))
if age < 5:
    print("Free")
elif age >= 5 and age <= 12:
    print("100 tk lagbe")
elif age >= 13 and age <= 59:
    print("200 tk lagbe")
else:
    print("150 tk")


////////////////////////////////
Hardest problem of if else elif
ac_num = int(input("Enter the account number: "))
pin = int(input("Enter your pin number: "))
balance = int(input("Enter your balance: "))
transaction = input("Enter transaction type (withdraw,deposite,check): ")
amount = int(input("Enter amount:  "))
if ac_num == 1001:
    print("Continue")
else:
    print("Invalid account")
if pin == 4321:
    print("Continue")
else:
    print("Incorrect Pin")
if transaction == "withdraw":
    if amount <= 0:
        print("Invalid ammount")
    elif amount > balance:
        print("Insufficient Balance")
else:
    print("Withdrawal Successful")
    print("Remaining Balance: ", balance - transaction)
if amount > 0:
    print("Deposite Successful")
    print("New Balance: ", balance + transaction)
else:
    print("Invalid Ammount")
if transaction == "check":
    print("Current Balance: ", balance - transaction)
else:
    print("Invalid Transation Type ")


ac_num = int(input("Enter the account number: "))
pin = int(input("Enter your PIN: "))
balance = int(input("Enter your balance: "))
transaction = input("Enter transaction type (withdraw, deposit, check): ").lower()

if ac_num == 1001:
    if pin == 4321:

        if transaction == "withdraw":
            amount = int(input("Enter amount: "))

            if amount <= 0:
                print("Invalid Amount")
            elif amount > balance:
                print("Insufficient Balance")
            else:
                balance = balance - amount
                print("Withdrawal Successful")
                print("Remaining Balance:", balance)

        elif transaction == "deposit":
            amount = int(input("Enter amount: "))

            if amount > 0:
                balance = balance + amount
                print("Deposit Successful")
                print("New Balance:", balance)
            else:
                print("Invalid Amount")

        elif transaction == "check":
            print("Current Balance:", balance)

        else:
            print("Invalid Transaction Type")

    else:
        print("Incorrect PIN")

else:
    print("Invalid Account")

University exam result System
StudentId = int(input("Enter sudent id: "))
Name = input("Enter student name: ")
Marks = int(input("Enter your mark: "))
Attendance = float(input("Enter your percentage: "))
Assignment_Submitted = input("assignment submitted or not: ").lower(20)
if StudentId == 2025:
    print("Continue")
    if Marks >= 40:
        print("Continue")
        if Attendance >= 75:
            print("continue")
            if Assignment_Submitted == "yes":
                print("continue")             
                if Marks >= 80:
                    print("Congratulation!\nGrade:A")
                elif Marks >= 70:
                    print("Grade: B")
                elif Marks >= 60:
                    print("Grade: C")
                elif Marks >= 50:
                    print("Grade: D")
                else:
                    print("Grade: Pass")
            else:
                print("Failed because assignment was not submitted")
        else:
            print("Failed because of low attandence")
    else:
        print("Failed due to low marks")
else:
    print("Invalid student Id")

*-++++-/--+-/-+---+-+--*-++/--
Resturant Ordering System 
Customer_Name = input("Enter customer name: ")
Membership = input("has_mambership (yes/not)?: ").title()
Food_category = input("Category: (Burger,Pizza,Drinks)")
Quantity = int(input("Enter quantity: "))
if Food_category == "Burger":
    Item = input("Enter burger type(chiken/beef): ").title()
    if Item == "Chicken":
        price = 250 
    elif Item == "Beef":
        price = 350
    else:
        print("Invalid burger type")
        exit()
    total = price * Quantity
    if Quantity >= 5:
        print("You get discount: ")
        total = total * 0.90
    print("Total Bill: ", total)

Customer_Name = input("Enter customer name: ")
Membership = input("Has membership (yes/no)?: ").title()
Food_category = input("Category (Burger, Pizza, Drinks): ").title()
Quantity = int(input("Enter quantity: "))

if Food_category == "Burger":
    Item = input("Enter burger type (Chicken/Beef): ").title()

    if Item == "Chicken":
        price = 250
    elif Item == "Beef":
        price = 350
    else:
        print("Invalid burger type")
        exit()

elif Food_category == "Pizza":
    Item = input("Enter pizza type (Small/Large): ").title()

    if Item == "Small":
        price = 500
    elif Item == "Large":
        price = 900
    else:
        print("Invalid pizza type")
        exit()

elif Food_category == "Drinks":
    Item = input("Enter drink type (Coke/Juice): ").title()

    if Item == "Juice":
        price = 50
    elif Item == "Coke":
        price = 120
    else:
        print("Invalid drink type")
        exit()

else:
    print("Invalid category")
    exit()

total = price * Quantity

discount = 0

# Quantity discount
if Quantity >= 5:
    discount = total * 0.10

final_price = total - discount

print("\n------ CUSTOMER BILL ------")
print("Customer Name :", Customer_Name)
print("Category      :", Food_category)
print("Item          :", Item)
print("Quantity      :", Quantity)
print("Total Bill    :", total)
print("Discount      :", discount)
print("Final Price   :", final_price)

=================the while loop============
i = 1
while i < 6:
    print(i)
    i += 1
============== the break statement==============
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

the continue statement============
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

the else statement==============
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer lees than 6")

=============== for loop statement==============
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    
===========Looping through a string==============
for x in "banana":
    print(x)
    
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "cherry":
        break
    print(x)

========
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
=================
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

************
for x in range(6):
    print(x)

============= INCREMENT THE RANGE OR NUMBER ================  
for x in range(2,30,3):
    print(x)
=============else in for loop
for x in range(6):
    print(x)
else:
    print("Finaly finished!")