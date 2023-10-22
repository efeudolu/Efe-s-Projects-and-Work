import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Assists per 90", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.show()


players = ["Nasri", "Milner", "Rooney", "van Der Wiel", "Di Maria"]
assists_per_90 = [0.84, 0.76, 0.70, 0.67, 0.66]
ticks = [0.6, 0.7, 0.8, 0.9, 1]

create_scatter_plot(players, assists_per_90, 'Player Names', 'Assists per 90', 'Most Assists per 90 in 2013-2014 UCL Season', ticks)
