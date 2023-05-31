#!/usr/bin/env python
# coding: utf-8

# In[24]:


# to download osm data
import osmnx as ox

# to import and explore data
import pandas as pd

# to manipulate and visualize spatial data
import geopandas as gpd

# to provide basemaps 
import contextily as ctx


# In[96]:


address = 'India,Maharashtra,Mumbai,Matunga'


# In[97]:


get_ipython().run_cell_magic('time', '', "# %%time is a magic command to see how long it takes this cell to run \n\n# get the data from OSM that are tagged as 'building' for a 1000m X 1000m square area\nosm = ox.geometries_from_address(address,tags={'building':True},dist=1000)\n")


# In[99]:


# how many rows and columns?
osm.shape


# In[100]:


# what is the datatype?
type(osm)


# In[102]:


# what are the columns and their datatypes?
osm.info()


# In[103]:


# show me the first 5 rows
osm.head()


# In[104]:


# show me 10 random rows
osm.sample(10)


# In[105]:


# subset it

# create a list of column names you want to keep
columns_to_keep = ['geometry','building']

# redefine the dataframe based on only the columns we want to keep 
osm = osm[columns_to_keep]

# output 10 random rows
osm.sample(10)


# In[106]:


# assign a new variable for building counts
osm_building_counts = osm.building.value_counts()

# output the results
osm_building_counts


# In[107]:


type(osm_building_counts)


# In[108]:


# create a new variable and convert it into a pandas dataframe
df_osm_building_types = pd.DataFrame(osm_building_counts)

# what does the dataframe look like?
df_osm_building_types


# In[109]:


# reset the index
df_osm_building_types = df_osm_building_types.reset_index()
df_osm_building_types


# In[110]:


df_osm_building_types.columns = ['building_type','count']
df_osm_building_types


# In[68]:


df_osm_building_types.plot()


# In[111]:


df_osm_building_types.plot.barh(figsize=(12,6),
                                x='building_type')


# In[112]:


# sort it the other way
df_osm_building_types = df_osm_building_types.sort_values(by='count', ascending=True)
df_osm_building_types


# In[113]:


df_osm_building_types[-10:].plot.barh(figsize=(12,4),
                                      x='building_type',
                                      y='count',
                                      title="Top 10 building types in "+address)


# In[114]:


# check the data type
type(osm)


# In[115]:


# plot entire dataset
ax = osm.plot(figsize=(10,10))


# In[116]:


# plot a single random building
ax = osm.sample(1).plot()


# In[117]:


# create the map plot
ax = osm.plot(figsize=(10,10),
         column='building',
         cmap='tab20',
         legend=True,
         legend_kwds={'loc':'upper left','bbox_to_anchor':(1,1),'frameon':False})

# additional attributes to the map plot

# add a title
ax.set_title('Building types in ' + address)

# get rid of the axis
ax.axis('off')


# In[118]:


# reproject to Web Mercator
osm_web_mercator = osm.to_crs(epsg=3857)


# In[119]:


ax = osm_web_mercator.plot(figsize=(10,10),
                            column='building',
                            cmap='tab20',
                            legend=True,
                            legend_kwds={'loc':'upper left','bbox_to_anchor':(1,1),'frameon':False})


# add a title
ax.set_title('Building types in ' + address)

# get rid of the axis
ax.axis('off')

# add the basemap

# open street map basemap
# ctx.add_basemap(ax,source=ctx.providers.OpenStreetMap.Mapnik)

# basemap from carto that has a dark background (easier to see)
ctx.add_basemap(ax,source=ctx.providers.CartoDB.DarkMatter)


# In[120]:


# import matplotlib's colors library
import matplotlib.colors as colors

# create a list of colors based on the number of items in your legend (14), and in this case, make it all grays
color_ramp = ['gainsboro']*14

# assign a single value in the list to be red. In this case, the 3rd entry in the list is for "commercial" buildings.
color_ramp[2] = 'red'

# create your colormap 
custom_cmap = colors.ListedColormap(color_ramp)


# In[121]:


ax = osm.plot(figsize=(10,10),
         column='building',
         cmap=custom_cmap,
         legend=True,
         legend_kwds={'loc':'upper left','bbox_to_anchor':(1,1),'frameon':False})

# add a title
ax.set_title('Building types in ' + address)

# get rid of the axis
ax.axis('off')


# In[122]:


# here is the function
def make_building_map(location):
    # get the data from osm
    osm = ox.geometries_from_address(location,
                                     tags={'building':True},
                                     dist=1000)
    
    # reproject to Web Mercator
    osm_web_mercator = osm.to_crs(epsg=3857)
    
    # create the map
    ax = osm_web_mercator.plot(figsize=(10,10),
                                column='building',
                                cmap='tab20',
                                legend=True,
                                legend_kwds={'loc':'upper left','bbox_to_anchor':(1,1),'frameon':False})
    
    # additional features

    # add a title
    ax.set_title('Building types in ' + location)

    # get rid of the axis
    ax.axis('off')
    
    # add a dark basemap
    ctx.add_basemap(ax,source=ctx.providers.CartoDB.DarkMatter)


# In[123]:


get_ipython().run_cell_magic('time', '', '# run the function once\nmake_building_map(address)\n')


# In[124]:


address_list = [address]


# In[125]:


get_ipython().run_cell_magic('time', '', '# run our function for every address in our list\nfor add in address_list:\n    make_building_map(add)\n')

