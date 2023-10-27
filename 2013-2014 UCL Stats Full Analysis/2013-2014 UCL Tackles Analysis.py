
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Tackles per Game", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Vidal", "Izaguirre", "Bender", "N'Sakala & Wernbloom", "Hummels", "Mascherano & Gabi", "Sahin & Fernandinho"]
tackles_made_per_game = [4.7, 4.6, 4.5, 4.3, 4.2, 4.1, 3.9]
ticks = [3.75, 4, 4.25, 4.5, 4.75, 5]

create_scatter_plot(players, tackles_made_per_game, 'Player Names', 'Tackles per Game', 'Most Tackles per Game in 2013-2014 UCL Season', ticks)

