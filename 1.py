#PART 1:
progression_count = {"progress":0, "trailer":0, "retriever":0, "excluded":0}
from graphics import *

def func():
    global pass_credits
    global defer_credits
    global fail_credits
    while True:
        pass_credits = get_integer_input("Please enter your credits at pass: ")

        defer_credits = get_integer_input("Please enter your credits at defer: ")

        fail_credits = get_integer_input("Please enter your credits at fail: ")

        if (check_total(pass_credits, defer_credits, fail_credits)):
            break
        else:
            print("Total incorrect")

    print(outcome(pass_credits, defer_credits, fail_credits))

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
        return("Progress")

    elif pass_credits == 100:
        progression_count["trailer"] += 1
        return("Progress (Module Trailer)")
        
    elif fail_credits >= 80:
        progression_count["excluded"] += 1
        return("Exclude")
        
    else:
        progression_count["retriever"] += 1
        return("Do not progress - module retriever")
        

# HISTOGRAM
def draw_histogram(data):
    max_value = max(data.values())

    colors = ["#aef8a1", "#a0c689", "#a7bc77", "#d2b6b5"]

    bar_width = 80
    gap = 20 
    x = 50
    total_bars = len(data)

    window_width = max(600, (bar_width + gap) * total_bars + 100)
    win = GraphWin("Histogram", window_width, 600)

    title = Text(Point(window_width / 2, 20), "Histogram Results")
    title.setSize(20)
    title.draw(win)

    for progression, count in data.items():
        bar_height = (count / max_value) * 200

        color_index = list(data.keys()).index(progression) % len(colors)
        current_color = colors[color_index]

        bar = Rectangle(Point(x, 250), Point(x + bar_width, 250 - bar_height))
        bar.setFill(current_color)
        bar.draw(win)

        label = Text(Point(x + bar_width / 2, 260), progression)
        label.draw(win)

        outcomes_text = Text(Point(x + bar_width / 2, 250 - bar_height - 10), str(count))
        outcomes_text.draw(win)

        x += bar_width + gap

    total_outcomes = sum(data.values())
    summary_text = Text(Point(window_width / 2, 580), f"{total_outcomes} outcomes in total")
    summary_text.setSize(14)
    summary_text.draw(win)

    win.getMouse()
    win.close()

#PART 2:
def part2():
    credit_list = [pass_credits, defer_credits, fail_credits]
    result = outcome(pass_credits, defer_credits, fail_credits)
    print(result,"-",credit_list[0],",",credit_list[1],",",credit_list[2])

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

#PART 3:
def part3():
    global pass_credits
    global defer_credits
    global fail_credits
    save_to_file(file_path, [pass_credits, defer_credits, fail_credits])
    stored_data = read_from_file(file_path)
    if stored_data:
        pass_credits, defer_credits, fail_credits = stored_data
        result = outcome(pass_credits, defer_credits, fail_credits)
        print(result, "-", pass_credits, ",", defer_credits, ",", fail_credits)
    else:
        print("No data found in the file.")

while True:
    func()
    print("Would you like to enter another set of data?")
    user_choice = input("Enter 'y' for yes or 'q' to quit and view results: ")
    if user_choice == "q":
        draw_histogram(progression_count)
        part2()
        part3()
        break
