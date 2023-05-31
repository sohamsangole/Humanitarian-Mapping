# Veermata Jijabai Technological Institute

## Soham Sangole **: 211080047**

## Ishaan Chandak: **211080044**

**Mentor : Prof. Dr.V.B.Nikam**

#
**# IGT Mini Project
 Humanitarian OpenStreet Mapping**

![](RackMultipart20230531-1-dpaj1k_html_58aac78687a609f.png)

![Shape1](RackMultipart20230531-1-dpaj1k_html_237499165a11f2b9.gif)

## Table of Contents

1. [Introduction](#_x5fpb2wq9npl)
2. [Project Scope](#_mgg5w27010t0)
3. [Technologies Used](#_8v1oxxo91du)
4. [Requirements](#_u3xlmmqsjhpe)
5. [Implementation](#_40e67aiebhat)
6. [Conclusion](#_3cllrcz1c9ey)
7. References

#
## Introduction

- Overview:
  - The Humanitarian OpenStreet Mapping Project, which intends to use the power of crowdsourcing and open data to enhance humanitarian and disaster response activities, is introduced in this document.
  - For areas that are vulnerable to natural disasters, armed conflict, or lack extensive mapping data, the initiative focuses on mapping and creating detailed geospatial data.
  - The project's objective is to enhance the accessibility and accuracy of geographic information in regions where it is most needed. It will be accomplished via the joint efforts of volunteers, local communities, and organizations.

- Purpose and Objectives:
  - The Humanitarian OpenStreet Mapping Project's main goal is to offer trustworthy and current geographic data to nonprofit organisations, governmental organisations, and local communities engaged in disaster response and preparedness.
  - By producing comprehensive maps that show important geographic features like roads, buildings, and other infrastructure, the initiative hopes to close the information gap.
  - The goal of the project is to promote effective emergency response, relief distribution, and infrastructure planning by improving the quality and accessibility of mapping data.

- Background:
  - The availability of precise and complete maps is constrained or nonexistent in many parts of the world, particularly in poor nations or regions ravaged by conflicts.
  - Lack of comprehensive maps during humanitarian crises or crisis scenarios makes it difficult to pinpoint impacted areas, arrange evacuation routes, or efficiently distribute supplies.
  - By enabling volunteers to contribute and instantly update geographic data, OpenStreetMap (OSM), a collaborative mapping platform, offers the perfect remedy.

#
## Project Scope

- Support **emergency response** planning by outlining evacuation routes, defining safe zones, and presenting situational awareness to help with decision-making in disaster situations.

- Collaborative **Data gathering** : To ensure a coordinated effort in data gathering, invite volunteers, local communities, and organisations to contribute and update geographic data using the OpenStreetMap platform.

- **Infrastructure Mapping** : To help with effective resource allocation and infrastructure planning, identify and map important infrastructure, such as roads, buildings, hospitals, schools, and water supplies.

- **Distribution of Humanitarian Aid** : Provide precise mapping data to aid in the successful distribution of humanitarian aid, allowing organizations to more efficiently reach affected communities.
- Making **Detailed Maps of Vulnerable Areas** : To aid in disaster response and preparation, make accurate maps of areas that are vulnerable to natural catastrophes, armed conflict, or a lack of comprehensive mapping data.

- Building Capacity: Hold training sessions and distribute materials to enable nearby communities and organizations to actively take part in mapping initiatives, promoting independence.

- Validation & Quality Assurance: Maintain high standards by rigorously validating the contributed mapping data to ensure its accuracy and dependability.

- Collaboration and Knowledge Sharing: Promote collaboration and knowledge sharing among volunteers, government organizations, and humanitarian organizations in order to take use of their combined expertise and enhance mapping results.

#

#

#

#

#
## Technologies/Libraries Used

Technologies Used:

- OSMnx (osmnx):
  - OSMnx is a Python library used for downloading OpenStreetMap (OSM) data.
  - It allows for the extraction of geometries and attributes based on specific criteria, such as buildings tagged as 'building'.
  - In the code, it is used to retrieve OSM data within a specified distance from a given address.

![](RackMultipart20230531-1-dpaj1k_html_52b1748755d30a78.png)

- pandas (pd):
  - pandas is a powerful library for data manipulation and analysis in Python.
  - It provides data structures like DataFrames that enable easy handling of structured data.
  - In the code, pandas is used to import, explore, and manipulate the OSM data.

![](RackMultipart20230531-1-dpaj1k_html_31e14a1bd3b1496c.png)

- geopandas (gpd):

  - geopandas is an extension of pandas that adds support for geospatial data analysis.
  - It allows for the manipulation, analysis, and visualization of geospatial data, including geometry operations.
  - In the code, geopandas is used to work with and visualize the spatial data from OSM.

![](RackMultipart20230531-1-dpaj1k_html_2cb6501875205984.png)

- contextily (ctx):
  - ![](RackMultipart20230531-1-dpaj1k_html_b52afadea7a1718e.png)
  - contextily is a Python library that provides basemaps for geospatial visualizations.
  - It enables the integration of basemaps from various providers, such as OpenStreetMap and CartoDB.
  - In the code, contextily is used to add basemaps to the geospatial plots.

- Matplotlib.colors:
  - matplotlib.colors is a module within the matplotlib library that provides utilities for working with colors.
  - It allows for the creation and customization of color ramps and colormaps.
  - In the code, it is used to create a custom colormap to highlight specific building types.

#
## Requirements

- Data Access:
  - The system should have the capability to access OpenStreetMap (OSM) data for the desired geographic locations.
  - The data access should support retrieving specific data attributes, such as buildings tagged as 'building'.
- Data Collection and Contributions:
  - Volunteers, local communities, and organizations should be able to contribute and update geospatial data using the system.
  - The system should provide tools and functionalities for efficient data collection and contributions.
- Data Storage and Management:
  - The system should have a centralized database or distributed system to store and manage the collected mapping data.
  - The data storage should support efficient retrieval, updating, and querying of the mapping data.
- Geospatial Analysis and Visualization:
  - The system should provide capabilities for geospatial analysis and visualization of the mapping data.
  - It should support operations such as geometry manipulation, attribute querying, and spatial visualization.

#

#

#
## Implementation

- **Data Access:**
  - Utilize the OSMnx library, an open-source Python package, to access OpenStreetMap (OSM) data.
  - Use the OSMnx functions to download and retrieve OSM data based on specific geographic locations, such as cities or regions.
  - Specify relevant parameters, such as tags or attributes, to filter the data and retrieve specific features of interest, like buildings or roads.

![](RackMultipart20230531-1-dpaj1k_html_47af43b0d28bc078.png)We extracted two columns only from the data [geometry, building]

- **Data Processing and Analysis:**
  - Import the downloaded OSM data into a pandas DataFrame or geopandas GeoDataFrame for easy manipulation and analysis.
  - Perform data cleaning and preprocessing steps to handle missing values, inconsistencies, or outliers in the data.
  - Apply geospatial analysis techniques, such as spatial queries, spatial joins, and buffer operations, to derive insights from the data.
  - Utilize statistical analysis or machine learning algorithms, if applicable, to gain deeper insights or make predictions based on the data.

![](RackMultipart20230531-1-dpaj1k_html_4aab91a8b8b5bdaa.png)

We used data analysis tools and found the no. of occurrences of building types from the data that we had just accessed

- **Data Visualization:**
  - Use geopandas and matplotlib libraries to visualize the geospatial data on interactive maps or static plots.
  - Customize the visualization by setting different colors, symbols, or sizes based on attributes or categories within the data.
  - Incorporate additional basemaps or contextual layers, such as satellite imagery or terrain data, using libraries like contextily.
  - Create informative and visually appealing maps to communicate the patterns, distributions, or trends present in the data.

![](RackMultipart20230531-1-dpaj1k_html_4b13ac4a91d7c7a3.png)

Random Polygon showing shape of one of the building included in the dataframe

![](RackMultipart20230531-1-dpaj1k_html_4641182441cc0e27.png)

## **Data Visualization**

**Bar Plots**![](RackMultipart20230531-1-dpaj1k_html_ffaece609d8461de.png)

Horizontal Bar Graph of the same for the top 5 most occurring type of buildings in the choosend region.

![](RackMultipart20230531-1-dpaj1k_html_418cdf2067135fd5.png)

**Basemap Overlay:**

![](RackMultipart20230531-1-dpaj1k_html_6b770b5ffea9eb36.png)

**Choropleth Map:**

A choropleth map was created to visualize the distribution of building types in the specified address. Each building type is represented by a different color on the map.

![](RackMultipart20230531-1-dpaj1k_html_a4e59a5d021e9d3b.png)

**Custom Color Map:**

A custom color map was created to highlight a specific building type (in this case, "commercial") by assigning it a different color (red) while keeping the rest of the building types in gray.

![](RackMultipart20230531-1-dpaj1k_html_5a0b989988a68c9f.png)

**We can also add an OpenStreetView Map,**

![](RackMultipart20230531-1-dpaj1k_html_3d95d58a4b24b55a.png)

**Output Map when we put**  **VJTI**  **as coordinates,**

![](RackMultipart20230531-1-dpaj1k_html_add09325f235e197.png)

Map plotted directly with the help of the dataset

![](RackMultipart20230531-1-dpaj1k_html_c2dbcc6f01fb95fa.png)

Map plotted on the StreetViewMap

This plotting clearly shows how accurate our project is in terms of mapping. It has successfully mapped VJTI and the prominent educational institutes surrounding VJTI. All marked in red symbolize this.

#

#

#
## Conclusion

With the help of community involvement and geographical data, the Humanitarian OpenStreet Mapping project hopes to aid humanitarian activities. The project offers a complete solution for mapping and analyzing geographic data from OpenStreetMap through the creation of data access, processing, analysis, visualization, and user interface components.

The project simplifies access to OSM data by utilizing the OSMnx library, enabling users to get particular features of interest based on geographic locations and qualities. Users can clean, preprocess, and analyze data using the data processing and analysis capabilities to gain insightful information using statistical and geospatial operations.

The project offers an interactive platform with a user-friendly interface where users may enter parameters, choose regions, and explore visualizations. Features like user login, data uploading, and preference storage are added to improve the user experience and foster teamwork among project participants.

In order to maximize performance and scalability, deployment considerations guarantee that the project can be hosted on a variety of platforms. The project's functions can be used to their full potential by users with the help of the documentation and user support tools, which offer thorough assistance.

In conclusion, the Humanitarian OpenStreet Mapping project provides a useful tool for volunteer groups, local communities, and humanitarian organizations engaged in mapping and geospatial data analysis. The project makes it possible by utilizing the power of OpenStreetMap data and offering easily accessible and user-friendly tools.

## **References**

- [https://learnosm.org/en/beginner/](https://learnosm.org/en/beginner/)
- [https://www.arcgis.com/home/index.html](https://www.arcgis.com/home/index.html)
- osmnx: The OSMnx library for downloading and working with OpenStreetMap data in Python.
  - GitHub repository: [https://github.com/gboeing/osmnx](https://github.com/gboeing/osmnx)
  - Documentation: https://osmnx.readthedocs.io/
- pandas: A powerful data manipulation and analysis library for Python.
  - Documentation: https://pandas.pydata.org/
- geopandas: A library for working with geospatial data in Python, built on top of pandas.
  - Documentation: https://geopandas.org/
- contextily: A library for adding basemaps to spatial visualizations in Python.
  - GitHub repository: [https://github.com/geopandas/contextily](https://github.com/geopandas/contextily)
  - Documentation: https://contextily.readthedocs.io/
