'''
Code is used to generate heatmap of the various points in az
'''

import folium
from folium.plugins import HeatMap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fp = "/Users/adityasamant/Desktop/Team-14/heatmap.html"
fp_two = "/Users/adityasamant/Desktop/Team-14/heatmap.html"
df = pd.read_csv("/Users/adityasamant/Desktop/Team-14/city-data.csv")

#Arizona [Lat, Lon]; zoom_start --> some random zoom focus
f_map = folium.Map([34.048927, -111.093735], zoom_start=13)

# Create a radius around each location
'''for index,row in df.iterrows():
    folium.CircleMarker([row['Y'], row['X']], radius=15,popup=row['No. of Tickets'], fill_color="#3db7e4").add_to(f_map)'''

hm_wide = HeatMap( zip(df.Y.values, df.X.values, df['No. of Tickets']),
                     min_opacity=0.2,
                     radius=15, blur=12,
                     max_zoom=1
                 )
f_map.add_child(hm_wide)
f_map.save(fp)









