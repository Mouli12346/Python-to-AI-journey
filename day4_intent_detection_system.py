#this is what every AI agent does before responding
#clean the message first
def user_intent(user_message):
    message = user_message.strip().lower()

#Chcek for different intents
    if any(word in message for word in ["refund", "money back", "return"]):
        return "refund_request"
    
    elif any(word in message for word in ["order", "delivery", "track", "status"]):
        return "order_inquiry"
    
    elif any(word in message for word in ["password", "login", "account", "access"]):
        return "account_issue"
    
    elif any(word in message for word in ["hello", "hi", "hey", "good morning"]):
        return "greeting"

    elif any(word in message for word in ["bye", "goodbye", "thank you", "thanks"]):
        return "farewell"
    else:
        return "unknown"

def respond_to_intent(intent, name="customer"):
    if intent == "refund request":
        return f"Hello {name}! I understand you want a refund. Let me help you with that."
    elif intent == "order_inquiry":
        return f"Hello {name}! Let me check your order status right away."

    elif intent == "account_issue":
        return f"Hello {name}! I will help you with your account issue."

    elif intent == "greeting":
        return f"Hello {name}! Welcome. How can I help you today?"

    elif intent == "farewell":
        return f"Thank you {name}! Have a wonderful day. Goodbye!"

    else:
        return f"I am sorry {name}, I did not understand. Can you please rephrase?"
    
#Test it
test_messages =  [
    "Hi there!",
    "I want my money back",
    "Where is my order?",
    "I cannot login to my account",
    "Thank you for your help",
    "What is the meaning of life?"
]

print("=== Intent Detection System ===")
print()
for message in test_messages:
    intent = user_intent(message)
    response = respond_to_intent(intent, "Rahul")
    print(f"User: {message}")
    print(f"Intent detected: {intent}")
    print(f"Agent: {response}")
    print()