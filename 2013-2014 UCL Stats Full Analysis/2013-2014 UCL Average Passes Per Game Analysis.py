
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Average Passes per Game", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Xavi", "Motta", "Kroos", "Busquets", "Verratti", "Iniesta", "Bourceanu", "Lahm", "Alves", "Schweinsteiger"]
average_passes_per_game = [107.2, 101.6, 95.4, 92.6, 89.4, 82.3, 77.2, 75.8, 74.5, 74]
ticks = [70, 75, 80, 85, 90, 95, 100, 105, 110]

create_scatter_plot(players, average_passes_per_game, 'Player Names', 'Average Passes Per Game', 'Highest Average Passes Per Game in 2013-2014 UCL Season', ticks)

