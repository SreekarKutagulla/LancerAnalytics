import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from datetime import datetime

now = datetime.now() # current date and time

# def onclick(event):
#    print([event.xdata, event.ydata])

def setup():

    fig, ax = plt.subplots()

    custom_lines = [Line2D([0], [0], color='green', lw=4),
                    Line2D([0], [0], color='red', lw=4),
                    Line2D([0], [0], color='purple', lw=4)]

    plt.legend(custom_lines, ['Hit', 'Strike', 'Ball'],loc='upper center', bbox_to_anchor=(1.15, 0.8), shadow=True)


    #horizantal
    plt.plot([-2, -2], [-2, 8], linewidth=2, color='black')
    plt.plot([8, 8], [-2, 8], linewidth=2, color='black')
    plt.plot([-2, 8], [-2, -2], linewidth=2, color='black')
    plt.plot([-2, 8], [0, 0], linewidth=2, color='black')
    plt.plot([-2, 8], [2, 2], linewidth=2, color='black')
    plt.plot([-2, 8], [4, 4], linewidth=2, color='black')
    plt.plot([-2, 8], [6, 6], linewidth=2, color='black')
    plt.plot([-2, 8], [8, 8], linewidth=2, color='black')

    #vertical
    plt.plot([-2, -2], [-2, 8], linewidth=2, color='black')
    plt.plot([0, 0], [-2, 8], linewidth=2, color='black')
    plt.plot([2, 2], [-2, 8], linewidth=2, color='black')
    plt.plot([4, 4], [-2, 8], linewidth=2, color='black')
    plt.plot([6, 6], [-2, 8], linewidth=2, color='black')
    plt.plot([8, 8], [-2, 8], linewidth=2, color='black')

    #inside zone
    ax.add_patch(Rectangle((0, 0), 6, 6,
                 edgecolor = 'red',
                 facecolor = 'none',
                 lw=5))

    # fig.canvas.mpl_connect('button_press_event', onclick)

    plt.ion()

def getMonthDay():
    now = datetime.now()  # current date and time

    md = now.strftime("%m-%d")
    md = '[' + md + ']'
    return md


def openPLayer(playerNum):
    file = 'hit' + playerNum + '.csv'
    df = pd.read_csv(file)
    return df

def plotScatter(playerNum):
    df = openPLayer(playerNum)
    setup()
    h = df[(df['SHB'] == 'H')]
    plt.scatter(h.X, h.Y, s=50, c='green')

    s = df[(df['SHB'] == 'S')]
    plt.scatter(s.X, s.Y, s=50, c='red')

    b = df[(df['SHB'] == 'B')]
    plt.scatter(b.X, b.Y, s=50, c='purple')

def plotScatterWithType(playerNum, type):
    setup()
    df = openPLayer(playerNum)

    if(type == 'H'):
        h = df[(df['SHB'] == 'H')]
        plt.scatter(h.X, h.Y, s=50, c='green')
    elif(type == 'S'):
        s = df[(df['SHB'] == 'S')]
        plt.scatter(s.X, s.Y, s=50, c='red')
    elif (type == 'B'):
        b = df[(df['SHB'] == 'B')]
        plt.scatter(b.X, b.Y, s=50, c='purple')


def update():
    batter = input("16 or 23 \n")
    df = openPLayer(batter)


    plotScatter(df)
    # create scatterplot of data with gridlines


def updateWithInput(playerNum):
    plotScatter(playerNum)

def show():
    plt.show()

def saveToImage(num):
    file = '' + getMonthDay() + num + 'pitches.png'
    plt.savefig(file , bbox_inches='tight', dpi=150)