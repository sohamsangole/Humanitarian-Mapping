# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import streamlit as st

st.markdown("# IGT PROJECT")

# !pip install osmnx

# !pip3 install pandas

# !pip install geopandas

# !pip install contextily

import osmnx as ox
import pandas as pd
import geopandas as gpd
import contextily as ctx

addr = 'VJTI'

# get data
osm = ox.geometries_from_address(addr, tags={'building' : True}, dist = 1000)

# analyze size of the data
osm.shape

# analyze how the data is stored
type(osm)

# info about every column of the dataframe
osm.info()

# shows the first 5 rows of the dataframe, just seeing how the data looks
osm.head()

# shows the last 5 rows of the dataframe, just seeing how the data looks
osm.tail()

# selecting any 10 rows from this data
osm.sample(10)

# full list of columns
list(osm)

st.table(osm)

# +
# to sort the data and only keep what we need, what we do is that we create a subset of the columns that we need 

# list of columns that we need
columns_to_keep = ['geometry', 'building']

# redefine the dataframe based on only the columns we want to keep
osm = osm[columns_to_keep]

# output 10 randoms rows of this subset
osm.sample(10)

# we did this to check whether the data have been sorted perfectly or not :)

# +
# counting the number of appearances for each value in the table
osm_b_count = osm.building.value_counts()

# output the results
osm_b_count
# -

# checking value of osm_b_count
type(osm_b_count)

# +
# converting to dataframe
df_osm_b_types = pd.DataFrame(osm_b_count)

# look of dataframe created
df_osm_b_types

# +
# giving index so that we can easily refer the data values
df_osm_b_types = df_osm_b_types.reset_index()

# look of dataframe created
df_osm_b_types
# -

# Renaming columns 
df_osm_b_types.columns = ['building_type', 'count']
df_osm_b_types

# general plot of this graph (line graph)
df_osm_b_types.plot()

# bar graph for this plot
df_osm_b_types.plot.barh(figsize = (12, 6), x='building_type')

df_osm_b_types.plot.bar(figsize = (12, 6), x='building_type')

# +
# A horizontal bar reverses the order of the values on the y axis. This can be solved by using sorting

df_osm_b_types = df_osm_b_types.sort_values(by='count', ascending=True)
df_osm_b_types

# +
# Plotting again

df_osm_b_types[-5:].plot.barh(figsize = (12, 4), x='building_type', y='count', title='Top 5 Building Types ' + addr)
# -

# Since we already know the dtype for osm we can plot the entire dataset using osm
ax = osm.plot(figsize=(10, 10))

# plotting one building
ax = osm.sample(1).plot()

# plotting a limited amt. of building
ax = osm.sample(100).plot()

# +
# creating the map plot 
ax = osm.plot(figsize=(10,10),
              column='building',
              cmap='tab20',
              legend=True,
              legend_kwds={'loc' : 'upper left' , 'bbox_to_anchor' : (1,1), 'frameon' : False})

ax.set_title("Building Types in: "+addr)

# +
# Adding a basemap
# -

osm_web_mercator = osm.to_crs(epsg = 3857)

# +
ax = osm_web_mercator.plot(figsize=(10, 10),
                          column='building',
                          cmap='tab20',
                          legend=True,
                          legend_kwds={'loc' : 'upper left' , 'bbox_to_anchor' : (1,1), 'frameon' : False})

ax.set_title("Building Types in: "+addr)

# dark background
ctx.add_basemap(ax, source=ctx.providers.CartoDB.DarkMatter)

# open street view
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
# -

st.plotly_chart(ax)



