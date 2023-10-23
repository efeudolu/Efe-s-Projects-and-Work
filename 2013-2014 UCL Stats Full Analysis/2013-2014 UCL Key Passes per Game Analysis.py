
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Key Passes per Game", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Ribery", "Gaitan", "Tevez & Pirlo", "Josue", "Lahm & Farfan & Ozil", "Robben & Messi"]
key_passes_per_game = [3.3, 3.2, 2.8, 2.5, 2.4, 2.3]
ticks = [2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4]

create_scatter_plot(players, key_passes_per_game, 'Player Names', 'Key Passes Per Game', 'Most Key Passes Per Game in 2013-2014 UCL Season', ticks)

