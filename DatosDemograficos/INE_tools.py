import requests
import json
import matplotlib
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

from settings import *

####################################################################
#Función principal que se encarga de crear el gráfico adecuado	 
####################################################################
def INEDataBase(filtro):

	resultado =  "Filtro no válido"
	
	if( filtro == TOTAL_POB_MAPA):
		resultado = totalPobMapa()
	elif (filtro == HOMBRE_POB_MAPA):
		resultado = homPobMapa()
	elif (filtro == MUJER_POB_MAPA):
		resultado = mujPobMapa()
	elif (filtro == TOTAL_POB_BAR):
		resultado = totalPobBar()
	elif (filtro == HOMBRE_POB_BAR):
		resultado = homPobBar()
	elif (filtro == MUJER_POB_BAR):
		resultado = mujPobBar()
	elif (filtro == AMBOS_POB_BAR):
		resultado = ambosPobBar()
			
	return resultado

####################################################################
# Función para guardar la población total en un mapa
####################################################################
def totalPobMapa():
	# Obtenemos la información de la URL
	try:
		info = requests.get(URL_POBLACION)
		jsonInfo = json.loads(info.text)
	
		# Nos quedamos con la población total en cada provincia
		poblacion = []
		for i in range(INI_INFO_TOTAL, FIN_INFO_TOTAL, INCREMENTO):
			poblacion.append(jsonInfo[i]["Data"][0]["Valor"] / 100000.0)

		# Leemos el geojson e incluimos la nueva columna
		m = "geojson/spain-provinces.geojson"
		map_data = gpd.read_file(m)
		map_data['POB2020'] = 0.0
		
		# Incluimos la información
		for i in range(len(TRADUCTOR)):
			map_data.loc[TRADUCTOR[i],'POB2020'] = poblacion[i]
		
		#Dibujamos el mapa
		fig, ax = plt.subplots(1, 1, figsize=(10, 10)) 
		# Control del encuadre (área geográfica) del mapa
		ax.axis([-12, 5, 32, 48])
		# Control del título y los ejes
		ax.set_title('Población total por provincias en 2020 (en 100 000 habitantes)', 
			     pad = 20, 
			     fontdict={'fontsize':20, 'color': '#4873ab'})
		ax.set_xlabel('Longitud')
		ax.set_ylabel('Latitud')
		 
		# Añadir la leyenda separada del mapa
		divider = make_axes_locatable(ax)
		cax = divider.append_axes("right", size="5%", pad=0.2)
		 
		# Generar y cargar el mapa
		map_data.plot(column='POB2020', cmap='plasma', ax=ax,
			      legend=True, cax=cax, zorder=5)
		
		plt.savefig("fig/total_pob_mapa.png")
		
		return "Mapa guardado con éxito. Búsqueda por: total población mapa"
		
	except requests.exceptions.RequestException as e: 
    		raise SystemExit(e)
    		
    		
    		
####################################################################
# Función para guardar la población total de hombres en un mapa
####################################################################
def homPobMapa():
	# Obtenemos la información de la URL
	try:
		info = requests.get(URL_POBLACION)
		jsonInfo = json.loads(info.text)
	
		# Nos quedamos con la población total en cada provincia
		poblacion = []
		for i in range(INI_INFO_TOTAL, FIN_INFO_TOTAL, INCREMENTO):
			poblacion.append(jsonInfo[i+ACCESO_HOMBRES]["Data"][0]["Valor"] / 100000.0)

		# Leemos el geojson e incluimos la nueva columna
		m = "geojson/spain-provinces.geojson"
		map_data = gpd.read_file(m)
		map_data['POB2020'] = 0.0
		
		# Incluimos la información
		for i in range(len(TRADUCTOR)):
			map_data.loc[TRADUCTOR[i],'POB2020'] = poblacion[i]
		
		#Dibujamos el mapa
		fig, ax = plt.subplots(1, 1, figsize=(10, 10)) 
		# Control del encuadre (área geográfica) del mapa
		ax.axis([-12, 5, 32, 48])
		# Control del título y los ejes
		ax.set_title('Población hombres por provincias en 2020 (en 100 000 habitantes)', 
			     pad = 20, 
			     fontdict={'fontsize':20, 'color': '#4873ab'})
		ax.set_xlabel('Longitud')
		ax.set_ylabel('Latitud')
		 
		# Añadir la leyenda separada del mapa
		divider = make_axes_locatable(ax)
		cax = divider.append_axes("right", size="5%", pad=0.2)
		 
		# Generar y cargar el mapa
		map_data.plot(column='POB2020', cmap='plasma', ax=ax,
			      legend=True, cax=cax, zorder=5)
	
		plt.savefig("fig/hom_pob_mapa.png")
		
		return "Mapa guardado con éxito. Búsqueda por: total población hombres mapa"
		
	except requests.exceptions.RequestException as e: 
    		raise SystemExit(e)

