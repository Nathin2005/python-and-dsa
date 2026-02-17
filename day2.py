
# student_type = input("Enter Student Type: ").lower()
# if student_type == "msb":
#     tuition_fee = float(input("**Enter Tuition Fee:** "))
#     bus_fee = float(input("**Enter Bus Fee:** "))
#     fee_amount = 1.5 * tuition_fee + bus_fee
#     print("Fee to be collected: ",fee_amount)
# elif student_type == "msh":
#     tuition_fee = float(input("Enter Tuition Fee: "))
#     hostel_fee = float(input("Enter Hostel Fee:"))
#     fee_amount = 1.5 * tuition_fee + hostel_fee
#     print("Fee to be collected: ",fee_amount)
# else:
#     print("in valid")
    
# ATM WITHDRAWEL

# balance = float(input("Enter account balance: "))
# amount = float(input("Enter withdrawal amount: "))
# if amount > balance:
#     print("Insufficient funds")
# elif amount > 10000:
#     print("Withdrawal limit exceeded")
# else:
#     balance = balance - amount
#     print("Withdrawal successful")
#     print("Remaining balance:", balance)

# Store the correct ATM PIN and balance

# stored_pin = "1234"
# balance = 15000.00
# withdraw_limit = 10000.00
# entered_pin = input("Enter your ATM PIN: ")
# if entered_pin == stored_pin:
#     print("PIN correct. Welcome!")
#     amount = float(input("Enter withdrawal amount: "))

#     if amount <= 0:
#         print("Invalid amount.")
#     elif amount > withdraw_limit:
#             print("Limit exceeded.", withdraw_limit)
#     elif amount > balance:
#                 print("Insufficient balance.", balance)
#     else:
#                 balance = balance - amount
#                 print("Withdrawal successful!")
#                 print("Remaining balance is", balance)

# else:
#     print("Wrong PIN. Access denied.")

# ticket booking theatre 

# age = int(input("Enter your age: "))
# show_time = input("Enter show time (morning/evening): ")

# child_price = 250
# adult_price = 250
# senior_price = 200
# if age < 5:
#     print("Free Entry - No ticket charge")
# else:
#     if age >= 5 and age <= 17:
#         ticket_price = child_price
#         category = "Child Ticket"
#     elif age >= 18 and age <= 59:
#         ticket_price = adult_price
#         category = "Adult Ticket"
#     else:
#         ticket_price = senior_price*0.30
#         category = "Senior Citizen Ticket"

   
#     if show_time == "morning":
#         discount = ticket_price * 0.50
#         final_price = ticket_price - discount
#     else:
#         final_price = ticket_price
#     print("Ticket Category:", category)
#     print("Final Ticket Price: Rs.", final_price)

# loop

# sum = 0
# for i in range(1, 100 , 2):
#         print (i)
#         sum += i
# print("Sum of odd numbers =", sum)

# EVEN

# sum = 0
# for i in range(2, 100 , 2):
#         print (i)
#         sum += i
# print("Sum of even numbers =", sum)

# TABLES

# number = int(input("Enter a number to table: "))
# for i in range(1, 11):
#     result = number * i
#     print(number, "x", i, "=", result)

# 5 subject marks 

# total_marks = 0
# num_subjects = 5
# for i in range(num_subjects):
#     marks = float(input("Enter marks for subject {i+1}: "))
#     total_marks += marks
# average_marks = total_marks / num_subjects
# print("Total Marks:", total_marks)
# print("Average Marks:", average_marks)

# starpattern

# for i in range(1, 6):
#         print("*" * i)
        
# for i in range(5,0,-1):
#         print("*" * i)

# WHILE

# i = 1
# while i <= 5:
#     i += 1
#     print("*" * i)

# i = 5
# while i >= 1:
#     i -= 1
#     print("*" * i)

# ODD AND EVEN 
    
# sum = 0
# i = 1
# while i < 100:  
#     sum += i
#     i += 2
#     print(i)
# print("Sum of odd numbers =", sum)

# sum = 0
# i = 0
# while i < 100:
#     sum += i
#     i += 2
#     print(i)
# print("Sum of even numbers =", sum)

# number = int(input("Enter a number to table: "))
# i = 1
# while i <= 10:
#     result = number * i
#     i += 1
#     print(number, "x", i, "=", result)


total_seats = 10
seat_number = 1  
while seat_number <= total_seats:
    name = input("Enter passenger name: ")
    print("Seat", seat_number, "booked for", name)
    seat_number += 1 
print("All seats are booked!")       