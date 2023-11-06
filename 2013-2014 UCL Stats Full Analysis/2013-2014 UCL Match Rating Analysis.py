
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.scatter(x_values, y_values, label="Overall Match Rating", marker="o")


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.legend()

    plt.show()


players = ["Ronaldo", "Messi", "Robben", "Ibrahimovic", "Modric", "Sandro", "Vidal", "Neymar", "Ribery & Aguero"]
overall_match_rating = [8.71, 8.37, 8.10, 8.01, 7.83, 7.81, 7.75, 7.68, 7.67]
ticks = [7.5, 7.75, 8, 8.25, 8.5, 8.75, 9]

create_scatter_plot(players, overall_match_rating, 'Player Names', 'Overall Match Rating', 'Highest Overall Match Rating in 2013-2014 UCL Season', ticks)

