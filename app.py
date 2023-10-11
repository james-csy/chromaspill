import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from cartopy import crs as ccrs

import geopandas
from geodatasets import get_path

# Specify the path to your CSV file
csv_file = 'incidents.csv'

# Initialize an empty list to store your data
data = []

df = pd.read_csv(csv_file)

"""
#define subplot layout
fig, axes = plt.subplots(nrows=2, ncols=2)

#add DataFrames to subplots
df.plot.scatter(x = "lat", y = "lon", c='max_ptl_release_gallons', ax=axes[0,0])
df.plot.scatter(x = "lat", y = "lon", c='measure_disperse', ax=axes[0,1])
df.plot.scatter(x = "lat", y = "lon", c='measure_burn', ax=axes[1,0])
df.plot.scatter(x = "lat", y = "lon", c='measure_bio', ax=axes[1,1])
plt.show()
"""

#geo plot setup
gdf = geopandas.GeoDataFrame( df, geometry=geopandas.points_from_xy(df.lon, df.lat), crs="EPSG:4326")

# plot on map

world = geopandas.read_file(get_path("naturalearth.land"))

fig, axes = plt.subplots(nrows=2, ncols=2)

# We restrict to Gulf.
ax1 = world.clip([-200, -100, 200, 200]).plot(color="white", edgecolor="black")
ax2 = world.clip([-200, -100, 200, 200]).plot(color="white", edgecolor="black")
ax3 = world.clip([-200, -100, 200, 200]).plot(color="white", edgecolor="black")
ax4 = world.clip([-200, -100, 200, 200]).plot(color="white", edgecolor="black")

# We can now plot our ``GeoDataFrame``.
gdf.plot(ax=ax1, alpha = 0.1, legend=True, column='max_ptl_release_gallons')
gdf.plot(ax=ax2, alpha = 0.1, legend=True, column='measure_disperse')
gdf.plot(ax=ax3, alpha = 0.1, legend=True, column='measure_burn')
gdf.plot(ax=ax4, alpha = 0.1, legend=True, column='measure_bio')

plt.show()

#print(data)