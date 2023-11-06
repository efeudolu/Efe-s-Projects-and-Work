
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Aerial Duels Won per Game ", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Garcia", "Ivanovic", "Szukala", "Drogba", "Vidic", "Sagna and Kießling", "Martinez", "Llorente & Chielleni"]
aerial_duels_per_game = [5.3, 4.8, 4.7, 4.6, 4.3, 4.1, 3.8, 3.6]
ticks = [3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5, 5.25, 5.5]

create_scatter_plot(players, aerial_duels_per_game, 'Player Names', 'Aerial Duels Won per Game', 'Most Aerial Duels Won per Game in 2013-2014 UCL Season', ticks)

