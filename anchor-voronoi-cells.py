#!/Users/simurgh/anaconda/bin/python
from scipy.spatial import Voronoi, voronoi_plot_2d
from ripe.atlas.cousteau import AnchorRequest

import mplleaflet

filters = {"status": 1}

anchors = AnchorRequest(**filters)
xy = []

# Grab the coordinates (longitude, latitude) of connected anchors
for anchor in anchors:
    xy.append(anchor["geometry"]["coordinates"])

vor_polygon = Voronoi(xy)
voronoi_plot_2d(vor_polygon, show_vertices = False)

mapfile = 'anchor-voronoi-cells.html'
# Create the map. Save the file to html
mplleaflet.show(path=mapfile)