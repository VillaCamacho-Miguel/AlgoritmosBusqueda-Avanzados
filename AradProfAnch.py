#CLASE ESTADO
class estado:

    def __init__(self, nombre):
        self.nombre = nombre
        G.add_node(nombre)
        self.visitado = False
        self.offspring = []
        
    def setOffspring(self, offspring):
        self.offspring = offspring
        for x in self.offspring:
            G.add_edge(self.nombre, x.nombre)
            
    def setVisitado(self, visitado):
        self.visitado = visitado

def B_A(F):
    E_a = F.pop(0) 
    print(E_a.nombre + " -> ")
    if(Goaltest(E_a)):
        TerminarPrograma()
    else:
        OS = Expand(E_a)
        F.extend(OS) 
        listOptimo.append(E_a.nombre)
        if(len(F) == 0):
            print("no se encontro el elemento")
            exit()
        B_A(F)


def Goaltest(E_a):
    return E_a ==  E_f

def Expand(E_A):
    OS = []
    for x in E_A.offspring:
        if  x.visitado == False:
            x.visitado = True
            OS.append(x)
    return OS

def TerminarPrograma():
    print("Se encontro el elemento")
    dibuja()
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
Arad = estado("Arad")
Zerind = estado("Zerind")
Oradea = estado("Oradea")
Timisoara = estado("Timisoara")
Lugoj = estado("Lugoj")
Mehadia = estado("Mehadia")
Dobreta = estado("Dobreta")
Craiova = estado("Craiova")
Sibiu = estado("Sibiu")
RimnicuVilcea = estado("RimnicuVilcea")
Fagaras = estado("Fagaras")
Pitesti = estado("Pitesti")
Bucharest = estado("Bucharest")
Urziceni = estado("Urziceni")
Neamt = estado("Neamt")
Vaslui = estado("Vaslui")
Eforie= estado("Eforie")
Lasi = estado("Lasi")
Giurgui = estado("Giurgiu")
Mirsova = estado("Mirsova")

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
Urziceni.setOffspring([Bucharest, Vaslui, Mirsova ])
Mirsova.setOffspring([Urziceni, Eforie])
Eforie.setOffspring([Mirsova])
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
E_i.setVisitado(True)
E_f = Bucharest
F = [E_i]
B_A(F)