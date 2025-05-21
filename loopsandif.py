import random
# print("hello world")


# print("Enter your age")

# age = int(input())

# print("So your age is "+ str(age), end = "?\n")

# if age >= 18:
#     print("You are an adult")
# elif age >= 13:
#     print("You are a tenager")
# else:
#     print("you are foolish")    
    
# cars = ["Volvo", "Benz"]

# for car in cars:
#     print(car)

# 

balance = 2000

withdraw = int(input("Enter the amount you wanna withdraw"))

if (withdraw == balance):
    print("How about withdraw charges!")
elif (withdraw > balance):
    print("Your account balance is too low")
else:
    print("Withdraw Successful!!!")    