
#lista de capitales
ListCap = [ 
' Arad ',
' Bucharest ',
' Craiova ',
' Dobreta ',
' Eforie ',
' Fagaras ',
' Giurgiu ',
' Hirsova ',
' Iasi ',
' Lugoj ',
' Mehadia ',
' Neamt ',
' Oradea ',
' Pitesti ',
' Rimnicu_Vilcea ',
' Sibiu ',
' Timisoara ',
' Urziceni ',
' Vaslui ',
' Zerind ',
]
#aqui establecemos los vecinos de cada ciudad
neighboring_cities = {' Arad ': [
' Zerind ',
' Sibiu ', 
' Timisoara ',
],
' Zerind ': [
' Arad ',
' Oradea ',
],
' Oradea ': [
' Zerind ',
' Sibiu ',
],
' Sibiu ': [
' Arad ',
' Oradea ',
' Fagaras ',
' Rimnicu_Vilcea ',
],
' Timisoara ': [
' Arad ',
' Lugoj ',
],
' Fagaras ': [
' Sibiu ',
' Bucharest ',
],
' Rimnicu_Vilcea ': [
' Sibiu ',
' Craiova ',
' Pitesti ',
],
' Pitesti ': [
' Rimnicu_Vilcea ',
' Craiova ',
' Bucharest ',
],
' Lugoj ': [
' Timisoara ',
' Mehadia ',
],
' Mehadia ': [
' Lugoj ',
' Dobreta ',
],
' Dobreta ': [
' Mehadia ',
' Craiova ',
],
' Craiova ': [
' Dobreta ',
' Rimnicu_Vilcea ',
' Pitesti ',
],
' Bucharest ': [
' Fagaras ',
' Pitesti ',
' Giurgiu ',
' Urziceni ',
],
' Giurgiu ': [
' Bucharest ',
],
' Urziceni ': [
' Bucharest ',
' Vaslui ',
' Hirsova ',
],
' Hirsova ': [
' Urziceni ',
' Eforie ',
],
' Eforie ': [
' Hirsova ',
],
' Vaslui ': [
' Urziceni ',
' Lasi ',
],
' Lasi ': [
' Vaslui ',
' Neamt ',
],
' Neamt ': [
' Lasi ',
]
}


cities_list = list(dict.keys(neighboring_cities))

def get_number_by_city(name: str) -> int:
  return cities_list.index(name)

def get_path_cities(path):
  return list(map(lambda pos: cities_list[pos], path))

def get_resume_matrix():
  total_cities = len(cities_list)
  matrix = []
  for index, city_name in enumerate(cities_list):
    matrix.append([])
    for city_connected in neighboring_cities[city_name]:
      matrix[index].append(get_number_by_city(city_connected))

  return matrix

#diccionarios que cada ciudad con sus respectivas heuristicas hacia las demas capitales
distance_to_Bucharest = {
' Arad ': 366 ,
' Bucharest ': 0 ,
' Craiova ': 160 ,
' Dobreta ': 242 ,
' Eforie ': 161 ,
' Fagaras ': 178 ,
' Giurgiu ': 77 ,
' Hirsova ': 151 ,
' Iasi ': 226 ,
' Lugoj ': 244 ,
' Mehadia ': 241 ,
' Neamt ': 234 ,
' Oradea ': 380 ,
' Pitesti ': 98 ,
' Rimnicu_Vilcea ': 193 ,
' Sibiu ': 253 ,
' Timisoara ': 329 ,
' Urziceni ': 80 ,
' Vaslui ': 199 ,
' Zerind ': 374 ,
}
#lista que contiene la ciudad con su respectivo diccionario de heurisitcas
listDHX =  [
[' Bucharest ', distance_to_Bucharest]
]


