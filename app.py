import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Specify the path to your CSV file
csv_file = 'incidents.csv'

# Initialize an empty list to store your data
data = []

df = pd.read_csv(csv_file)
#print(df.head())
#print(df.columns)

#define subplot layout
fig, axes = plt.subplots(nrows=2, ncols=2)

#add DataFrames to subplots

df.plot.scatter(x = "lat", y = "lon", c='max_ptl_release_gallons', ax=axes[0,0])
df.plot.scatter(x = "lat", y = "lon", c='measure_disperse', ax=axes[0,1])
df.plot.scatter(x = "lat", y = "lon", c='measure_burn', ax=axes[1,0])
df.plot.scatter(x = "lat", y = "lon", c='measure_bio', ax=axes[1,1])
plt.show()


"""
df_viz = df.drop(labels = ['id', 'open_date', 'name', 'location','threat', 'tags',
       'commodity', 'measure_skim', 'measure_shore', 'measure_bio',
       'measure_disperse', 'measure_burn', 'max_ptl_release_gallons', 'posts',
       'description'])
"""

#print (df_viz.head())

#df.plot(kind="scatter", x = "lat", y = "lon", s = df["max_ptl_release_gallons"], label="spill amounts", c = "max_ptl_release_gallons",
 #           cmap = plt.get_cmap("tab20c"), colorbar=True, alpha = 0.7, figsize=(25,15))
#plt.show()


# Open and read the CSV file
with open(csv_file, mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row if it exists
    next(csv_reader, None)
    
    # Iterate through the rows and append data to the list
    for row in csv_reader:
        data.append(row)

# Now 'data' contains your CSV data as a list of lists
# Each inner list represents a row from the CSV file

# Generate random data for demonstration
num_points = len(data)
lat = []
long = []
for i in range(num_points):
    lat.append(data[i][4])
    long.append(data[i][5])

values = [1] * num_points   # Replace with your values if available

'''
# Define the size of the grid and the resolution
grid_size = 100  # Adjust this based on your preference
heatmap, xedges, yedges = np.histogram2d(lat, long, bins=grid_size, weights=values)
plt.imshow(heatmap, cmap='viridis', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
plt.colorbar(label='Intensity')  # Add a colorbar for reference
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Heatmap of Coordinates')
plt.show()
'''


#print(data)