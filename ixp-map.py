#!/Users/simurgh/anaconda/bin/python

import os
import json
import folium
from folium import GeoJson
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

ixp_location = os.path.join('buildings.geojson')
with open(ixp_location) as f:
	 ixp = json.load(f)
	 
coor_list=[]
for feature in ixp['features']:
    coor_list.append(feature['geometry']['coordinates'])

kw = {'location': [48, -102], 'zoom_start': 3}
m = folium.Map(**kw)
GeoJson(ixp).add_to(m)
vor = Voronoi(coor_list)
vor_plot = voronoi_plot_2d(vor)
#vor_plot.add_to(m)

m.save(os.path.join('ixp-map.html'))