print("=" * 40)
print("---Customer Record System---")
print("=" * 40)
print()

# Store all customers in a list of dictionaries
customers = []

# Keep running until user exits
while True:
    print("What do you want to do?")
    print("1. Add new customer")
    print("2. View all customers")
    print("3. Search customer by name")
    print("4. Exit")
    print()

    choice = input("Enter the choice (1/2/3/4): ")
    print()

    if choice == "1":
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
        print("New customer added successfully!")
        print()

    elif choice == "2":
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

    elif choice == "3":
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

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3 or 4")
        print()