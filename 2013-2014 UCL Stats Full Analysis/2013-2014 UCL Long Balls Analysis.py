
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Long Balls per Game ", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Sommer", "Szczesny", "Pirlo", "Muslera", "Hart", "Kroos", "Forster", "de Gea", "Cillessen", "Schar"]
long_balls_per_game = [13, 11.9, 11.4, 11, 10.9, 10.7, 10, 9.9, 9.8, 9.7]
ticks = [9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13]

create_scatter_plot(players, long_balls_per_game, 'Player Names', 'Long Balls per Game', 'Most Long Balls per Game in 2013-2014 UCL Season', ticks)

