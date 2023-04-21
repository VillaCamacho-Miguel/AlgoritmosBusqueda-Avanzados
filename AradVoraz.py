#CLASE ESTADO
from audioop import reverse


class estado:

    def __init__(self, nombre,distanceBucharest):
        self.nombre = nombre
        G.add_node(nombre)
        self.distanceBucharest = distanceBucharest
        self.offspring = []
    def getDistanceBucharest(self):
        return self.distanceBucharest
    def getOffspring(self):
        return self.offspring
    def setOffspring(self, offspring):
        self.offspring = offspring
        for x in self.offspring:
            G.add_edge(self.nombre, x.nombre)
         
def B_A(F):
    if(len(F) == 0):
            exit()
    E_a = F.pop(0) 
    print(E_a.nombre + " -> ")
    if(Goaltest(E_a)):
        TerminarPrograma()
    else:        
        OS = Expand(E_a)
#        OS = Evalua(OS)
        F = F+OS #Para busqueda larga seria OS.extend(F).
        F.sort(key = lambda x: x.getDistanceBucharest(), reverse = False)
        listOptimo.append(F[0].nombre)
        for x in F:
            print(x.nombre)
        F = [F[0]]
        
    B_A(F)


def Goaltest(E_a):
    return E_a.nombre ==  E_f.nombre

def Expand(E_A):
    OS = []
    for x in E_A.offspring:
        OS.append(x)
    return OS

def TerminarPrograma():
    dibuja()
    print("Se encontro el elemento")
    exit()

def dibuja():
    color_map = []
    for x in G:
        if x in listOptimo and x!= E_f.nombre and x != E_i.nombre:
            color_map.append('blue')
        elif x == E_f.nombre or x == E_i.nombre:
            color_map.append('red')
        else: 
            color_map.append('green')      
    nx.draw(G, node_color=color_map, with_labels = 1)
    plt.show()
 

import matplotlib.pyplot as plt
import networkx as nx
listOptimo = []
G = nx.Graph()

#ESTA ES LA REPRESENTACION DEL DIAGRAMA
Arad = estado("Arad",366)
Zerind = estado("Zerind",374)
Oradea = estado("Oradea",380)
Timisoara = estado("Timisoara",329)
Lugoj = estado("Lugoj",244)
Mehadia = estado("Mehadia",241)
Dobreta = estado("Dobreta",242)
Craiova = estado("Craiova",160)
Sibiu = estado("Sibiu",253)
RimnicuVilcea = estado("RimnicuVilcea",193)
Fagaras = estado("Fagaras",178)
Pitesti = estado("Pitesti",98)
Bucharest = estado("Bucharest",0)
Urziceni = estado("Urziceni",80)
Neamt = estado("Neamt",234)
#Rinova = estado("Rinova",)
Vaslui = estado("Vaslui",199)
Eforie= estado("Eforie",161)
Lasi = estado("Lasi",226)
Giurgui = estado("Giurgiu",77)
Hirsova = estado("Hirsova",151)

Arad.setOffspring([Zerind,Sibiu,Timisoara])
Zerind.setOffspring([Arad,Oradea])
Oradea.setOffspring([Zerind,Sibiu])
Sibiu.setOffspring([Arad,Oradea,Fagaras,RimnicuVilcea])
Timisoara.setOffspring([Arad,Lugoj])
Fagaras.setOffspring([Sibiu,Bucharest])
RimnicuVilcea.setOffspring([Sibiu, Craiova, Pitesti])
Pitesti.setOffspring([ RimnicuVilcea, Craiova, Bucharest])
Timisoara.setOffspring([Arad, Lugoj])
Lugoj.setOffspring([Timisoara, Mehadia])
Mehadia.setOffspring([Lugoj, Dobreta])
Dobreta.setOffspring([Mehadia, Craiova])
Craiova.setOffspring([Dobreta, RimnicuVilcea, Pitesti])
Bucharest.setOffspring([Fagaras, Pitesti, Giurgui, Urziceni])
Giurgui.setOffspring([Bucharest])
Urziceni.setOffspring([Bucharest, Vaslui, Hirsova ])
Hirsova.setOffspring([Urziceni, Eforie])
Eforie.setOffspring([Hirsova])
Vaslui.setOffspring([Urziceni, Lasi])
Lasi.setOffspring([Vaslui, Neamt])
Neamt.setOffspring([Lasi])

##ALGORITMO##
'''
E_i = {Arad}
F = {E_i}

B_A(F)
E_A = F.pop()
if(Goltest(E_A))
    //termina
else
    OS = Expand(E_A)
    F=Append(F,OS)
    B_A(F)
'''

E_i = Arad
listOptimo.append(E_i.nombre)
E_f = Bucharest
F = [E_i]
B_A(F)