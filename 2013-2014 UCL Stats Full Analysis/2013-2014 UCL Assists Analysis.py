import matplotlib.pyplot as plt

def create_bar_chart(x_values, y_values, x_label, y_label, title, number_of_ticks):

    plt.bar(x_values, y_values)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.yticks(number_of_ticks)

    plt.show()


players = ["Rooney & Di Maria", "Benzema & Ronaldo & Gabi", "Bale & Robben & Nasri & Oscar & van der Wiel" ]
assists = [6, 5, 4]
ticks = list(range(1, max(assists) + 1))

create_bar_chart(players, assists, 'Player Names', 'Assists Provided', 'Assist Leaders for 2013-2014 UCL Season', ticks)
