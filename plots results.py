import matplotlib.pyplot as plt
import numpy as np
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

episodes = []
steps = []
laps = []

for x in data[3:]:
    if x[0]:
        episodes.append(x[0])
    if x[1]:
        steps.append(x[1])
    if x[2]:
        laps.append(x[2])

laps = [float(x) for x in laps]
steps = [int(y) for y in steps]
total_steps = [sum(steps[:s]) for s in range(1, len(steps) + 1)]

window = 50
average_laps = []
average_steps = []
for ind in range(len(laps) - window + 1):
    average_laps.append(np.mean(laps[ind:ind + window]))
    average_steps.append(np.mean(steps[ind:ind + window]))
x = np.arange(window, len(episodes) + 1, 1)

print(sum(steps))

plt.figure("Laps per episode")
plt.axhline(y=np.mean(laps), color='b', linestyle='-', label="Mean")
plt.plot(laps, color='magenta', mfc='pink', label="Laps")  # plot the data
plt.plot(x, average_laps, 'black', label='Running average')
plt.xticks(np.arange(0, len(episodes) + 1, 250))  # set the tick frequency on x-axis
plt.yticks(np.arange(0, round(max(laps)), 10))
plt.ylabel('laps')  # set the label for y axis
plt.xlabel('episode')  # set the label for x-axis
plt.legend()
plt.title("Laps per episode")  # set the title of the graph

plt.figure("Steps per episode")
plt.axhline(y=np.mean(steps), color='r', linestyle='-', label="Mean")
plt.plot(steps, color='green', mfc='pink', label="Steps")  # plot the data
plt.plot(x, average_steps, 'black', label='Running average')
plt.xticks(np.arange(0, len(episodes) + 1, 250))  # set the tick frequency on x-axis
plt.yticks(np.arange(0, round(max(steps)), 2000))
plt.ylabel('steps')  # set the label for y axis
plt.xlabel('episode')  # set the label for x-axis
plt.legend()
plt.title("Steps per episode")  # set the title of the graph
plt.show()
