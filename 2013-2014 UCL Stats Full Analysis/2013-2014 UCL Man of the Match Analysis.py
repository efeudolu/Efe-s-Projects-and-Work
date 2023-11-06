
import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.bar(x_values, y_values)


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.show()


players = ["Messi", "Ronaldo & Ibrahimovic", "Neymar & Garcia", "Sandro & Di Maria & Robben & Vidal & Chedjou"]
man_of_the_match_awards_won = [5, 4, 3, 2]
ticks = [0, 1, 2, 3, 4, 5]

create_scatter_plot(players, man_of_the_match_awards_won, 'Player Names', 'Man of the Match Awards Won', 'Most Man of the Match Awards Won in 2013-2014 UCL Season', ticks)

