#day 1 mini project
#customer chatbot
print()
print("=" *40)
print("Welcome to Support Bot")
print("=" *40)
print()

name = input("What is your name?")
print()
print("Hello", name , "How can I help you today?")
print()

#Show menu
print("Please choose an option")
print("1. Check order status")
print("2. Request Refund")
print("3. Talk to Human Agent")
print("4. Exit")
print()

choice = input("Please choose an option(1/2/3/4):")

if choice == "1":
  Order_ID = input("Please enter your order Id:")
  print("checking order", Order_ID, "....")
  print("Your order is currently being proceesed")
  print("Expected delivery: 3-5 business days")

elif choice == "2":
  Order_ID = input("Please enter your order Id for Refund:")
  Reason = input("Reason for refund:")
  print("Refund request submitted for your order", Order_ID)
  print("Reason noted:", Reason)
  print("Refund will be processed within 5-7 days")

elif choice == "3":
  print("Connectiong you to a Real Human Agent:")
  print("Please wait! It will take upto 5 to 7 minutes.")

elif choice == "4":
  print("Thank you for contacting us.", name)
  print("Have a great day!")

else:
  print("Invalid choice. Please choose options: 1,2,3, or 4")

print()
print("Thank you for using Support Bot!")