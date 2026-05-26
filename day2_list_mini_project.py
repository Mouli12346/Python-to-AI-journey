#creating my own project
skills = ["SQL","Python","Power Bi","Excel"]
#Prints the total number of skills
print(len(skills))
#Prints your first skill
print(skills[0])
#Prints your last skill
print(skills[-1])
print(skills[-2])
#Adds "AI Agents" to the list using append
#Prints the updated list
skills.append("AI agent")
print("After adding AI agent:",skills)
#Loops through and prints each skill with "I know:" before it
for i in range(len(skills)):
    print("I know:",skills[i])