####################################################################
# Función para guardar la población total de hombres en un mapa
####################################################################
def mujPobMapa():
	# Obtenemos la información de la URL
	try:
		info = requests.get(URL_POBLACION)
		jsonInfo = json.loads(info.text)
	
		# Nos quedamos con la población total en cada provincia
		poblacion = []
		for i in range(INI_INFO_TOTAL, FIN_INFO_TOTAL, INCREMENTO):
			poblacion.append(jsonInfo[i+ACCESO_MUJERES]["Data"][0]["Valor"] / 100000.0)

		# Leemos el geojson e incluimos la nueva columna
		m = "geojson/spain-provinces.geojson"
		map_data = gpd.read_file(m)
		map_data['POB2020'] = 0.0
		
		# Incluimos la información
		for i in range(len(TRADUCTOR)):
			map_data.loc[TRADUCTOR[i],'POB2020'] = poblacion[i]
		
		#Dibujamos el mapa
		fig, ax = plt.subplots(1, 1, figsize=(10, 10)) 
		# Control del encuadre (área geográfica) del mapa
		ax.axis([-12, 5, 32, 48])
		# Control del título y los ejes
		ax.set_title('Población mujeres por provincias en 2020 (en 100 000 habitantes)', 
			     pad = 20, 
			     fontdict={'fontsize':20, 'color': '#4873ab'})
		ax.set_xlabel('Longitud')
		ax.set_ylabel('Latitud')
		 
		# Añadir la leyenda separada del mapa
		divider = make_axes_locatable(ax)
		cax = divider.append_axes("right", size="5%", pad=0.2)
		 
		# Generar y cargar el mapa
		map_data.plot(column='POB2020', cmap='plasma', ax=ax,
			      legend=True, cax=cax, zorder=5)

		plt.savefig("fig/muj_pob_mapa.png")
		
		return "Mapa guardado con éxito. Búsqueda por: total población mujeres mapa"
		
	except requests.exceptions.RequestException as e: 
    		raise SystemExit(e)

####################################################################    		
# Función para guardar la población total en un gráfico de barras
####################################################################
def totalPobBar():
	# Obtenemos la información de la URL
	try:
		info = requests.get(URL_POBLACION)
		jsonInfo = json.loads(info.text)
	
		# Nos quedamos con la población total en cada provincia y sus nombres
		ciudades = []
		poblacion = []
		for i in range(3,151,3): 
			completo  = jsonInfo[i]["Nombre"] 
			completo = completo[completo.find(".") + 2:]
			completo = completo[:completo.find(".")]
			ciudades.append(completo)
			poblacion.append(jsonInfo[i]["Data"][0]["Valor"]/100000)

		y_pos = np.arange(len(ciudades))

		# Dibujamos el gráfico
		fig, ax = plt.subplots(1, 1, figsize=(10, 8))
		ax.barh(y_pos, poblacion, align='center', alpha=0.5, height = 0.8)
		ax.set_yticks(y_pos)
		ax.set_yticklabels(ciudades, size=7)
		ax.set_xscale('linear')
		#ax.set_xlim(left=0, right=2000000)
		ax.set_xlabel('Población (en 100 000 habitantes)')

		plt.title('Población total por provincias')
		plt.savefig("fig/total_pob_bar.png")
		
		return "Mapa guardado con éxito. Búsqueda por: total población barras"
		
	except requests.exceptions.RequestException as e: 
    		raise SystemExit(e)

