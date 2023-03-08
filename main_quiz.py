from questions import Question

score = 0  
#welcome statement
print("Welcome to the quiz of the day!")
name = input("What is your name?\n")
print("Hi " + name)
test = 0
while test == 0:
    difficulty = input("Please select your difficulty:\n Normal (n)\n Hard (h)\n").lower()

    if difficulty == "n" or difficulty == "normal":
        from questions import normal_questions as questions
        test += 1
    elif difficulty == "h" or difficulty == "hard":
        from questions import hard_questions as questions
        test += 1
    else:
        print("No valid difficulty selected")
    
for q in questions:
    if (q.m != None):
        print(f"{q.q}?")
        for option in q.m:
            print(option)
        userInput = input() 
    else:
        print(f"{q.q}?")
        userInput = input()

    if (userInput.lower() == q.a.lower()):
        print("That is correct!")
        if difficulty == "n":
            score += 10
        else:
            score += 15
    else:
        print(f"Sorry, the correct answer is {q.a}.")

print("That is the end of the quiz. \nYour score is: " + str(score))

new_player = [str(score), ":", name, ","]
scores_file = open("scores.txt", "a")
scores_file.writelines(new_player)
scores_file.close()

scores_file = open("scores.txt")
list_file = list(scores_file)
split_file = []
for item in list_file:
    split_file.append(item.split(","))

last_lits = []
for i in split_file:
    for l in i:
        last_lits.append(l.split(":"))

for item in sorted(last_lits, reverse=True):
    if score > int(item[0]):
        print("Congratulations {}! You have reached the Top 5!".format(name))
        break

print("The leaderboard is as follows;")

top_5 = 0
for item in sorted(last_lits, reverse=True):
    if top_5 < 5: 
        top_5 += 1
        print(str(top_5) + ". " + item[1].title() + " with a score of " + item[0])
    else:
        break

scores_file.close()


#try and make classes of everything. Like the scoreboard, 
