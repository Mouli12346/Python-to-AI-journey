#Lession 1: Lists
# A list sotes multiple values at one place

#List of strings(text)
Fruits = ["Apple","Banana","oranges","grapes","Watermelon"]

#List of numbers
Marks = [23,67,87,98,25]

#List of mixed values
Person = ["Mouli", 32, "Swapnil", 36]

#empty lists(we will add things later)
empty_lists = []

#print the lists
print(Fruits)
print(Marks)
print(Person)
print(empty_lists)
print()

#Accessing items using Index
Fruits = ["Apple","Banana","oranges","grapes","Watermelon"]

print(Fruits[0]) #print 1st item - Apple
print(Fruits[1]) #print 2nd item - Banana
print(Fruits[2]) #print 3rd item - oranges
print(Fruits[3]) #print 4th item - Grapes
print(Fruits[4]) #print 5th item - watermelon
print()
#negative index
print(Fruits[-1]) #last item - watermeln
print(Fruits[-2]) #2nd last from end - Grapes
print(Fruits[-3]) #3rd last from end - oranges
print(Fruits[-4]) #4th last from end - Banana
print(Fruits[-5]) #5th last from end - Apple
print()

#len means length of the list, here it is 5(how many items are there in the list)
print(len(Fruits))
print()

#start with empty list
shopping = []
print ("start:", shopping)

#add items one by one using append
shopping.append("milk")
print("After adding milk:",shopping)

shopping.append("Bread")
print("After adding Bread:", shopping)

shopping.append("Eggs")
print("After adding Eggs:", shopping)

print(shopping)
print()

#Remove items using remove
shopping.remove("Bread")
print("After removing Bread:", shopping)
print()

#Add item in specific position using insert
shopping.insert(0,"Butter")  #adding butter in the 1st position
print("After adding Butter in 0 position", shopping)

shopping.insert(8,"tomato")
print("After adding tomato at 8th position",shopping)
shopping.insert(2,"Corn")
print("After adding Corn in 2nd postion",shopping)
print(len(shopping))
print()

#Remove last item using Pop
#last_item saved the removed item so that if we want we can use it anytime
last_item = shopping.pop()
print("Removed last item:",last_item)
print("List after Pop:",shopping)
print()

#Loop through lists
fruits = ["Apple","Banana","Oranges","Grapes"]
print("----Simple Loop----")
for fruit in fruits:
  print("I like:",fruit)
  print()

  #Loop with index number
  print("----using index number----")
  for i in range(len(fruits)):
    print(i,"-",fruits[i])
    
print()

#check if the item is in the list
print("---check if the item exists-----")
if "Mango" not in fruits:
  print("No, Mango is not in the list")

if "Apple" in fruits:
  print("Yes, Apple is in the list")
