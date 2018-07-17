#!/usr/bin/python2

x=input("press 1 for addition, press 2 to print hello world, press 3 to check whether a number is prime or not, press 4 for calculator, press 5 to find factorial of a number ")


if x==1:
	a=input("enter first number: ")
	b=input("enter second number: ")
	c=a+b
	print ("sum is ",c)

if x==2:
	print("Hello World")
if x==3:
	num=int(input("enter a number to check whether its prime or not"))
		
	if num > 1:
       
		for i in range(2,num):
			if (num % i) == 0:
				print(num,"is not a prime number")
			else:
       				print(num,"is a prime number")
       

	else:
   		print(num,"is not a prime number")
if x==4:

	print("CALCULATOR")

	def add(x, y):
   		return x + y


	def subtract(x, y):
   		return x - y


	def multiply(x, y):
  		return x * y


	def divide(x, y):
   		return x / y

	print("Select operation.")
	print("1.Add")
	print("2.Subtract")
	print("3.Multiply")
	print("4.Divide")


	choice = int(input("Enter choice(1/2/3/4):"))

	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))

	if choice == '1':
   		print(num1,"+",num2,"=", add(num1,num2))
		

	elif choice == '2':
  		print(num1,"-",num2,"=", subtract(num1,num2))

	elif choice == '3':
   		print(num1,"*",num2,"=", multiply(num1,num2))

	elif choice == '4':
   		print(num1,"/",num2,"=", divide(num1,num2))
	else: 
		print "invalid input"

if x==5:

	num = int(input("Enter a number: "))

	factorial = 1


	if num < 0:
   		print("Sorry, factorial does not exist for negative numbers")
	elif num == 0:
   		print("The factorial of 0 is 1")
	else:
   		for i in range(1,num + 1):
       			factorial = factorial*i
   		print("The factorial of",num,"is",factorial) 									
