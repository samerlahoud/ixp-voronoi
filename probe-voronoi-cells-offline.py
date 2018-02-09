#!/Users/simurgh/anaconda/bin/python
import json
import os

import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

import mplleaflet

# Load up the geojson data
filename = ('probes.geojson')
with open(filename) as f:
    gj = json.load(f)

# Grab the coordinates (longitude, latitude) from the features, which we
# know are Points
xy = np.array([feat['geometry']['coordinates'] for feat in gj['features']])

#plt.hold(True)
# Plot the ixp as red dots
#plot(xy[:,0], xy[:,1], 'rx')

vor_polygon = Voronoi(xy)
voronoi_plot_2d(vor_polygon, show_vertices = False)

mapfile = 'probe-voronoi-cells.html'
# Create the map. Save the file to html
mplleaflet.show(path=mapfile)