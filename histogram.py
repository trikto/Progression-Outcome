from graphics import *

def draw_histogram(data):
    max_value = max(data.values())

    colors = ["#aef8a1", "#a0c689", "#a7bc77", "#d2b6b5"]

    bar_width = 80
    gap = 20  # Gap between bars
    x = 50
    total_bars = len(data)

    # Calculate window width dynamically based on the number of bars
    window_width = max(600, (bar_width + gap) * total_bars + 100)
    win = GraphWin("Histogram", window_width, 600)

    # Title at the top
    title = Text(Point(window_width / 2, 20), "Histogram Results")
    title.setSize(20)
    title.draw(win)

    for progression, count in data.items():
        bar_height = (count / max_value) * 200

        color_index = list(data.keys()).index(progression) % len(colors)
        current_color = colors[color_index]

        # Draw the bar
        bar = Rectangle(Point(x, 250), Point(x + bar_width, 250 - bar_height))
        bar.setFill(current_color)
        bar.draw(win)

        # Display the label at the bottom
        label = Text(Point(x + bar_width / 2, 260), progression)
        label.draw(win)

        # Display the number of outcomes at the top of the bar
        outcomes_text = Text(Point(x + bar_width / 2, 250 - bar_height - 10), str(count))
        outcomes_text.draw(win)

        x += bar_width + gap

    # Summary at the bottom
    total_outcomes = sum(data.values())
    summary_text = Text(Point(window_width / 2, 580), f"{total_outcomes} outcomes in total")
    summary_text.setSize(14)
    summary_text.draw(win)

    win.getMouse()
    win.close()

# Example data for the histogram
progression_count = {"progress": 10, "trailer": 5, "retriever": 7, "excluded": 3}

# Call the function to draw the histogram
draw_histogram(progression_count)
