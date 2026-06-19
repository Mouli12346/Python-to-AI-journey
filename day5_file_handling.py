#write to a file
with open("notes.txt", "w") as file:
    file.write("My name is Mouli\n")
    file.write("I am learning python\n")
    file.write("I am from Kolkata\n")

print("File saved!")

#Read from a file

with open("notes.txt", "r") as file:
    content = file.read()      

print(content)

#Add to a existing file without deleting anything
with open("notes.txt", 'a') as file:
    file.write("This new line is added/n")
    print("Line added")

#Read again to verify
with open("notes.txt", 'r') as file:
    content = file.read()

print(content)

#agent saving the conversation

import json
import os

conversation = [
    {"role" : "user", "content" : "Hi"},
    {"role" : "assistant", "content" : "How can I help you?"},
    {"role": "user", "content": "I need a refund"}

    ]

with open("memory.json","w") as file:
    json.dump(conversation, file, indent=4)

print("Memory saved!")

if os.path.exists("memory.json"):
    with open("memory.json","r") as file:
        loaded = json.load(file)
    print("memory loaded!")
for message in loaded:
    print(message["role"],":", message["content"])
else:
    print("No memory file found!")