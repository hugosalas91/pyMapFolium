#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import folium
import random

def hex_code_colors():
    a = hex(random.randrange(0,256))
    b = hex(random.randrange(0,256))
    c = hex(random.randrange(0,256))
    a = a[2:]
    b = b[2:]
    c = c[2:]
    if len(a)<2:
        a = "0" + a
    if len(b)<2:
        b = "0" + b
    if len(c)<2:
        c = "0" + c
    z = a + b + c
    return "#" + z.upper()

def main():
	sectors = {}
	map_1 = folium.Map(location=[43.357635062481116, -5.847971154492139], zoom_start=8, tiles='OpenStreetMap')
	frame = pd.read_csv('data_results.csv', sep=';')
	for idx, row in frame.iterrows():
		if str(row['latitude']) == "nan":
			#latitud = random.uniform(43.241789682006626, 43.45848969135412)
			#longitud = random.uniform(-6.71536806640618, -5.05368593749993)
			latitud = 43.241789682006626
			longitud = -6.71536806640618
		else:
			latitud = float(row['latitude'].replace(",","."))
			longitud = float(row['longitude'].replace(",","."))
		#map_1.simple_marker([latitud, longitud], popup=row['Empresa'])
		if sectors.has_key(str(row['CNAECodigo'])) == False:
			sectors[str(row['CNAECodigo'])] = hex_code_colors()
		
		if row['approximation'] == 1:
			map_1.polygon_marker(location=[latitud, longitud], popup=row['Empresa']+"; "+row['CNAEdescripcion'], fill_color=sectors[str(row['CNAECodigo'])], num_sides=6, radius=10, rotation=60)
		elif row['approximation'] == 2:
			map_1.polygon_marker(location=[latitud, longitud], popup=row['Empresa']+"; "+row['CNAEdescripcion'], fill_color=sectors[str(row['CNAECodigo'])], num_sides=4, radius=10, rotation=60)
		else:
			map_1.polygon_marker(location=[latitud, longitud], popup=row['Empresa']+"; "+row['CNAEdescripcion'], fill_color=sectors[str(row['CNAECodigo'])], num_sides=3, radius=10, rotation=60)
	map_1.create_map(path='osm.html')

if __name__ == "__main__":
    main()