#Day2 - Dictionaries
# Dictionaries stores information with a lables(keys)

#Customer record
Customer = {
    "name" : "Rahul Sharma",
    "Phone Number" : "9876543219",
    "Age" : "34",
    "Salary" : "20000",

}
print(Customer)
print()

#simple dictionary
Person = {
    "name" : "Mouli",
    "Age" : "32",
    "Salary" : "100000"
}
print(Person)
print()

#Accessing Dictionary 
#In list we use Index Number and In Dictionaries we use Keyname to access the values

Customer = {
    "name" : "Rahul Sharma",
    "Phone Number" : "9876543219",
    "Age" : "34",
    "Salary" : "20000",

}
#Access values using keyname
print(Customer["name"])
print(Customer["Phone Number"])
print(Customer["Age"])
print(Customer["Salary"])
print()

#Safe way to access(No error if key is missing)
print(Customer.get("name"))
print(Customer.get("Age"))
print(Customer.get("email"))
print(Customer.get("email not provided"))

#adding and updating dictonary
customer = {
    "name" : "Mouli Das",
    "Age" : "32",
}
print("Original:",customer)

#Adding values
customer["City"] = "Delhi"
print("After adding City:", customer)
print()

#Updating existing customer
customer["Age"] = "31"
print("After updating Age:",customer)
print()

#Deleting values
del customer["Age"]
print("After deleting the Age:",customer)
print()

#Check if key is exists
if "name" in customer:
    print("name is there:",customer["name"])

if "email" not in customer:
    print("Email does not exist")
    print()

#Loopng through dictonaries
Customer1 = {
    "name" : "Mouli Das",
    "Age" : "32",
    "Phonenumber" : "9878987856",
    "issue" : "Refund Request",
}

#Loops through keys only
print("---keys only---")
for key in Customer1:
    print(key)

print()

#Looping thorugh values
print("---values only----")
for value in Customer.values():
    print(value)

print()

#Print both keys and values
print("---both Keys and Values---")
for key, value in Customer1.items():
    print(key, "-", value)
    
print()
#Multiple customer records
#This is how AI agents stores conversation history
Customers = [
{
    "Name" : "Priya",
    "Age" : "21",
    "City" : "Delhi",
    "resolved": True
},
{
    "Name" : "Riya",
    "Age" : "25",
    "City" : "Noida",
    "resolved": False
},
{
    "Name" : "Deep",
    "Age" : "31",
    "City" : "Mumbai",
    "resolved": True
}
]
#Access 1st customer
print(Customers[0])
print(Customers[0]["Name"])
print(Customers[2])
print(Customers[2]["Name"])
print()

#Loop through all customers
for customer in Customers:
    print("name:",customer["Name"])
    print("age:",customer["Age"])
    print("issue:",customer["resolved"])
    print()

#Find Unresloved issue
print("---unresolved issue---")
for customer in Customers:
    if customer["resolved"] == False:
        print(customer["Name"], "has not resolved" , customer["Age"])
    

