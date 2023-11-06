
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Minutes Played", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Miranda", "Casillas", "Gabi & Juanfran & Courtois", "Koke", "Alaba & Neuer", "Ronaldo", "Lahm"]
minutes_played = [1200, 1125, 1110, 1094, 1080, 993, 991]
ticks = [950, 1000, 1050, 1100, 1150, 1200, 1250]

create_scatter_plot(players, minutes_played, 'Player Names', 'Minutes Played', 'Most Minutes Played in 2013-2014 UCL Season', ticks)

