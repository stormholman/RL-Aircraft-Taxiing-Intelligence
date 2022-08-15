import pygame
import pandas as pd


class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, win):
        pygame.draw.line(win, (255, 255, 255), (self.x1, self.y1), (self.x2, self.y2), 5)


def getWalls():
    walls = []
    mycoor = pd.read_csv('coordinates_walls.csv')
    # mycoor=pd.read_csv('coordinates_no_guidance_walls.csv') # activate to get rid of guidance walls

    for i in range(len(mycoor.index)):
        x1 = mycoor.iloc[i][1]
        y1 = mycoor.iloc[i][2]
        x2 = mycoor.iloc[i][3]
        y2 = mycoor.iloc[i][4]

        wall = Wall(x1, y1, x2, y2)
        walls.append(wall)

    return (walls)
