
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Least Times Dribbled Past per Game", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Terry & Ribery & Xavi & Eto'o & Koscielny & Mertesacker & Alex & Arshavin & Varane & Rosicky"]
least_dribbled_past_per_game = [0.1]
ticks = [0, 0.1, 0.2, 0.3]

create_scatter_plot(players, least_dribbled_past_per_game, 'Player Names', 'Least Times Dribbled Past per Game', 'Least Times Dribbled Past per Game in 2013-2014 UCL Season', ticks)

