#!/Users/simurgh/anaconda/bin/python
from scipy.spatial import Voronoi, voronoi_plot_2d
from ripe.atlas.cousteau import ProbeRequest

import mplleaflet

filters = {"status": 1}

probes = ProbeRequest(**filters)
xy = []

# Grab the coordinates (longitude, latitude) of connected probes
for probe in probes:
    xy.append(probe["geometry"]["coordinates"])

vor_polygon = Voronoi(xy)
voronoi_plot_2d(vor_polygon, show_vertices = False)

mapfile = 'probe-voronoi-cells.html'
# Create the map. Save the file to html
mplleaflet.show(path=mapfile)