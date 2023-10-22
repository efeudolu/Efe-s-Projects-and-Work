
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Non-Penalty Goals per 90", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Negredo", "Ronaldo", "Ibrahimovic", "Costa", "Higuain", "Messi & Torres", "Aguero"]
non_penalty_goals_per_90 = [1.38, 1.36, 1.21, 1.08, 0.89, 0.86, 0.84]
ticks = [0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]

create_scatter_plot(players, non_penalty_goals_per_90, 'Player Names', 'Non-Penalty Goals per 90', 'Most Non-Penalty Goals Per 90 in 2013-2014 UCL Season', ticks)