#diccionario que contiene las respectivas distancias con sus respectivos vecinos de cada ciudad
cities_with_distances = {
' Arad ': [
(' Zerind ', 75 ),
(' Sibiu ', 140 ),
(' Timisoara ', 118 ),
],
' Zerind ': [
(' Arad ', 75 ),
(' Oradea ', 71 ),
],
' Oradea ': [
(' Zerind ', 71 ),
(' Sibiu ', 151 ),
],
' Sibiu ': [
(' Arad ', 140 ),
(' Oradea ', 151 ),
(' Fagaras ', 99 ),
(' Rimnicu_Vilcea ', 80 ),
],
' Timisoara ': [
(' Arad ', 118 ),
(' Lugoj ', 111 ),
],
' Fagaras ': [
(' Sibiu ', 99 ),
(' Bucharest ', 211 ),
],
' Rimnicu_Vilcea ': [
(' Sibiu ', 80 ),
(' Craiova ', 146 ),
(' Pitesti ', 97 ),
],
' Pitesti ': [
(' Rimnicu_Vilcea ', 97 ),
(' Craiova ', 138 ),
(' Bucharest ', 101 ),
],
' Lugoj ': [
(' Timisoara ', 111 ),
(' Mehadia ', 70 ),
],
' Mehadia ': [
(' Lugoj ', 70 ),
(' Dobreta ', 75 ),
],
' Dobreta ': [
(' Mehadia ', 75 ),
(' Craiova ', 120 ),
],
' Craiova ': [
(' Dobreta ', 120 ),
(' Rimnicu_Vilcea ', 146 ),
(' Pitesti ', 138 ),
],
' Bucharest ': [
(' Fagaras ', 211 ),
(' Pitesti ', 101 ),
(' Giurgiu ', 90 ),
(' Urziceni ', 85 ),
],
' Giurgiu ': [
(' Bucharest ', 90 ),
],
' Urziceni ': [
(' Bucharest ', 85 ),
(' Vaslui ', 142 ),
(' Hirsova ', 98 ),
],
' Hirsova ': [
(' Urziceni ', 98 ),
(' Eforie ', 86 ),
],
' Eforie ': [
(' Hirsova ', 86 ),
],
' Vaslui ': [
(' Urziceni ', 142 ),
(' Lasi ', 92 ),
],
' Lasi ': [
(' Vaslui ', 92 ),
(' Neamt ', 87 ),
],
' Neamt ': [
(' Lasi ', 87 ),
],}

def getCiudad():
    ciudad = {}
    ciudadCode = {}
    f = open("Ciudades.txt")
    j = 1
    for i in f.readlines():
        nodo_ciudad_val = i.split()
        ciudad[nodo_ciudad_val[0]] = [int(nodo_ciudad_val[1]), int(nodo_ciudad_val[2])]

        ciudadCode[j] = nodo_ciudad_val[0]
        j += 1

    return ciudad, ciudadCode


def crearGrafo():
    grafo = {}
    file = open("ciudadesGrafo.txt")
    for i in file.readlines():
        node_val = i.split()

        if node_val[0] in grafo and node_val[1] in grafo:
            c = grafo.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            grafo.update({node_val[0]: c})

            c = grafo.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            grafo.update({node_val[1]: c})

        elif node_val[0] in grafo:
            c = grafo.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            grafo.update({node_val[0]: c})

            grafo[node_val[1]] = [[node_val[0], node_val[2]]]

        elif node_val[1] in grafo:
            c = grafo.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            grafo.update({node_val[1]: c})

            grafo[node_val[0]] = [[node_val[1], node_val[2]]]

        else:
            grafo[node_val[0]] = [[node_val[1], node_val[2]]]
            grafo[node_val[1]] = [[node_val[0], node_val[2]]]

    return grafo
