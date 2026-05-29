
# Day 3 Project
# AI Agent Tool System
# This is the foundation of a real AI agent

# ============ TOOL FUNCTIONS ============
# Each function below is one tool the AI agent can use

def calculate(expression):
    try:
        result = eval(expression)
        return "Result: " + str(result)
    except:
        return "Error: Invalid expression"

def search_web(query):
    # Simulated web search (real one needs API)
    results = {
        "weather delhi": "Sunny, 35 degrees",
        "python tutorial": "python.org has best tutorials",
        "ai agents": "AI agents are autonomous systems that use LLMs"
    }
    query_lower = query.lower()
    if query_lower in results:
        return results[query_lower]
    else:
        return "No results found for: " + query

def check_order(order_id):
    # Simulated order database
    orders = {
        "ORD001": "Delivered on 20th May",
        "ORD002": "Out for delivery",
        "ORD003": "Processing"
    }
    if order_id in orders:
        return "Order " + order_id + ": " + orders[order_id]
    else:
        return "Order not found: " + order_id

def convert_currency(amount, from_currency, to_currency):
    rates = {
        "USD_INR": 83.5,
        "INR_USD": 0.012,
        "EUR_INR": 90.2,
        "INR_EUR": 0.011
    }
    key = from_currency + "_" + to_currency
    if key in rates:
        result = float(amount) * rates[key]
        return str(amount) + " " + from_currency + " = " + str(round(result, 2)) + " " + to_currency
    else:
        return "Currency conversion not supported"

def show_help():
    print("Available commands:")
    print("  calculate [expression]  →  Example: calculate 25 * 4")
    print("  search [query]          →  Example: search weather delhi")
    print("  order [order_id]        →  Example: order ORD001")
    print("  convert [amount] [from] [to]  →  Example: convert 100 USD INR")
    print("  help                    →  Show this menu")
    print("  exit                    →  Exit the program")
    print()

# ============ MAIN AGENT ============
def run_agent():
    print("=" * 40)
    print("      AI Agent Assistant")
    print("=" * 40)
    print("Type 'help' to see what I can do")
    print()

    while True:
        user_input = input("You: ").strip()
        print()

        if user_input.lower() == "exit":
            print("Agent: Goodbye! Have a great day!")
            break

        elif user_input.lower() == "help":
            show_help()

        elif user_input.lower().startswith("calculate"):
            expression = user_input[9:].strip()
            result = calculate(expression)
            print("Agent:", result)

        elif user_input.lower().startswith("search"):
            query = user_input[6:].strip()
            result = search_web(query)
            print("Agent:", result)

        elif user_input.lower().startswith("order"):
            order_id = user_input[5:].strip()
            result = check_order(order_id)
            print("Agent:", result)

        elif user_input.lower().startswith("convert"):
            parts = user_input.split()
            if len(parts) == 4:
                result = convert_currency(parts[1], parts[2], parts[3])
                print("Agent:", result)
            else:
                print("Agent: Please use format: convert 100 USD INR")

        else:
            print("Agent: I do not understand that command.")
            print("Agent: Type 'help' to see what I can do.")

        print()

# Start the agent
run_agent()