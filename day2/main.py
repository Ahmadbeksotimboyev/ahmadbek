# num_char = len(input("What is youyr name?"))

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters.")

# print(type(num_char))

# a = float(123)
# print(type(a))

# print(str(70) + str(12))
# a = input("Type a two digit number:")

# print(type(a))

# first_digit = int(1[0])
# second_digit = int(a[1])

# a = second_digit + first_digit

# print(a)

# print(type(6/3))


# print(8 // 2)

# score = 0 
# height = 1.8
# Iswinning = True 


# print("your score is" + str(score))
# print(f"your score is {score}, your height is {height}, you are winning is {Iswinning}")

# age = input("Yoshingiz")
# a =int(age)

# years_remaining = 90 - a 
# days_remaining = years_remaining * 365 
# week_remaining = years_remaining * 53 
# month_remaining = years_remaining * 12

# print(f"You have {days_remaining} days, {week_remaining} weeks and {month_remaining} month")

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15?"))
people = int(input("How many poeple to split the bill?"))
tip_as_percent = tip / 100 
total_tip_amount = bill * tip_as_percent 
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people 
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")