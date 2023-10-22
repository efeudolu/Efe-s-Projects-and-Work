import matplotlib.pyplot as plt

def create_bar_chart(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.bar(x_values, y_values)


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.show()


players = ["Ronaldo", "Ibrahimovic", "Costa", "Messi & Bale", "Lewandowksi & Benzema & Negredo"]
non_penalty_goals = [15, 9, 7, 6, 5]
ticks = list(range(1, max(non_penalty_goals) + 1))

create_bar_chart(players, non_penalty_goals, 'Player Names', 'Non Penalty Goals', 'Most Non Penalty Goals in 2013-2014 UCL Season', ticks)
