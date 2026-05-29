# Day 4 Project
# Smart Customer Support System
# Uses string processing to understand customers

# ===== VALIDATION FUNCTIONS =====
def validate_phone(phone):
    phone = phone.strip()
    if len(phone) == 10 and phone.isdigit():
        return True
    return False

def validate_order_id(order_id):
    order_id = order_id.strip().upper()
    if order_id.startswith("ORD") and len(order_id) == 6:
        return True
    return False

# ===== INTENT DETECTION =====
def detect_intent(message):
    message = message.lower().strip()

    if any(word in message for word in ["refund", "money back", "return", "cancel"]):
        return "refund"
    elif any(word in message for word in ["order", "delivery", "track", "where", "status"]):
        return "order"
    elif any(word in message for word in ["hello", "hi", "hey", "help"]):
        return "greeting"
    elif any(word in message for word in ["bye", "goodbye", "thank"]):
        return "farewell"
    else:
        return "unknown"

# ===== RESPONSE FUNCTIONS =====
def handle_greeting(name):
    return f"Hello {name}! Welcome to Customer Support. How can I help you today?"

def handle_refund(name):
    print(f"I understand you want a refund, {name}.")
    order_id = input("Please provide your order ID: ").strip().upper()

    if validate_order_id(order_id):
        print(f"Order {order_id} found.")
        print(f"Refund request for {order_id} has been submitted.")
        print("You will receive your refund in 5-7 business days.")
    else:
        print("Invalid order ID. Must be like ORD123.")
    print()

def handle_order(name):
    print(f"Let me help you track your order, {name}.")
    order_id = input("Please provide your order ID: ").strip().upper()

    orders = {
        "ORD001": "Delivered on 20th May",
        "ORD002": "Out for delivery — arriving today",
        "ORD003": "Processing — will ship in 2 days"
    }

    if validate_order_id(order_id):
        if order_id in orders:
            print(f"Order {order_id}: {orders[order_id]}")
        else:
            print(f"Order {order_id} not found in our system.")
    else:
        print("Invalid order ID format.")
    print()

def handle_farewell(name):
    return f"Thank you for contacting us, {name}! Have a wonderful day. Goodbye!"

def handle_unknown(name):
    return f"I am sorry {name}, I did not understand that. Can you please rephrase?"

# ===== MAIN SUPPORT SYSTEM =====
def run_support():
    print("=" * 45)
    print("     Smart Customer Support System")
    print("=" * 45)
    print()

    # Get customer details
    name = input("Welcome! What is your name? ").strip()
    phone = input(f"Hello {name}! Please enter your phone number: ").strip()

    if not validate_phone(phone):
        print("Invalid phone number. Must be 10 digits.")
        print("Please call again with correct number.")
        return

    print(f"\nThank you {name}! Your phone {phone} is verified.")
    print("You can now ask me anything.\n")

    while True:
        user_message = input(f"{name}: ").strip()
        print()

        if not user_message:
            print("Please type something.\n")
            continue

        intent = detect_intent(user_message)

        if intent == "greeting":
            print(f"Agent: {handle_greeting(name)}\n")

        elif intent == "refund":
            handle_refund(name)

        elif intent == "order":
            handle_order(name)

        elif intent == "farewell":
            print(f"Agent: {handle_farewell(name)}\n")
            break

        else:
            print(f"Agent: {handle_unknown(name)}\n")

# Start the system
run_support()