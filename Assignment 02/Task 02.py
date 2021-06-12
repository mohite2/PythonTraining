#Question 01: 

user_input = int(input("Enter only interger number: "))

if user_input % 3 ==0: 
    print("Consultadd")
elif user_input % 5 ==0: 
    print("“Python Training")
elif user_input % 3 ==0  and user_input % 5 ==0: 
    print("“Consultadd - Python Training”")
    
    
 ## Question 02:

print("Enter 1 - Addition \nEnter 2 - Subtraction \nEnter 3 - Division \nEnter 4 - Multiplication \nEnter 5 - Average")

Operation = int(input("Enter the number for above opertions: "))
while Operation not in range(1,6): 
    print("Number not Valid")
    Operation = int(input("Enter the Valid number for above opertions: "))
    
# numbers = [int(input("Enter the number: ")) for x in range (0,2)]
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if Operation == 5: 
    print("Enter two more numbers")
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    total = (num1+num2+num3+num4)/4
elif Operation == 1:
    total = num1+num2
elif Operation == 2: 
    total = num1-num2
elif Operation == 3: 
    total = num1/num2
elif Operation == 4:
    total = num*num2

if total <0: 
    print("NEGATIVE")
else: 
    print(total)
    
    
    
##Question 03: 

a = 10 
b=20
c= 30 

avg= (a+b+c)/3
print("avg = {}".format(avg))


if (avg >a and avg >b and avg>c) or (avg >a and avg >b): 
    print("avg is higher than a,b,c")
elif (avg >a and avg>c): 
    print("avg is higher than a,c")
elif (avg >b and avg>c):
    print("avg is higher than b,c")
elif (avg > a):
    print("avg is higher than a")
elif (avg >b):
    print("avg is higher than b")
elif (avg >c):
    print("avg is higher than c")
    
    
    
##Question 04: 

while True: 
    number = int(input("Enter the number: "))  
    if number >= 0: 
        print("Good Going")
        
    else: 
        print("It's Over")
        break
        
        
##Question 05: 

for x in range(2000,3201): 
    if x%7==0 and x%5 == 1: 
        print(x, end=', ')
        
        
### Question 06:

## (A)
x=123
for i in x:
    print(i)
    # Output: TypeError: 'int' object is not iterable 

## Question 06: b 
# 0
# error
# 1
# error
# 2

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")
        
        
  ##Question 06: c

# 0
# 1
# 2
# 3
# 4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
        
 # Question 07: 

for x in range(0,7):
    if x != 3 and x!=6: 
        print(x)
    else: 
        continue
        
        
## Question 08:

user_input = input("Enter a string: ")
digits = letters = 0

for i in user_input: 
    if i.isdigit():
        digits +=1
    elif i.isalpha():
        letters+=1
print("Digits count: ", digits)
print("Letters count: ", letters)



## Question 09: 
# Write a program such that it asks users to “guess the lucky number”. If the correct number isguessed the program stops, otherwise it continues forever.

lucky_numbers = [28,19,100, 6, 10, 56, 33, 89, 45]


while True: 
    number = int(input("guess the lucky number: "))  
    if number not in lucky_numbers: 
        number = int(input("guess the lucky number: "))  
        
         
    else:
        print("VOLA! you have a gift awiated at the door")
        break 

###Part b:
# Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)

while True: 
    number = int(input("guess the lucky number: "))  
    if number not in lucky_numbers: 
        answer = input("do you want to continue guessing (Yes/No): ") 
        if answer in ["Yes","yes","y","Y"]:
            continue
        else: 
            break
    else:
        print("VOLA! you have a gift awiated at the door")
        break

## Question 10: 

# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as



Counter = 5 

lucky_numbers = [28,19,100, 6, 10, 56, 33, 89, 45]

while Counter<=5: 
    number = int(input("guess the lucky number: "))  
    if number not in lucky_numbers: 
        print("Try Again!")
        Counter -= 1
        if Counter ==0: 
            print("Game Over")
            break

    else:
        print("Good Guess")
        
        
   ##Question 11: 

Counter = 5 

lucky_numbers = [28,19,100, 6, 10, 56, 33, 89, 45]

while Counter<=5: 
    number = int(input("guess the lucky number: "))  
    if number not in lucky_numbers: 
        print("Try Again!")
        Counter -= 1
        if Counter ==0: 
            print("Game Over")
            break

    else:
        print("Good Guess")


  
