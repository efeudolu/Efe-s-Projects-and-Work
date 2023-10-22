import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Assists per 90", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.show()


players = ["Ronaldo", "Aguero", "Negredo", "Costa", "Ibrahimovic", "Higuain", "Messi", "van Persie", "Nasri", "Bale"]
goals_and_assists_per_90 = [1.99, 1.67, 1.66, 1.39, 1.35, 1.33, 1.14, 1.09, 1.05, 1.03]
ticks = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

create_scatter_plot(players, goals_and_assists_per_90, 'Player Names', 'Most Goals and Assists per 90', 'Most Goals and Assists per 90 in 2013-2014 UCL Season', ticks)
