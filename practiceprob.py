# num = int(input("enter the number: "))
# if num > 0:
#     print("Positive")
# else:
#     print("Not Positive")
    
# Login system
# username = input("Enter name: ")
# password = input("Enter password: ")
# if username ==  "admin":
#     if password == "1234":
#         print("Login successfully")        
#     else:
#         print("worng password")
# else:
#     print("User not found")

# Movie ticket
# age = int(input("Enter the age: "))
# has_ticket = input("do  you have ticket: ")
# if age >= 18:
#     if has_ticket == "yes":
#         print("You may enter")
#     else:
#         print("Buy a ticker first")
# else:
#     print("Your are not allowed to enter")
    
# Atm withdrawal
# balance = int(input("Enter you balance: "))
# withdraw_amount = int (input("Enter your withdrawal ammount: "))
# if balance >= withdraw_amount:
#     if withdraw_amount > 0:
#         print("Transaction successful")
#     else:
#         print("Invalid amount")
# else:
#     print("Insufficien balance")

# scolership eligibility
# marks = int(input("Enter your mark: "))
# family_income = int(input ("Enter the amount: "))
# if marks >= 80:
#     if family_income <= 50000:
#         print("Scholership approved")
#     else:
#         print("Marks are good, but income is too high.")
# else:
#     print("Not Eligible")

# chalange harder
# username = input("Enter the name: ")
# password = input("Enter the password: ")
# otp = int(input("The otp is: "))
# if username == "Bappy":
#     if password == "py123":
#         if otp == "9876":
#             print("Login successful")
#         else:
#             print("Invalid OTP")
#     else:
#         print("Wrong Password")
# else:
#     print("User not found")


# ***************
# pin = int(input())
# balance = int(input())
# withdraw = int(input())
# if pin == 1234:
#     if withdraw <= balance:
#         if withdraw > 0:
#             print("Transaction Successful")
#             print("Remaining Balance:", balance - withdraw)
#         else:
#             print("Invalid withdrawal Amount")
#     else:
#         print("Insufficient balance")
# else:
#     print("Incorrect PIN")

# gpa counting
# gpa = float(input())
# english_marks = int(input())
# age = int(input())
# if gpa >= 3.50:
#     if english_marks >= 70:
#         if age <= 25:
#             print("Admission Approved")
#         else:
#             print("Age limited exceeeded")
#     else:
#         print("English mark too low")
# else:
#     print("GPA too low")  
    
# online shopping discount
# total_price = int(input("enter the price: "))
# is_member = input("do you have  mambership yes/not: ")
# coupon = input("do you have coupon code: ")
# if total_price >= 5000:
#     if is_member == "yes":
#         if coupon == "yes":
#             print("20% disocunt applied.")
#         else:
#             print("10% member discount applied.")
#     else:
#         print("No member discount.")
# else:
#     print("Minimum purchase not reached.")
    
# game level unlock
# level = int(input())
# coins = int(input())
# boss_defeated = input("Player defeted ? yes/not:")
# if level >= 10:
#     if coins >= 1000:
#         if boss_defeated == "yes":
#             print("secret level unlocked")
#         else:
#             print("Defeat the boss first")
#     else:
#         print("Not enough coin")
# else:
#     print("Reach level 10 first")

# employee bonus
# years_of_service = int(input())
# performance = input("Bhalo nakie kharap? good/bad: ")
# attendance = int(input())
# if years_of_service >= 5:
#     if performance == "good":
#         if attendance >= 90:
#             print("Bonus Approved")
#         else:
#             print("Attendance too low for bonus")
#     else:
#         print("Performance not eligible")
# else:
#     print("not enough years of service")

# Grade calculator using elif
# mark = int(input("enter your mark: "))
# if mark >= 80:
#     print("Grade A")
# elif mark >= 70:
#     print("Grade B")
# elif mark >= 60:
#     print("Grade C")
# elif mark >= 50:
#     print("Grade D")
# else:
#     print("Fail")
    
# example of elif
# color = input("Select a color: ")
# if color == "red":
#     print("Stop")
# elif color == "yellow":
#     print("Ger Ready")
# elif color == "green":
#     print("Go")
# else:
#     print("Invalid signal")
    
# example of day of the week
# day = int(input("Enter the day : "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Staurday")
# elif day == 7:
#     print("Invalid Day")

# calculator 
# temperature = int(input("What is the temp: "))
# if temperature >= 35:
#     print("Very Hot")
# elif temperature >= 24 and temperature <= 34:
#     print("Warm")
# elif temperature >= 15 and temperature <= 24:
#     print("Pleasent")
# elif temperature >= 5 and temperature <= 14:
#     print("Cold")
# else:
#     print("Very Cold")
    
