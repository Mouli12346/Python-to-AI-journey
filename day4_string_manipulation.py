#finding things inside sentences
sentence = "I want to request a refund for my order"

#check if word exists
print("want" in sentence)
print("delivery" in sentence)
print()

#find positions of a word
print(sentence.find("to"))
print(sentence.find("world"))
print()

#count how many times word appears
print(sentence.count("e"))
print(sentence.count("my"))
print(sentence.count("of"))
print()

#check start and end
print(sentence.startswith("I want"))
print(sentence.endswith("order"))
print(sentence.endswith("my"))
print()

#cleaning and replacing text
#dirty user input(common in real life)
user_input = "  I WANT MY REFUND PLEASE!!!  "

#remove extra spaces
cleaned = user_input.strip()
print("After cleaning:",cleaned)
print()

#make it in lower case
cleaned = cleaned.lower()
print("After cleaning:", cleaned)
print()

#remove unwanted character
cleaned = cleaned.replace("!!!","")
print("After replacing:",cleaned)
print()

#replacing words
cleaned = cleaned.replace("I want","Customer wants")
print("After replacing:",cleaned)

#Combing everything together
Final = user_input.strip().lower().replace("!!!",".")
print("Final result:",Final)
print()

#Spliting and Joining
#Split - Breaks text into list
sentence = "I want to know my refund status"

words = sentence.split()
print(words)
print(words[0])
print(words[-1])
print(len(words))
print()

#Split by specific character
person = "Rahul,25,Mumbai"
character = person.split(",")
print(character)
print(character[0])
print(character[2])
print()

#Join
#combine list back to string
Plus = ["I","Love","Mumbai"]
Result = " ".join(Plus)
print(Result)
print()

Show = " ".join(["Mouli","25","Kolkata"])
print(Show)
print()

#String formatting
name = "Rahul"
age = 25
salary = 45000.5678
order_id = "ORD001"
status = "Delivered"

#old way of priniting result
print("Hello",name,"your age is",age)

#New way - F string way
print(f"Hello {name} your age is {age}")
print(f"your oder_id is {order_id} and the status is {status}")
print(f"Your salary is: {salary:.2f}")
print(f"name is Caps: {name.upper()}")
print(f"name is {name} years old {age} and earns {salary:.2f} per month")
print()

# Extract specific information from user messages

def extract_order_id(message):
    words = message.split()
    for word in words:
        if word.startswith("ORD"):
            return word
    return None

def extract_phone_number(message):
    words = message.split()
    for word in words:
        if len(word) == 10 and word.isdigit():
            return word
    return None

def extract_email(message):
    words = message.split()
    for word in words:
        if "@" in word and "." in word:
            return word
    return None

# Test extraction
messages = [
    "I have a problem with order ORD123 please help",
    "My phone number is 9876543210 please call me",
    "Contact me at rahul@gmail.com for more details",
    "I need help with my account"
]

print("=== Information Extraction ===")
print()

for message in messages:
    print(f"Message: {message}")

    order = extract_order_id(message)
    phone = extract_phone_number(message)
    email = extract_email(message)

    if order:
        print(f"Order ID found: {order}")
    if phone:
        print(f"Phone found: {phone}")
    if email:
        print(f"Email found: {email}")
    if not order and not phone and not email:
        print("No specific information found")
    print()

# Validate user inputs before processing

def validate_phone(phone):
    phone = phone.strip()
    if len(phone) == 10 and phone.isdigit():
        return True, "Valid phone number"
    elif len(phone) != 10:
        return False, f"Phone must be 10 digits. You entered {len(phone)} digits"
    else:
        return False, "Phone must contain only numbers"

def validate_order_id(order_id):
    order_id = order_id.strip().upper()
    if order_id.startswith("ORD") and len(order_id) == 6:
        return True, "Valid order ID"
    else:
        return False, "Order ID must start with ORD followed by 3 numbers. Example: ORD123"


def validate_email(email):
    email = email.strip().lower()
    if "@" in email and "." in email:
        return True, "Valid email"
    else:
        return False, "Invalid email. Must contain @ and ."
    
# Test validation
print("=== Input Validation ===")
print()

# Phone tests
phones = ["9876543210", "98765", "987654321a"]
for phone in phones:
    is_valid, message = validate_phone(phone)
    print(f"Phone: {phone}")
    print(f"Valid: {is_valid} — {message}")
    print()

# Order ID tests
orders = ["ORD123", "ABC123", "ORD12"]
for order in orders:
    is_valid, message = validate_order_id(order)
    print(f"Order ID: {order}")
    print(f"Valid: {is_valid} — {message}")
    print()