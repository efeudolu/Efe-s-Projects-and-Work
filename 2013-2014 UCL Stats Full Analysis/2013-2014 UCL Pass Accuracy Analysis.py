
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Pass Accuracy (%) ", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Varane", "Xavi", "Busquets", "Lahm", "Kroos", "Verratti", "Maxwell", "Alex", "Martinez & Mascherano"]
pass_accuracy = [95.3, 95.2, 94.6, 94.3, 94.2, 93.7, 93.5, 93.3, 92.8]
ticks = [92, 92.5, 93, 93.5, 94, 94.5, 95, 95.5, 96]

create_scatter_plot(players, pass_accuracy, 'Player Names', 'Pass Accuracy (%)', 'Highest Pass Accuracy in 2013-2014 UCL Season', ticks)

