import pygame
import pandas as pd


class Goal:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.isactiv = False

    def draw(self, win):
        pygame.draw.line(win, (0, 255, 0), (self.x1, self.y1), (self.x2, self.y2), 2)
        if self.isactiv:
            pygame.draw.line(win, (255, 0, 0), (self.x1, self.y1), (self.x2, self.y2), 2)


# the file of shame
def getGoals():
    goals = []
    mycoor = pd.read_csv("coordinates_goals.csv")

    for i in range(len(mycoor.index)):
        x1 = mycoor.iloc[len(mycoor.index) - 1 - i][1]
        y1 = mycoor.iloc[len(mycoor.index) - 1 - i][2]
        x2 = mycoor.iloc[len(mycoor.index) - 1 - i][3]
        y2 = mycoor.iloc[len(mycoor.index) - 1 - i][4]

        goal = Goal(x1, y1, x2, y2)
        goals.append(goal)
    goals[len(goals) - 1].isactiv = True

    return (goals)