####################################################################    		
# Función para guardar la población hombres en un gráfico de barras
####################################################################
def homPobBar():
	# Obtenemos la información de la URL
	try:
		info = requests.get(URL_POBLACION)
		jsonInfo = json.loads(info.text)
	
		# Nos quedamos con la población total en cada provincia y sus nombres
		ciudades = []
		poblacion = []
		for i in range(3,151,3): 
			completo  = jsonInfo[i]["Nombre"] 
			completo = completo[completo.find(".") + 2:]
			completo = completo[:completo.find(".")]
			ciudades.append(completo)
			poblacion.append(jsonInfo[i+ACCESO_HOMBRES]["Data"][0]["Valor"]/100000)

		y_pos = np.arange(len(ciudades))

		# Dibujamos el gráfico
		fig, ax = plt.subplots(1, 1, figsize=(10, 8))
		ax.barh(y_pos, poblacion, align='center', alpha=0.5, height = 0.8)
		ax.set_yticks(y_pos)
		ax.set_yticklabels(ciudades, size=7)
		ax.set_xscale('linear')
		#ax.set_xlim(left=0, right=2000000)
		ax.set_xlabel('Población (en 100 000 habitantes)')

		plt.title('Población hombres por provincias')
		plt.savefig("fig/hom_pob_bar.png")
		
		return "Mapa guardado con éxito. Búsqueda por: hombres población barras"
		
	except requests.exceptions.RequestException as e: 
    		raise SystemExit(e)

####################################################################    		
# Función para guardar la población mujeres en un gráfico de barras
####################################################################
def mujPobBar():
	# Obtenemos la información de la URL
	try:
		info = requests.get(URL_POBLACION)
		jsonInfo = json.loads(info.text)
	
		# Nos quedamos con la población total en cada provincia y sus nombres
		ciudades = []
		poblacion = []
		for i in range(3,151,3): 
			completo  = jsonInfo[i]["Nombre"] 
			completo = completo[completo.find(".") + 2:]
			completo = completo[:completo.find(".")]
			ciudades.append(completo)
			poblacion.append(jsonInfo[i+ACCESO_MUJERES]["Data"][0]["Valor"]/100000)

		y_pos = np.arange(len(ciudades))

		# Dibujamos el gráfico
		fig, ax = plt.subplots(1, 1, figsize=(10, 8))
		ax.barh(y_pos, poblacion, align='center', alpha=0.5, height = 0.8)
		ax.set_yticks(y_pos)
		ax.set_yticklabels(ciudades, size=7)
		ax.set_xscale('linear')
		#ax.set_xlim(left=0, right=2000000)
		ax.set_xlabel('Población (en 100 000 habitantes)')

		plt.title('Población mujeres por provincias')
		plt.savefig("fig/muj_pob_bar.png")
		
		return "Mapa guardado con éxito. Búsqueda por: mujeres población barras"
		
	except requests.exceptions.RequestException as e: 
    		raise SystemExit(e)
    		

####################################################################    		
# Función para guardar la población hombres/mujeres en un gráfico de barras
####################################################################
def ambosPobBar():
	# Obtenemos la información de la URL
	try:
		info = requests.get(URL_POBLACION)
		jsonInfo = json.loads(info.text)
	
		# Nos quedamos con la población total en cada provincia y sus nombres
		ciudades = []
		poblacion_hom = []
		poblacion_muj = []
		for i in range(3,151,3): 
			completo  = jsonInfo[i]["Nombre"] 
			completo = completo[completo.find(".") + 2:]
			completo = completo[:completo.find(".")]
			ciudades.append(completo)
			poblacion_hom.append(jsonInfo[i + ACCESO_HOMBRES]["Data"][0]["Valor"]/100000.0)
			poblacion_muj.append(jsonInfo[i + ACCESO_MUJERES]["Data"][0]["Valor"]/100000.0)

		y_pos = np.arange(len(ciudades))

		# Dibujamos el gráfico
		y_pos = np.arange(len(ciudades))
		y_pos *= 2 # Para separar más las barras
			
		width = 0.85  # the width of the bars
		
		fig, ax = plt.subplots(1, 1, figsize=(10, 10))
		ax.barh(y_pos - width/2, poblacion_hom, width, label='Hombres')
		ax.barh(y_pos + width/2, poblacion_muj, width, label='Mujeres')
		
		# Add some text for labels, title and custom x-axis tick labels, etc.
		ax.set_xlabel('Población (100 000)')
		ax.set_yticks(y_pos)
		ax.set_yticklabels(ciudades, size = 7)
		ax.legend()

		plt.title('Población hombres/mujeres por provincias')
		plt.savefig("fig/ambos_pob_bar.png")
		
		return "Mapa guardado con éxito. Búsqueda por: hombres/mujeres población barras"
		
	except requests.exceptions.RequestException as e: 
    		raise SystemExit(e)
