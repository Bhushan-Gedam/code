"""
# only if 
if condition1 :
   executes when the condition1 is true

# if else 
if condition1 :
   executes when the condition1 is true
else :
   executes when the condition1 is false
   
#if elif else ladder   
if condition1 :
   executes when the condition1 is true
elif condition2 :
   executes when the condition2 is true and condition1 is false
else :
   executes when the both condition1 and condition2 is false

"""  
''''
# demo

# if 
weather = "cold"
if weather == "cold":
	print(" I am having  green tea")

# if else
weather = "cold"
if weather == "cold":
	print(" I am having  green tea")
else:
	print(" I am having  water")
 
# if else if ladder
weather = "cold"
personal_preference = "Hot"
if weather == "Sunny":
	print(" I am having  cold coffee")
elif weather == "raining":
	print(" I am having  hot tea")
elif weather == "cold":
	print(" I am having  green tea")
else:
	print(" I am having  water")

print(" Thank you !")

'''


# nesting the if else if ladder
# weather = "cold"
# personal_preference = "Hot"

# if weather == "Sunny":
# 	if personal_preference == "Hot":
# 		print(" I am having  Hot coffee")
# 	else:
# 		print(" I am having  cold coffee")	
# elif weather == "raining":
# 	if personal_preference == "Hot":
# 		print(" I am having  hot tea")
# 	else:
# 		print(" I am having  cold tea")
# elif weather == "cold":
# 	if personal_preference == "Hot":
# 		print(" I am having  hot green tea")
# 	else:
# 		print(" I am having  cold green tea")
# else:
# 	if personal_preference == "Hot":
# 		print(" I am having  hot water")
# 	else:
# 		print(" I am having  cold water")
	

# print(" Thank you !")


"""
if the number is divisible by 3 print Fizz    
if the number is divisible by 5 print Buzz
if the number is divisible by 3 and also divisible by 5 print Fizz Buzz

Testcase : 
    21 --> Fizz
    50 --> Buzz
    15 --> Fizz Buzz
    22 --> Invalid Input 
"""
    
    # else:
        
  
    

# num =int(input("Enter the number"))
# if (num%5==0):
#     if (num%3==0):
#         print("Fizz BUzz")
#     else:
#         print("Buzz")
# elif (num%3==0):
#     print("Fizz")  
# else:
#     print("Invalid input")

# num=1
# while(num<10):
#     if(num<6):
#         print(num,end = " \n")
#     continue
#     num+=1
#     print(num,end=" ")


# while(True):
#     val = int(input('What operation do you want to do?\n 1. Addition\n 2. Square\n 3. Exponenation\n 4. Exit\n'))
#     if val == 4:
#         break
#     if val == 1:
#         num1 = int(input('Enter the first number: '))
#         num2 = int(input('Enter the second number: '))
#         print(num1+num2)
        
#     elif val == 2:
#         num1 = int(input('Enter the number which you want to square: '))
#         print(num1*num1)
#     elif val == 3:
#         num1 = int(input('Enter a number: '))
#         num2 = int(input('Enter the exponential power: '))
#         print(num1 ** num2)
#     else:
#         print('Enter valid option!!!')

# Solve the following using either while/do while loops
# 1) Take a number from the user and print sum from 1 to that number for eg: 10 o/p : 55
# 2) Take a number from the user and print all Odd numbers from 1 to that number  eg : 10 o/p 1 3 5 7 9
# 3) Take a number from the user and print all Even numbers from 1 to that number eg : 10 2 4 6 8 10

# num = int(input('Enter any number: '))

# sum = 0

# for i in range(1,num+1):
#     sum = sum + i
    
#     print(f'The adittion of the numbers from 1 to {num} is: {sum}')




# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# num = int(input('Enter any number: '))
# sum = 0
# for i in range(1,num+1):
#     if (i%2==0):
#         print(i)
    
 
# --------------------------------------------------------------------------------

num = int(input('Enter any number: '))
sum = 0
for i in range(1,num+1):
    if (i%2!=0):
        print(i)    
    
    

        
        
        
        
        
        
        
    