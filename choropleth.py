# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 12:11:43 2021

@author: Yalin Li
"""

# Read map
import geopandas as gpd
world = gpd.read_file('world_map.json')
world.plot() # see the world map
world.plot('economy')

# Read data
import pandas as pd
population = pd.read_csv('population_density.csv', skiprows=4)
# Pass the value to the map
filtered = world[world.iso_a3.isin(population.loc[:, 'Country Code'])].sort_values(by='iso_a3').reset_index(drop=True)
population = population[population.loc[:, 'Country Code'].isin(world.iso_a3)].sort_values(by='Country Code').reset_index(drop=True)
filtered['population_2020'] = population['2020']

# Make the plot
ax = world.plot(color='lightgrey', edgecolor='k') # plot the background
filtered.plot('population_2020', cmap='Blues', edgecolor='k', legend=True,
              scheme='quantiles', ax=ax) # you'll need the ``mapclassify`` package for using the scheme here

legend = ax.get_legend()
labels = [i.get_text() for i in legend.get_texts()]
ax.legend(handles=legend.get_lines(), labels=labels,
          loc='lower left', title='population density',
          frameon=True, fancybox=True)
          
ax.set_axis_off() # if you don't want the axis		                
ax.figure.show()