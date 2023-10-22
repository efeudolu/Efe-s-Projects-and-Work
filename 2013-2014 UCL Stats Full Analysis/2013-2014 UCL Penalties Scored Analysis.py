import matplotlib.pyplot as plt

def create_bar_chart(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.bar(x_values, y_values)


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.show()


players = ["Vidal", "Ronaldo & Messi & Aguero"]
penalty_goals = [4, 2]
ticks = list(range(1, max(penalty_goals) + 1))

create_bar_chart(players, penalty_goals, 'Player Names', 'Penalties Scored', 'Most Penalties Scored in 2013-2014 UCL Season', ticks)
