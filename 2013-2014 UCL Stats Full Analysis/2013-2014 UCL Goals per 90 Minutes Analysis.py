
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Goals per 90", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Ronaldo", "Negredo", "Ibrahimovic", "Aguero", "Costa", "Messi", "Higuain", "van Persie"]
goals_per_90 = [1.54, 1.38, 1.35, 1.25, 1.24, 1.14, 0.89, 0.87]
ticks = [0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

create_scatter_plot(players, goals_per_90, 'Player Names', 'Goals per 90', 'Most Goals Per 90 in 2013-2014 UCL Season', ticks)

