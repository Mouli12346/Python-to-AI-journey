#defining a function(creating procedures)

def greet():
    print("Hello!")
    print("Welcome to customer Support.")
    print("How can I help you today?")

#Calling the function
greet()
print()
greet()
greet()
greet()

print()

#Functions with input
def greet_customer(name):
    print("Hello!",name)
    print("Welcome to the Customer Support")
    print("How can I help you today,",name,"?")

greet_customer("Rahul")
print()
greet_customer("Priya")
print()
greet_customer("Sahil")
print()

#Function without a return
def add_number(a,b):
    result = a+b
    print("Result:",result)      #It only prints the result, you can not use "result anywhere else."
add_number(10,5)
print()

#Function with return
def add_numbers_v2(a,b):
    result = a + b
    return(result)
answer = add_numbers_v2(10,5)
print("The answer is:", answer)
print("Double the answer:",answer*2)
print("Add 100 to the answer:",answer+ 100)

print()

#Make a real time refund calculator
def calculate_refund(original_price, days_after_purchase):
    if days_after_purchase <=7:
        refund = original_price  #full refund
    elif days_after_purchase <=30:
        refund = original_price * 0.5   #half refund
    else:
        refund = 0   #no refund
    return refund

amount = calculate_refund(1000, 5)
print("The refund amount is: ", amount)
print()

amount = calculate_refund(1000, 27)
print("The refund amount is: ",amount)
print()
amount = calculate_refund(1000, 31)
print("The refund amount is: ",amount)
print()

#Default values in function
def greet_people(name, language = "English"):
    if language == "English":
        print("Hello",name,"Welcome to the Customer Support!")
    elif language == "Hindi":
        print("Namaste", name, "Aapka swagat hai!")
    else:
        print("Hello", name)

#call without language, use default language
greet_people("Rahul")

#call with language specified
greet_people("Rahul","English")
greet_people("Priya","Hindi")

#Function 1: check_order_status(order_id)
def check_order_status(order_id):
    if order_id.startswith("ORD"):
        print("Valid order found", order_id)
    else:
        print("Order Id not found")

check_order_status("ORD1234556")
check_order_status("768668998")
print()

#Function 2: calculate_wait_time(queue_position)
def calculate_wait_time(queue_position):
    wait_time = queue_position * 3
    return wait_time

result = calculate_wait_time(15)
print("The total wait time is", result, "minutes")
print()

#Function 3: is_vip_customer(total_purchases)
def is_vip_customer(total_purchases):
    if total_purchases > 10000:
       return True
    else:
        return False

Result = is_vip_customer(5000)
print("Is VIP cuatomer:", Result)
Result = is_vip_customer(1200000)
print("Is VIP cuatomer:", Result)
    
print()

#organizing code with functions
def show_header():
    print("=" * 40)
    print("---Customer Record System---")
    print("=" * 40)
    print()

def show_menu():
    print("What do you want to do?")
    print("1. Add new customer")
    print("2. View all customers")
    print("3. Search customer by name")
    print("4. Exit")
    print()

def add_customer(customer):
    name = input("Customer name: ")
    phone = input("Phone number: ")
    issue = input("Customer issue: ")

    new_customer = {
        "name": name,
        "phone": phone,
        "issue": issue,
        "resolved": False
    }
    customers.append(new_customer)
    print("Customer added successfully!")
    print()
    return customers
def view_customer(customer):
    if len(customers) == 0:
        print("No customers yet.")
    else:
        print("--- All Customers ---")
        for i, customer in enumerate(customers):
            print(i + 1, ".", customer["name"])
            print("   Phone:", customer["phone"])
            print("   Issue:", customer["issue"])
            print("   Resolved:", customer["resolved"])
            print()

def search_customer(customer):
    search = input("Search by customer name: ")
    found = False

    for customer in customers:
        if search.lower() in customer["name"].lower():
            print("Found!")
            print("Name:", customer["name"])
            print("Phone:", customer["phone"])
            print("Issue:", customer["issue"])
            found = True
        if not found:
         print("No customer found with this name.")
    print()

# MAIN PROGRAM
# Now the main code is clean and readable
customers = []
show_header()

while True:
    show_menu()
    choice = input("Enter the choice (1/2/3/4): ")
    print()

    if choice == "1":
        customers = add_customer(customers)
    elif choice == "2":
        view_customer(customers)
    elif choice == "3":
        search_customer(customers)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3 or 4")
        print()

#Function calling other functions
def get_customer_name():
    return input ("Enter the customer name:")

def get_customer_issue():
    return input("Enter customer issue")

def create_ticket(name, issue):
    ticket = {
        "id" : "TKT" + str(len(name)),
        "name" : name,
        "issue" : issue,
        "status" : "open"
    }
    return ticket

def print_ticket(ticket):
    print("=" * 30)
    print("TICKET CREATED")
    print("ID:", ticket["id"])
    print("Customer:", ticket["name"])
    print("Issue:", ticket["issue"])
    print("Status:", ticket["status"])
    print("=" * 30)

    def handle_new_complaint():
    # This function calls all other functions
      name = get_customer_name()      # calls function 1
      issue = get_customer_issue()    # calls function 2
      ticket = create_ticket(name, issue)  # calls function 3
      print_ticket(ticket)            # calls function 4
    return ticket
# Run the whole process with one line
    handle_new_complaint()