# movie ticket price
# age = int(input("Enter age number: "))
# if age < 5:
#     print("Free")
# elif age >= 5 and age <= 12:
#     print("100 tk lagbe")
# elif age >= 13 and age <= 59:
#     print("200 tk lagbe")
# else:
#     print("150 tk")


# ////////////////////////////////
# Hardest problem of if else elif
# ac_num = int(input("Enter the account number: "))
# pin = int(input("Enter your pin number: "))
# balance = int(input("Enter your balance: "))
# transaction = input("Enter transaction type (withdraw,deposite,check): ")
# amount = int(input("Enter amount:  "))
# if ac_num == 1001:
#     print("Continue")
# else:
#     print("Invalid account")
# if pin == 4321:
#     print("Continue")
# else:
#     print("Incorrect Pin")
# if transaction == "withdraw":
#     if amount <= 0:
#         print("Invalid ammount")
#     elif amount > balance:
#         print("Insufficient Balance")
# else:
#     print("Withdrawal Successful")
#     print("Remaining Balance: ", balance - transaction)
# if amount > 0:
#     print("Deposite Successful")
#     print("New Balance: ", balance + transaction)
# else:
#     print("Invalid Ammount")
# if transaction == "check":
#     print("Current Balance: ", balance - transaction)
# else:
#     print("Invalid Transation Type ")


# ac_num = int(input("Enter the account number: "))
# pin = int(input("Enter your PIN: "))
# balance = int(input("Enter your balance: "))
# transaction = input("Enter transaction type (withdraw, deposit, check): ").lower()

# if ac_num == 1001:
#     if pin == 4321:

#         if transaction == "withdraw":
#             amount = int(input("Enter amount: "))

#             if amount <= 0:
#                 print("Invalid Amount")
#             elif amount > balance:
#                 print("Insufficient Balance")
#             else:
#                 balance = balance - amount
#                 print("Withdrawal Successful")
#                 print("Remaining Balance:", balance)

#         elif transaction == "deposit":
#             amount = int(input("Enter amount: "))

#             if amount > 0:
#                 balance = balance + amount
#                 print("Deposit Successful")
#                 print("New Balance:", balance)
#             else:
#                 print("Invalid Amount")

#         elif transaction == "check":
#             print("Current Balance:", balance)

#         else:
#             print("Invalid Transaction Type")

#     else:
#         print("Incorrect PIN")

# else:
#     print("Invalid Account")

# University exam result System
# StudentId = int(input("Enter sudent id: "))
# Name = input("Enter student name: ")
# Marks = int(input("Enter your mark: "))
# Attendance = float(input("Enter your percentage: "))
# Assignment_Submitted = input("assignment submitted or not: ").lower(20)
# if StudentId == 2025:
#     print("Continue")
#     if Marks >= 40:
#         print("Continue")
#         if Attendance >= 75:
#             print("continue")
#             if Assignment_Submitted == "yes":
#                 print("continue")             
#                 if Marks >= 80:
#                     print("Congratulation!\nGrade:A")
#                 elif Marks >= 70:
#                     print("Grade: B")
#                 elif Marks >= 60:
#                     print("Grade: C")
#                 elif Marks >= 50:
#                     print("Grade: D")
#                 else:
#                     print("Grade: Pass")
#             else:
#                 print("Failed because assignment was not submitted")
#         else:
#             print("Failed because of low attandence")
#     else:
#         print("Failed due to low marks")
# else:
#     print("Invalid student Id")

# *-++++-/--+-/-+---+-+--*-++/--
# Resturant Ordering System 
# Customer_Name = input("Enter customer name: ")
# Membership = input("has_mambership (yes/not)?: ").title()
# Food_category = input("Category: (Burger,Pizza,Drinks)")
# Quantity = int(input("Enter quantity: "))
# if Food_category == "Burger":
#     Item = input("Enter burger type(chiken/beef): ").title()
#     if Item == "Chicken":
#         price = 250 
#     elif Item == "Beef":
#         price = 350
#     else:
#         print("Invalid burger type")
#         exit()
#     total = price * Quantity
#     if Quantity >= 5:
#         print("You get discount: ")
#         total = total * 0.90
#     print("Total Bill: ", total)

# Customer_Name = input("Enter customer name: ")
# Membership = input("Has membership (yes/no)?: ").title()
# Food_category = input("Category (Burger, Pizza, Drinks): ").title()
# Quantity = int(input("Enter quantity: "))

# if Food_category == "Burger":
#     Item = input("Enter burger type (Chicken/Beef): ").title()

#     if Item == "Chicken":
#         price = 250
#     elif Item == "Beef":
#         price = 350
#     else:
#         print("Invalid burger type")
#         exit()

# elif Food_category == "Pizza":
#     Item = input("Enter pizza type (Small/Large): ").title()

#     if Item == "Small":
#         price = 500
#     elif Item == "Large":
#         price = 900
#     else:
#         print("Invalid pizza type")
#         exit()

