from questions import Question
from questions import normal_questions as questions


for qs in questions:
    if (qs.m != None):
        print(f"{qs.q}?")
        for option in qs.m:
            print(option)
        userInput = input() 
    else:
        print(f"{qs.q}?")
        userInput = input()

    if (userInput.lower() == qs.a.lower()):
        print("That is correct!")
    else:
        print(f"Sorry, the correct answer is {qs.a}.")