def drawMap(ciudad, grafo):
    for i, j in ciudad.items():
        plt.plot(j[0], j[1], "ro")
        plt.annotate(i, (j[0] + 5, j[1]))

        for k in grafo[i]:
            n = ciudad[k[0]]
            plt.plot([j[0], n[0]], [j[1], n[1]], "gray")

    for i in range(len(get_path_cities(path_finded))):
        
        try:
            first = ciudad[get_path_cities(path_finded)[i].strip()]
            secend = ciudad[get_path_cities(path_finded)[i + 1].strip()]

            plt.plot([first[0], secend[0]], [first[1], secend[1]], "green")
        except:
            continue

    print(get_path_cities(path_finded))
    plt.errorbar(1, 1, label="ASTAR", color="blue")
    plt.legend(loc="lower left")

    plt.show()

#matriz de adyacencia
def get_resume_matrix():
  total_cities = len(cities_list)
  matrix = []
  for index, city_name in enumerate(cities_list):
    matrix.append([])
    for city_connected in cities_with_distances[city_name]:
      matrix[index].append((get_number_by_city(city_connected[0]), city_connected[1]))
  return matrix
  #método para calcular el costo de cada camino encontrado
def calcular_distancias(city_list):
  temp=[]
  for i in range(len(city_list)):
    for element in city_list[i]:
      temp.append(element)

  count=0
  c=0
  for i in range (len(temp)-1):
    
    citi_aux=temp[c+1]
    y=cities_with_distances[temp[i]]

    for j in range (len(y)) : 
      if temp[i]==citi_aux:
        c+=1
        break
      if citi_aux == y[j][0]:
        count+=y[j][1]
        c+=1
        break
  return count

import matplotlib.pyplot as plt
import queue
import itertools
import random
import copy
import sys
sys.setrecursionlimit(10000)
class Path:
  def __init__(self, value, distancia_recorrida):
    self.value = value
    self.distancia_recorrida = distancia_recorrida

  def __repr__(self):
    return " -- " + str(self.value) + ', '+ str(self.distancia_recorrida) + ' -- '

#método goal test
def goal_test(path: Path):
  current_city = path.value[-1][0]
  return current_city == goal

def getDistancesHX(str):
  #print(listDHX)
  for x in listDHX:
    
    if x[0] == str:
      return x[1]
  return None


#método expand
def expand(path: Path):
    current_city = path.value[-1][0]
    path_list = path.value

    childs = graph[current_city]
    #print(childs[0])
    paths = []

    for child in childs:
        next_path = list(path_list)
        next_path.append(child)
        distancia_recorrida = sum(j for i, j in path_list)
        distance_next_city = child[1]
        paths.append(Path(next_path, distancia_recorrida + distance_next_city + distances[child[0]]))

    return paths
#método de a estrella
def a_star_search(frontier: list):
  if (len(frontier) == 0):
    return None
  current = frontier.pop(0)
  if goal_test(current):
    return current
  off_spring = expand(current)
  for node in off_spring:
      frontier.insert(0, node)
  frontier.sort(key=lambda x:x.distancia_recorrida)
  return a_star_search(frontier)

#*******************************************************************************************
#aquí escogemos las ciudades que se deben visitar o se pueden generar de manera aleatoria

CaminoMasOptimo = 0
city_start = ' Timisoara '
city_end = ' Bucharest '

start = get_number_by_city(city_start)
goal = get_number_by_city(city_end)
getHX = getDistancesHX(city_end)

distances = [i for i in getHX.values()]
print(distances)


print('El programa inicia en ' + city_start + '(' + str(start) + ')')
print('Busca llegar a ' + city_end + '(' + str(goal) + ')')

graph = get_resume_matrix()
frontier = [ Path([(start, 0)], 0) ]
path = a_star_search(frontier)
path_finded = [i for i, j in path.value]
aux1=[]
if (path == None):
    print('No existe camino de ' + city_start + ' a ' + city_end)
else:
    print('Camino encontrado: ' + str(path_finded))
    print('Camino encontrado: ' + str(get_path_cities(path_finded)))
    aux1.append(get_path_cities(path_finded))
    costo1=calcular_distancias(aux1)
    print("Costo del camino:",costo1)
    grafo = crearGrafo()
    ciudad, codes = getCiudad()
    drawMap(ciudad, grafo)
