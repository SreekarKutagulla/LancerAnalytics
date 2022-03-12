from setup import *
# from determineValue import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.ndimage.filters import gaussian_filter


def myplot(x, y, s, bins=1000):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins)
    heatmap = gaussian_filter(heatmap, sigma=s)

    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent

def generateHeatmapsFromPlayer(playerNum, saving):

    data = openPLayer(playerNum)
    generateHeatmaps(data, playerNum, saving)


def generateHeatmaps(data, playerNum, saving):
    fig, axs = plt.subplots(2, 2)

    sigmas = [0, 16, 32, 64]

    for ax, s in zip(axs.flatten(), sigmas):
        if s == 0:
            ax.plot(data.X, data.Y, 'k.', markersize=5)
            ax.set_title("Scatter plot")
        else:
            img, extent = myplot(data.X, data.Y, s)
            ax.imshow(img, extent=extent, origin='lower', cmap=cm.jet)
            ax.set_title("sigma %d" % s)
            if(s == 64 and saving):
                file = '' + getMonthDay() + str(playerNum) +  'heatmap.png'
                plt.savefig(file, bbox_inches='tight', dpi=150)

    plt.show()