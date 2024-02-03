#PART 3
progression_count = {"progress":0, "trailer":0, "retriever":0, "excluded":0}
from graphics import *
file_path = "credits_data.txt"

def save_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(','.join(map(str, data)))

def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = list(map(int, file.read().split(',')))
        return data
    except FileNotFoundError:
        return None

def func():
    while True:
        pass_credits = get_integer_input("Please enter your credits at pass: ")

        defer_credits = get_integer_input("Please enter your credits at defer: ")

        fail_credits = get_integer_input("Please enter your credits at fail: ")

        if (check_total(pass_credits, defer_credits, fail_credits)):
            save_to_file(file_path, [pass_credits, defer_credits, fail_credits])
            stored_data = read_from_file(file_path)
            if stored_data:
                pass_credits, defer_credits, fail_credits = stored_data
                result = outcome(pass_credits, defer_credits, fail_credits)
                print(result, "-", pass_credits, ",", defer_credits, ",", fail_credits)
            else:
                print("No data found in the file.")
            break
        else:
            print("Total incorrect")

def get_integer_input(inp):
    while True:
        try:
            user_input = int(input(inp))
            credit_range = [0,20,40,60,80,100,120]
            if user_input not in credit_range:
                print("Out of range")
            else:
                return user_input
        except ValueError:
            print("Integer required. Please enter a valid integer.")

def check_total(a,b,c):
    if (a + b + c) != 120:
        return 0
    else:
        return 1

def outcome(pass_credits, defer_credits, fail_credits):
    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
        progression_count["progress"] += 1
        return "Progress"
    elif pass_credits == 100:
        progression_count["trailer"] += 1
        return "Progress (Module Trailer)"
    elif fail_credits >= 80:
        progression_count["excluded"] += 1
        return "Exclude"
    else:
        progression_count["retriever"] += 1
        return "Do not progress - module retriever"

def draw_histogram(data):
    win = GraphWin("Histogram", 600, 600)

    max_value = max(data.values())

    bar_width = 80
    x = 50
    for progression, count in data.items():
        bar_height = (count / max_value) * 200

        bar = Rectangle(Point(x, 250), Point(x + bar_width, 250 - bar_height))
        bar.setFill("blue")
        bar.draw(win)

        label = Text(Point(x + bar_width / 2, 260), progression)
        label.draw(win)

        x += bar_width + 20

    win.getMouse()
    win.close()

while True:
    func()
    print("Would you like to enter another set of data?")
    user_choice = input("Enter 'y' for yes or 'q' to quit and view results: ")
    if user_choice == "q":
        draw_histogram(progression_count)
        break

