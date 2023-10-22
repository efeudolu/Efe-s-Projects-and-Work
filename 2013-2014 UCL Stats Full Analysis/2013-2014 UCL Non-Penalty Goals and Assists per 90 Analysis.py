
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Goals per 90", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Ronaldo", "Negredo", "Higuain", "Aguero", "Costa", "Ibrahimovic", "Nasri", "Bale", "Milner"]
non_penalty_goals_and_assists_per_90 = [1.81, 1.66, 1.33, 1.25, 1.24, 1.21, 1.05, 1.03, 1.01]
ticks = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

create_scatter_plot(players, non_penalty_goals_and_assists_per_90, 'Player Names', 'Non-Penalty Goals and Assists per 90', 'Most Non-Penalty Goals and Assists Per 90 in 2013-2014 UCL Season', ticks)

