import json

points = 0

def show_question(question):
    global points
    print(question["pytanie"])
    print("a", question["a"])
    print("b", question["b"])
    print("c", question["c"])
    
    answer = input("Którą odpowiedź wybierasz?")

    if answer == question["odpowiedz"]:
        points += 1
        print("Prawidłowa odpowiedź","Masz", points, "punktów.")
    else:
            print("Nope, prawidłowa odpowedź " + question["odpowiedz"] + ".")

with open("quiz.json") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        show_question(questions[i])

print("Bravo, masz ", points)