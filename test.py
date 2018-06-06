# -*- coding: utf-8 -*-
import re
import sys
import os
import glob


if __name__ == '__main__':

	# CHEQUEAR VERSION DE PYTHON
	if (sys.version_info.major != 3 ) or (sys.version_info.minor != 6):
		print("Está usando la versión de Python: "+str(sys.version))
		sys.exit("Pero debe usar la versión de Python 3.6.X")
	
	# VEFIFICAR QUE EXISTA EL DIRECTORIO SALIDAS
	try:
		os.stat("salidas")
	except:
		os.mkdir("salidas")
	
	# ITERAR SOBRE TODAS LAS ENTRADAS
	errores = 0;

	for archEntrada in sorted(glob.glob('entradas'+os.sep+'entrada*.txt')):

		# OBTENER LOS NOMBRES DE ARCHIVOS
		s = re.search(r"(entrada\d+)", archEntrada, flags=0)
		entrada = s.group(1)
		archSalida = "salidas" + os.sep + "salida_" + entrada + ".txt"
		archSalidaOficial = "salidas_oficiales" + os.sep + "salida_" + entrada + ".txt"

		# EJECUTAR EL PROGRAMA
		print("\n\n### Entrada: "+entrada+" ###\n")
		ejecutar = "python main.py " + archEntrada + " " + archSalida
		print(ejecutar)
		x = os.system(ejecutar)
		if x != 0:
		   print ("ERROR: Error de ejecución al procesar "+entrada)
		   errores = errores + 1

		else:
		    # COMPARAR LAS SALIDAS
			diferencias = "diff --strip-trailing-cr " + archSalida + " " + archSalidaOficial 
			print(diferencias)
			x = os.system(diferencias)		
			if x != 0:
				print("ERROR: Los archivos de salida: "+archSalida+" y "+archSalidaOficial+" no son iguales")
				errores = errores + 1
			else:
				print("OK")
	
	# MOSTRAR RESULTADO
	if errores == 0:
		print("\nResultado: todos los test OK!!")
	else:
		print("\nResultado: "+str(errores)+" error/es.")
