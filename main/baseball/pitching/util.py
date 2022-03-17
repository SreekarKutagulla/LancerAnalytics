from setup import *
from heatMap import *

def plotAndSaveAllTypesIndividually(playerNum):
    types = ['S', 'H', 'B']
    data = openPLayer(playerNum)
    updateWithInput(playerNum)
    saveToImage(playerNum)
    generateHeatmaps(data, playerNum, True)
    for i in types:
        plotScatterWithType(playerNum, i)
        saveToImage(playerNum)
