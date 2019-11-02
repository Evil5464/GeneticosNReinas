#! /usr/bin/python3

import random
from time import time


	

def algoritmoGenetico(poblacion_inicial):
	poblacion = poblacion_inicial
	repite=True#indica si el algoritmo no ha econtrado el optimo
	ciclos = 1

	while (repite):#repite el algoritomo hasta encontrar el optimo
		nueva_poblacion = [] #La nueva población esta vacia por el momento
		for i in range(0,tam_poblacion):
			x = selec_aleatoria(poblacion)
			y = selec_aleatoria(poblacion)
#			print("seleccion aleatoria de X y Y")
#			print(x, y)
#			print("reproducir hijo")
			hijo1 = reproducir(x, y)
#			print(hijo1)
#			print("mutacion")
			if random.random()>umbralMuta:
				hijo1 = mutar(hijo1)
#			print("hijo mutado")
#			print(hijo1)
			nueva_poblacion.append(hijo1)
		poblacion = nueva_poblacion
		for j in range(0,tam_poblacion):
			if(aux_idoneidad-idoneidad(poblacion[j]) == aux_idoneidad):
				print("numero de ciclos necesarios: ", ciclos)
				return poblacion[j]
		ciclos = ciclos + 1
#		repite = False
#	return poblacion[j]

def idoneidad(candidato):
	contDA1 = 0
	contDA2 = 0
	contDB1 = 0
	contDB2 = 0
	idoGlobal = 0
	
	#contamos las coinsidencias en el mismo renglon
	for i in range(0, num_reinas):
		auxcont = candidato.count(i) #cuenta coinsidencias en el condidato por renglon
		if auxcont>1: #si son mas de dos entonces se atacan
			idoGlobal = idoGlobal + auxcont
	
	#contamos las reinas que se atacan en diagonal hacia arriba
	for i in range(0, num_reinas):
		auxcont = 0
		for j in range(0,i+1):
			if candidato[j] == i-j:
				auxcont = auxcont +1
		if auxcont>1:
			contDA1 = contDA1 + auxcont
	
	for k in range(1, num_reinas):
		auxcont = 0
		i = num_reinas - k
		for j in range(i, num_reinas):
			if candidato[j] == (num_reinas-1) - (j-i):
				auxcont = auxcont +1
		if auxcont>1:
			contDA2 = contDA2 + auxcont
	#contamos las reinas que se atacan en diagonal hacia arriba
	for i in range(0, num_reinas):
		auxcont = 0
		for j in range(0, num_reinas):
			if candidato[j] == (num_reinas-1)-(i-j):
				auxcont = auxcont +1
		if auxcont>1:
			contDB1 = contDB1 + auxcont

	for i in range(1, num_reinas):
		auxcont = 0
		for j in range(i, num_reinas):
			if candidato[j] == j-i:
				auxcont = auxcont + 1
		if auxcont > 1:
			contDB2 = contDB2 + auxcont

#	print(idoGlobal, contDA1, contDA2, contDB1, contDB2)
	idoGlobal = idoGlobal + contDA1 + contDA2 + contDB1 + contDB2

	return idoGlobal

def selec_aleatoria(poblacion):
	lista = []
	for i in range(0, tam_poblacion):
		ido = aux_idoneidad-idoneidad(poblacion[i])
		for j in range(0, ido):
			lista.append(poblacion[i]) #dependiendo de la idoneidad se repite el elemento en la lista
#	print("imprime lista generada")
#	for h in range(0,len(lista)):
#		print(lista[h])
	return random.choice(lista)		

def reproducir(x, y):
	hijo = []
	c = random.randint(0, len(x))
#	print("	valor de c: ", c)
	for i in range(0, c):
		hijo.append(x[i])
	for j in range(c,len(x)):
		hijo.append(y[j])
	return hijo

def mutar(hijo):
	c = random.randint(0,len(hijo)-1)
#	print("numero a mutar")
#	print(c)
	hijo[c] = random.randint(0, num_reinas-1)
	return hijo


print("Inicia el programa de n-reinas genetico")
num_reinas = 8
tam_poblacion = 50
umbralMuta = 0.6
aux_idoneidad = num_reinas*3
print("Numero de reinas = ", num_reinas)
print("tam_poblacion = ", tam_poblacion)
print("umbralMuta = ", umbralMuta)
tiempo_inicial = time()


poblacion_inicial = []#Lista vacia de la población inicial
#print("Imprime poblacion inicial")
for p in range(0,tam_poblacion):
	propuesta = [] 
	for q in range(0,num_reinas):
		pass
		pos_reina = random.randint(0, num_reinas-1) #posición aleatoria de la reina
		propuesta.append(pos_reina)
	poblacion_inicial.append(propuesta)
#	print(propuesta)

optimo = algoritmoGenetico(poblacion_inicial)

#result = algoritmoGenetico(poblacion_inicial, num_reinas)#población inicial con idoneidad = tam, ninguna se ataca
#print("La combinacón idonea es: ", result)
#candidato = [0, 1, 0, 0, 1]
#print(candidato)
#print(idoneidad(candidato))
print("optimo")
print(optimo)
print("idoneidad inversa")
print(aux_idoneidad-idoneidad(optimo))
tiempo_final = time()
print("El tiempo total de ejecución es: ", tiempo_final - tiempo_inicial)
