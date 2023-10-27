
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Clearances per Game", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Ortlechner & Vidic", "Siovas", "Szukala", "Manolas", "Mellberg & Sigurdsson", "Gardos", "Pique", "Hubocan"]
clearances_made_per_game = [10.8, 10.5, 10.2, 10.1, 8.2, 7.8, 7.6, 7.5]
ticks = [7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11]

create_scatter_plot(players, clearances_made_per_game, 'Player Names', 'Clearances per Game', 'Most Clearances per Game in 2013-2014 UCL Season', ticks)

