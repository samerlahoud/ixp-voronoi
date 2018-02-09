#!/Users/simurgh/anaconda/bin/python

import os
import json
import folium
from folium import GeoJson
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

probe_location = os.path.join('probes.geojson')
with open(probe_location) as f:
	 probe = json.load(f)
	 
coor_list=[]
for feature in probe['features']:
    coor_list.append(feature['geometry']['coordinates'])

kw = {'location': [48, -102], 'zoom_start': 3}
m = folium.Map(**kw)
GeoJson(probe).add_to(m)
vor = Voronoi(coor_list)
vor_plot = voronoi_plot_2d(vor)
#vor_plot.add_to(m)

m.save(os.path.join('probe-map.html'))