
import matplotlib.pyplot as plt

def create_bar_chart(x_values, y_values, x_label, y_label, title, number_of_ticks):


    plt.bar(x_values, y_values)


    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    plt.yticks(number_of_ticks)

    plt.show()


players = ["Ronaldo", "Ibrahimovic & Bale & Benzema", "Costa & Di Maria", "Rooney & Robben & Aguero & Lewandowksi & Messi"]
goals_and_assists = [22, 10, 9, 8]
ticks = list(range(1, max(goals_and_assists) + 1))

create_bar_chart(players, goals_and_assists, 'Player Names', 'Goals & Assists (Direct Goal Contributions)', 'Direct Goal Contribution Leaders of 2013-2014 UCL Season', ticks)
