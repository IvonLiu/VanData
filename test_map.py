# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:24:51 2015

@author: Owner
"""

# Import pandas
import pandas

# Import matplotlib and Basemap
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Set iPython to display visualization inline
%matplotlib inline

business_df = pandas.read_csv('/resources/business_licences.csv', dtype={12: str})
business_df = business_df.dropna()
business_df.head()

# Group data by category
businesses_by_type = business_df.groupby(['BusinessType'])
businesses_by_type.head()

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

count = 0;
for name, group in businesses_by_type:
    # Define our longitude and latitude points
    x,y = map(group['Longitude'].values, group['Latitude'].values)
    # Plot them using round markers of size 6
    temp = ""
    if count % 2 == 0:
        temp = "#33b5e5"
    else:
        temp = "#ff0000"
    map.plot(x, y, 'o', markersize=3)
    count = count+1

# Show the map
plt.show()