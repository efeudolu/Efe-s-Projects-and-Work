import matplotlib.pyplot as plt

# Data that will be used
players = ["Ronaldo", "Ibrahimovic", "Messi", "Costa", "Lewandowski"]
goals = [17, 10, 8, 8, 6]

# Create the scatter plot
plt.bar(players, goals)

# Adding labels and a title
plt.xlabel('Player Names')
plt.ylabel('Goals Scored')
plt.title("Top Five Scorers of 2013-2014 UCL Season")

plt.ylim(1,20)

custom_ticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

plt.yticks(custom_ticks)


# Display the graph
plt.show()
