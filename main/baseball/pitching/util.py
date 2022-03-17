from setup import *
from heatMap import *

def plotAndSaveAllTypesIndividually(playerNum):
    types = ['S', 'H', 'B']
    typeNames = ["strikes", "hits", "balls"]
    data = openPLayer(playerNum)
    updateWithInput(playerNum)
    saveToImage(playerNum)
    generateHeatmaps(data, playerNum, True)
    for i in range(len(types)):
        plotScatterWithType(playerNum, types[i])
        saveToImage(typeNames[i] + playerNum)