# elif Food_category == "Drinks":
#     Item = input("Enter drink type (Coke/Juice): ").title()

#     if Item == "Juice":
#         price = 50
#     elif Item == "Coke":
#         price = 120
#     else:
#         print("Invalid drink type")
#         exit()

# else:
#     print("Invalid category")
#     exit()

# total = price * Quantity

# discount = 0

# # Quantity discount
# if Quantity >= 5:
#     discount = total * 0.10

# final_price = total - discount

# print("\n------ CUSTOMER BILL ------")
# print("Customer Name :", Customer_Name)
# print("Category      :", Food_category)
# print("Item          :", Item)
# print("Quantity      :", Quantity)
# print("Total Bill    :", total)
# print("Discount      :", discount)
# print("Final Price   :", final_price)

# ===================+++++=====================++++++============+++++++++++++
# ===================+++++=====================++++++============+++++++++++++
#   ==================== FOR LOOP AND WHILE LOOP EXESRCISE WITH PYTHON ====================

#   print Hello word ten times
# for x in range(10):
#     print("Hello, WORLD!")
# using while loop 
# count = 1
# while count <= 10:
#     print("Hello,World!")
#     count += 1
    
# +=====================+
# /                     /
# +=====================+
# PRINT NUMBERS FROM 1 TO 10

# for y in range(1 , 11):
#     print(y)

# +=====================+
# /                     /
# +=====================+
# for x in range(10, 1 , -1):
#     print(x)
    
# ===========Print all even numbers from 1 to 50.
# for x in range(1,51):
#     if x % 2 == 0 :
#         print(x)
        
# ============= Print all odd numbers from 1 to 50.
# for y in range(1,51):
#     if y % 2 != 0:
#         print(y)
        
# =======Print the multiplication table of a number.
# for b in range(1,11):
#     print(f"5 x {b} = {5 * b}")
# using variable
# num = 5
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")

# ================
# 5
    
# ===========Find the sum from 1 to N.
# n = int(input("Enter any number: "))
# total = 0
# for i in range(1, n + 1):
#     total = total + i
#     print("Sum =", total)

# n = int(input("Enter a number: "))
# print(sum(range(1, n + 1)))

# num = 100
# total = 0
# for i in range(1,num + 1):
#     total = total + i
#     print(total)

#  Find the factorial of a number.
# num = 5
# fact = 1
# for i in range(1,num + 1):
#     fact = fact * i
#     print(fact)
    
# Count from 100 to 0 by skipping 5.
# n = 100
# count = 0
# for b in range(100,-1,-5):
#     print(b)

# ====================== Print every character of a string.
# for x in "python":
#     print(x)
    
# Count how many digits a number has.
# n = 12345
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
#     print(n)
    
    
# Reverse a number.==============
# x = 12345
# reverse = 0
# while x > 0:
#     digit = x % 10
#     reverse = reverse * 10 + digit
#     x //= 10
#     print(reverse)

# print number from 1 to N
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(i)
    
# sum of first n number
# n = int(input("Enter a number: "))
# total = 0
# for i in range(1 , n + 1):
#     total += i
# print("Sum=", total)

# count digit
# n = int(input("Enter a num: "))
# count = 0
# while n > 0:
#     count += 1
#     n//= 10
# print("total=",count)

# reverse a number
# n = int(input("Enter a num:"))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n//= 10
# print(reverse)

# Largest 3 number
# k = int(input())
# l = int(input())
# m = int(input())
# largest = k 
# if l > k:
#     largest = l
# if m > k:
#     largest = m
# print("Largest is the:", largest)

# multiplication table
# a = int(input("Put a num: "))
# for i in range(1,11):
#     print(f"{a} x {i} = {a * i}")

# prime number
# n = int(input())
# prime = True
# if n <= 1:
#     prime = False
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             prime = False
#             break
# if prime:
#     print("Prime")
# else:
#     print("Not Prime")

# sum of digits
# n = int(input("Enter a num: "))
# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10
# print(total)

# factorial
# n = 10
# fact = 1
# for i in range(1,n + 1):
#     fact *= i
# print(fact)

# count odd digits in a number
# n = int(input("Enter a num: "))
# count = 0
# while n > 0:
#     digit = n % 10
#     if digit % 2 != 0:
#         count += 1
#     n //= 10
# print(count)
 
# find the largest digit in a num
# n = int(input("Enter a num:"))
# largest = 0
# while n > 0:
#      digit = n % 10
#      if digit > largest:
#         largest = digit
#      n //= 10
# print("Largest digit",largest)
        
   
# find the smallest num in a digit
n = int(input("Enter a num:"))
smallest = n % 10
while n > 0:
     digit = n % 10
     if digit < smallest:
        smallest = digit
     n //= 10
print("small digit",smallest)
        