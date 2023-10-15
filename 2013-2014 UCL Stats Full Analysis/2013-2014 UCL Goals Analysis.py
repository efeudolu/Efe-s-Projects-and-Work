
import matplotlib.pyplot as plt

def create_bar_chart(x_values, y_values, x_label, y_label, title, number_of_ticks):
    # Created a function to represent data in a bar chart
    # Function takes in 5 parameters

    # Create the bar chart
    plt.bar(x_values, y_values)

    # Adding labels and a title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Apply  tick positions to the y-axis
    plt.yticks(number_of_ticks)

    # Display the graph
    plt.show()


players = ["Ronaldo", "Ibrahimovic", "Messi", "Costa", "Lewandowski"]
goals = [17, 10, 8, 8, 6]
ticks = list(range(1, max(goals) + 4))

create_bar_chart(players, goals, 'Player Names', 'Goals Scored', 'Top Scorers of 2013-2014 UCL Season', ticks)
