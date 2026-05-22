# Lession 1: Python calculator
# anything after # is a comment. Python ignores it.
# comments are notes for human not computer.

print (2+3)    #addition
print (10-4)   # substraction
print (6*4)    # multiplication
print (10/2)   # Division
print (10**3)  # 10 to the power 2
print (17 % 5)  # remainder
print()         #add empty line
print("=" * 30) #print ============
print("Lession 2 - Vriables") #print the text
print("=" *30)
print()         #agin add empty line



#Lession 2: Variables
# A variable stores a value with a name
#Use ,  →  almost always, works with everything
#Use +  →  only when you want no space between words and everything is text only

Name = 'Rahul'  # Storing text (called string)
Age = 25        # Storing number (called interger)
Salary = 100000.00 # Storing decimal points (called Float)
is_working = True   # Storing True or False (called Boolean)

print(Name)
print(Age)
print(Salary)
print(is_working)

#You can combine variables with text
print("My name is", Name)
print ("I am", Age, "years old" )
print()         #add empty line
print("=" * 30) #print ============
print("Lession 3") #print the text
print("=" *30)
print()         #agin add empty line

#Lession 3 : taking inputs from users

user_name = input("what is your name?")
user_city = input("where are you from?")

print("Hello", user_name, "from", user_city)
print("welcome to pythong programming!")
print()         #add empty line
print("=" * 30) #print ============
print("Lession 3") #print the text
print("=" *30)
print()       

# lession 4: use of If/Else or making dicisions

age = int(input("what is your age: "))

if  age >= 18:
  print("You are an Adult.")
  print(" You can Vote.")
else:
  print("You are not an Adult.")
  print("You cannot Vote.")
print("This line always works")
print()         #add empty line
print("=" * 30) #print ============
print("Lession 4") #print the text
print("=" *30)
print() 

#Lession 4 : if/elif/else

marks = int(input("Enter your marks out of 100: "))

if marks >= 90:
  print("Grade A : Execellent!")
elif marks >= 75:
  print("Grade B: Good")
elif marks >=60:
  print("Grade C :Average")
elif marks >= 40:
  print("Grade D : Below Average")
else:
  print ("Grade F : Failed")

print()         #add empty line
print("=" * 30) #print ============
print("Lession 4") #print the text
print("=" *30)
print()

#Lession 5 : Loops, while loops
#For Loop : Repeat a fixed number of times

print("---For Loop---")
for i in range(5):
  print("This is the line number", i)

print()         #add empty line
print("=" * 30) #print ============
print("Lession 4") #print the text
print("=" *30)
print()

#Lession 6 : while Loop : repeat until condition is false

print("---while loop---")
count = 1
while count <= 5:
  print("count is:", count)
  count = count+1
  print()         #add empty line
print("=" * 30) #print ============
print("Lession 4") #print the text
print("=" *30)
print()

#Lession 7 : Loop with a List

print("---Loop throgh a List")
fruits = ["Apple", "Orange","Grapes","Banana","Kiwi"]
for fruit in fruits:
  print("I like", fruit)




