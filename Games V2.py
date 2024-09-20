print("Hello there! My name is Game Bot AI (GBAI)")
print("I will be verry happy to play with you!")
print("Let's start!!!")
firstname=input("Please enter your first name:  ")
lastname=input("Please enter your last name:  ")
print("Hello there!", firstname, lastname)
print("Do you want to play a math game?")
print("I will guess the sum of your two numbers!  ")
num1=int(input("Please enter your first number:  "))
num2=int(input("Please enter your second number:  "))
ans=(num1 + num2)
print("Your answer is:", ans)
print("now, can you enter the third number?")
num3=int(input("Please enter your third number:  "))
ans=(num1 + num2)*num3
print("Your answer is:", ans)
print("Now, do you want to play a game named guess the pizza?")
print("How to play: Imagine, your friend bought a pizza and two of you eat it I will guess the slice of pizza that two of you didn't eat!")
num1=int(input("How much slices of pizza do you have?:  "))
num2=int(input("How many slices did you eat?:  "))
num3=int(input("How many slices did your friend eat?:  "))
ans=num1-(num2+num3)
print("The answer is:", ans)
age=int(input("Can you enter your age?:  "))
age1=age+1
print("Next year you will be:", age1)
print("Let's play a game named divide the bill!")
num1=int(input("What is the price of the bill?  "))
num2=int(input("How many meals did they eat?  "))
num3=int(input("how many people did they go with you?  "))
ans=(num1*num2)/num3
print("Each people has to pay:", ans)
print("Let's play how much time there is from the day! Such a loooooong name! Right?")
print("(Just enter a small amount of time or this could be verryyyyy loooooooog!)")
# import the time module 
import time 

# define the countdown func. 
def countdown(t): 
	
	while t: 
		mins, secs = divmod(t, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") 
		time.sleep(1) 
		t -= 1
	
	print('The End!!!') 


# input time in seconds 
t = input("Enter the time in seconds: ") 

# function call 
countdown(int(t)) 
