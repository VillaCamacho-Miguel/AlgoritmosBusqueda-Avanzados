#CLASE ESTADO
from audioop import reverse


class estado:

    def __init__(self, nombre,Hx):
        self.nombre = nombre
        self.Fx = 0
        G.add_node(nombre)
        self.Hx = Hx
        self.distanciaActual = 0
        self.offspring = []

    def getHx(self):
        return self.Hx
    def setValuesSpring(self, i,j,v):
        self.offspring[i][j] = v
    def getOffSpring(self):
        return self.offspring
    def setOffSpring(self, offspring):
        self.offspring = offspring
        for x in range(len(self.offspring)):
            G.add_edge(self.nombre, self.offspring[x][0].nombre)
        
#METODO RECURSIVO
def A_Star(F):
    if(len(F) == 0):
            exit()
    E_a = F.pop(0) 
    
    C_A = E_a[0].distanciaActual
    print(E_a[0].nombre,": ",E_a[0].Fx," -> ")
    if(Goaltest(E_a)):
        TerminarPrograma()
    else:        
        OS = Expand(E_a[0])
        OS = Evalua(OS,C_A) 
        F = F+OS 
        F.sort(key = lambda x: x[0].Fx, reverse = False)
        listOptimo.append(E_a[0].nombre)
    A_Star(F)
    
def imprime(F):
    print(len(F))
    for i in range(len(F)):
            print(F[i][0].nombre,"->", F[i][0].Fx)            
       
def Evalua(OS,C_A):
    for i in range(len(OS)):
        if OS[i][0].nombre == "Bucharest":
            if OS[i][0].Fx > (OS[i][1]+OS[i][0].getHx()):
                continue
        OS[i][1] = OS[i][1]+C_A
        OS[i][0].Fx = OS[i][1]+OS[i][0].getHx()
        OS[i][0].distanciaActual = OS[i][1]
    return OS    

def Goaltest(E_a):
    return E_a[0].nombre ==  E_f.nombre

def Expand(E_A):
    OS = E_A.getOffSpring()
    return OS

def TerminarPrograma():
    dibuja()
    print("Se encontro el elemento")
    exit()

def dibuja():
    color_map = []
    for x in G:
        if x in listOptimo and x!= E_f.nombre and x != E_i[0].nombre:
            color_map.append('blue')
        elif x == E_f.nombre or x == E_i[0].nombre:
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
Vaslui = estado("Vaslui",199)
Eforie= estado("Eforie",161)
Lasi = estado("Lasi",226)
Giurgui = estado("Giurgiu",77)
Hirsova = estado("Hirsova",151)

Arad.setOffSpring([[Zerind,75],[Sibiu,140],[Timisoara,118]])
Zerind.setOffSpring([[Arad, 75],[Oradea,71]])
Oradea.setOffSpring([[Zerind,71],[Sibiu,151]])
Sibiu.setOffSpring([[Arad,140],[Oradea,151],[Fagaras,99],[RimnicuVilcea,80]])
Timisoara.setOffSpring([[Arad,118],[Lugoj,111]])
Fagaras.setOffSpring([[Sibiu,99],[Bucharest,211]])
RimnicuVilcea.setOffSpring([[Sibiu,80], [Craiova,146], [Pitesti,97]])
Pitesti.setOffSpring([[RimnicuVilcea,97], [Craiova,138], [Bucharest,101]])
Lugoj.setOffSpring([[Timisoara,111], [Mehadia,70]])
Mehadia.setOffSpring([[Lugoj,70], [Dobreta,75]])
Dobreta.setOffSpring([[Mehadia,75], [Craiova,120]])
Craiova.setOffSpring([[Dobreta,120], [RimnicuVilcea, 146], [Pitesti,138]])
Bucharest.setOffSpring([[Fagaras,211], [Pitesti,101], [Giurgui,90], [Urziceni,85]])
Giurgui.setOffSpring([[Bucharest,90]])
Urziceni.setOffSpring([[Bucharest,85], [Vaslui,142], [Hirsova,98]])
Hirsova.setOffSpring([[Urziceni,98], [Eforie,86]])
Eforie.setOffSpring([[Hirsova,86]])
Vaslui.setOffSpring([[Urziceni,142], [Lasi,92]])
Lasi.setOffSpring([[Vaslui,92], [Neamt,87]])
Neamt.setOffSpring([[Lasi,87]])

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
E_i = [Arad,0]
listOptimo.append(E_i[0].nombre)
E_f = Bucharest
F = [E_i]
A_Star(F)