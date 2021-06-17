# 1. Create a list of 10 elements of four different data types like int, string, complex and float.

mylist =[1,"string", 3+3j, 4.05]

# 2. Create a list of size 5 and execute the slicing structure
mylist = [1,2,3,4,5,6,7]

result = mylist[2:]

# 3. Write a program to get the sum and multiply of all the items in a given list.
from functools import reduce 
import numpy as np
mylist = [1,2,3,4,5,6,7,8,9,10]
result = reduce(lambda x,y: x*y ,mylist)

print("Sum of all items in the given list: ", sum(mylist))
print("Mutiply of all items in the given list: ", result)

# 4. Find the largest and smallest number from a given list.
mylist = [1,2,3,4,5,6,7,8,9,10]
print("Largest number in the given list: ", max(mylist))
print("Smallest number in the given list: ", min(mylist))

# 5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.

mylist = [1,2,3,4,5,6,7,8,9,10]
result = [x for x in mylist if x%2 !=0]

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).
result = [x*x for x in range (0,31)][1:6] + [y*y for y in range (0,31)][-5:]
print(result)

# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]

list1 = list(map(int, input("Enter the list  of numbers: ").split()))
new_list = list(map(int, input("Enter the new list of to be replaced: ").split()))
list1.pop(-1)
list1 +new_list

# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}

n = int(input("Enter the length of dictonary: "))
a = dict(input("Enter the Dictonary_1: ").split() for _ in range(n))
b= dict(input("Enter the Dictonary_2: ").split() for _ in range(n))
a.update(b)
print(a,end= "\n")


# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
n = int(input("Enter the length of dictonary: "))
result =  {x:x**2 for x in range(n)}
result

# 10. Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
user_input = list(map(int,input("Enter the comma-separated list: ").split(",")))

result = [str(x) for x in user_input]
print(result,tuple(user_input))



# Task 04: 

# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”
user_input = input("Enter the string: ")
result = user_input[::-1]


# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
def calling(line):
    lower = [x for x in user_input if x.islower()]
    upper = [x for x in user_input if x.isupper()]
    return "No. of Uppercase characters : {} No. of Lower case Characters : {}". format(len(lower), len(upper))
    
user_input = input("Enter the string: ")
print(calling(user_input))

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
def calling1(mylist):
    return list(set(mylist))
    
users = list(input("Enter the items in list: ").split())
print(calling1(users))

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
users = input("Enter the hyphen-separated sequence of words: ").split("-")
print("-".join(sorted(users)))
    
# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
print(input("Enter the line: ").upper())

# 6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.
def calling_3(num1, num2): 
    return int(num1) +int(num2)
    
result = calling_3 (str(input("Enter the number1: ")), str(input("Enter the number2: ")))
print(result)

# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.
def calling_4(str_1, str_2): 
    if len(str_1) == len(str_2): 
        return (str_1,str_2)
    else: 
        return max(str_1, str_2)
               
max(input_1, input_2)
result = calling_4(input("Enter the string_1: "),input("Enter the string_2: "))
print(result)


# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).
def squares(m,n): 
    return tuple([x**2 for x in range(m,n+1)])

print(squares(1,20),end = "\n")

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def even_odd(limit):     
    for x in range(0,limit): 
        if x%2 ==0: 
            print(x," EVEN")
        else: 
            print(x," ODD")
            
even_odd(3)

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
list_1 = [x for x in range(0,21)]
list(filter(lambda x: x%2 == 0, list_1))

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.
list_1 = [x for x in range(0,21)]
list(map(lambda x:x**2,filter(lambda x: x%2 == 0, list_1)))

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
try: 
    num1 = int(input("Enter the number:"))
    num2 = int(input("Enter the number:"))
    
    ans = num1/num2
    print(ans)
except ZeroDivisionError: 
    print("Enter valid number")

# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce

list_1= [1,2,3,4,5,6,7]

flatten = reduce(lambda x,y: str(x)+""+str(y), list_1)
flatten

# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.
list(filter(lambda x: x%3 != 0 and x%7 == 0, range(0,100)))


# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.
print(list(map(lambda x,y: x*y,range(1,10),range(1,10))),end = "\n")

# 16. What is the output of the following codes:
(i) def foo():
try:
return 1
finally:
return 2
k = foo()
print(k)
## output: 2

(ii) def a():
try:
f(x, 4)
finally:
print('after f')
print('after f?')
a()

#NameError: name 'f' is not defined
##after f
##after f?
