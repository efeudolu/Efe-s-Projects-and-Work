
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Interceptions per Game", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Kucher", "Schar", "Tiago", "de Jong", "Chedjou & Schmelzer", "Melo & Gibbs", "Sahin & Kehl"]
interceptions_made_per_game = [4.8, 4, 3.9, 3.8, 3.6, 3.5, 3.4]
ticks = [3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5]

create_scatter_plot(players, interceptions_made_per_game, 'Player Names', 'Interceptions per Game', 'Most Interceptions per Game in 2013-2014 UCL Season', ticks)

