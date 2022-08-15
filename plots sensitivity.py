import matplotlib.pyplot as plt
import numpy as np
import csv


class Data():
    def __init__(self, filename, label):

        with open(filename, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        self.label = label
        self.episodes = []
        self.steps = []
        self.laps = []

        for x in data[3:]:
            if x[0]:
                self.episodes.append(x[0])
            if x[1]:
                self.steps.append(x[1])
            if x[2]:
                self.laps.append(x[2])

        self.laps = [float(x) for x in self.laps]
        self.steps = [int(y) for y in self.steps]
        self.total_steps = [sum(self.steps[:s]) for s in range(1, len(self.steps) + 1)]

        self.window = 50
        self.average_laps = []
        self.average_steps = []
        for ind in range(len(self.laps) - self.window + 1):
            self.average_laps.append(np.mean(self.laps[ind:ind + self.window]))
            self.average_steps.append(np.mean(self.steps[ind:ind + self.window]))
        self.x = np.arange(self.window, len(self.episodes) + 1, 1)

        # KPI
        self.avgone = 0
        for idx, x in enumerate(self.average_laps):
            if x >= 1:
                self.avgone = idx
                break

        self.max = np.max(self.laps)
        self.avgmax = np.max(self.average_laps)
        self.mean_steps = np.mean(self.steps)
        self.mean_laps = np.mean(self.laps)
        self.laps_steps = self.mean_laps / self.mean_steps


# Datasets
# Sensitivity
files = ["data/data baseline.csv", "data/data DQN.csv", "data/data gamma 0.85.csv", "data/data gamma 0.99csv.csv",
         "data/data lr0.0001.csv", "data/data lr0.0005.csv", "data/data no guidance walls.csv", "data/data sensors.csv"]
filenames = ["base", "DQN", "gamma 0.85", "gamma 0.99",
             "lr 0.0001", "lr 0.0005", "no guidance walls", "11 sensors"]

# files = ["data.csv"]
# filenames = ["current data"]

# Uncertainty
# files = ["data/data baseline.csv", "data/base 2.csv", "data/data base 3.0.csv"]
# filenames = ["base 1", "base 2", "base 3"]

filesobj = []
for idx, file in enumerate(files):
    filesobj.append(Data(file, filenames[idx]))

# KPI
for file in filesobj:
    print("=====", " ", file.label, " ", "=====")
    print("Total steps", file.total_steps[-1])
    print("Average >1 on episode", file.avgone, " & step ", file.total_steps[file.avgone])
    print("max", file.max)
    print("avgmax", file.avgmax)
    print("mean_steps", file.mean_steps)
    print("mean_laps", file.mean_laps)
    print("laps_steps", file.laps_steps)
    print(" ")

# Graphs
plt.figure("Laps per episode")
for file in filesobj:
    plt.plot(file.x[:3000], file.average_laps[:3000], label=file.label)
plt.ylabel('laps')  # set the label for y axis
plt.xlabel('episode')  # set the label for x-axis
plt.legend()
# Show the major grid lines with dark grey lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.title("Laps per episode")  # set the title of the graph
# plt.show()

plt.figure("Steps per episode")
for file in filesobj:
    plt.plot(file.x[:3000], file.average_steps[:3000], label=file.label)
plt.ylabel('steps')  # set the label for y axis
plt.xlabel('episode')  # set the label for x-axis
plt.legend()
# Show the major grid lines with dark grey lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.title("Steps per episode")  # set the title of the graph
plt.show()
