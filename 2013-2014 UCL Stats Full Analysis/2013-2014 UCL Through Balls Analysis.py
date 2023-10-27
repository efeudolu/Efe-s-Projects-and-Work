
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Through Balls per Game ", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Messi", "Iniesta", "Wernbloom", "Pedro", "Honda", "Sanchez & Tiago & Pirlo & Robben"]
through_balls_per_game = [1, 0.8, 0.7, 0.6, 0.5, 0.4]
ticks = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

create_scatter_plot(players, through_balls_per_game, 'Player Names', 'Through Balls per Game', 'Most Through Balls per Game in 2013-2014 UCL Season', ticks)

