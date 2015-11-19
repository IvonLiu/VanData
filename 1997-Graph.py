# Import pandas
import pandas as pd

# Import matplotlib and Basemap
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Set iPython to display visualization inline
%matplotlib inline

businesss_df = pandas.read_csv('/resources/1997business_licences.csv')

business_df = businesss_df.dropna()

# Display Latitudes and Longitudes in a table
#df = pandas.DataFrame(business_df, columns = ['Longitude', 'Latitude'])
#df

# Size of Figure
fig = plt.figure(figsize=(20,10))

# Feel Free to adjust llcrnrlon, llcrnrlat and urcnrnrlon, urcrnrlat 

map = Basemap(projection='merc', lat_0=49, lon_0=-123,
              resolution = 'h', area_thresh = 1000,
              llcrnrlon=-123.3, llcrnrlat=49.1,
              urcrnrlon=-123, urcrnrlat=49.4)

# Coastlines
map.drawcoastlines()

# Country Borders
map.drawcountries()

# Gray Continents
map.fillcontinents(color = '#888888')

# Draw the map boundaries
map.drawmapboundary(fill_color='#f4f4f4')

# Define our longitude and latitude points
x,y = map(df['Longitude'].values, df['Latitude'].values)

# Plot them using round markers of size 6
map.plot(x, y, 'ro', markersize=6)

# Show the map
plt.show()