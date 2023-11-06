
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Blocks per Game ", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Delaney", "Szukala", "Lombaerts & Mertesacker", "Vidic & Albiol & van Dijk", "Ferdinand & Melo & Koscielny"]
blocks_per_game = [1.7, 1.5, 1.4, 1.2, 1.1]
ticks = [1, 1.2, 1.4, 1.6, 1.8, 2]

create_scatter_plot(players, blocks_per_game, 'Player Names', 'Blocks per Game', 'Most Blocks per Game in 2013-2014 UCL Season', ticks)

