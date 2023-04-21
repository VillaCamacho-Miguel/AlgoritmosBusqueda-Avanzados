class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.nivel = 0
    def getElemento(self):
        return self.elemento
    def getNivel(self):
        return self.nivel
    def setNivel(self, nivel):
        self.nivel = nivel

def Expand(V):
    copia = V.copy()
    arregloBi = []
    for x in range(len(V)):
        var = V[x]+1
        if(var > len(V)): 
            continue
        V[x] = var
        if(V not in listaNegra):
            arregloBi.append(V.copy())
            listaNegra.append(V.copy())
        V = copia.copy()
    return arregloBi    

def P_L(F, limite):
    
    if(len(F) == 0):
            print("no se encontro el elemento")
            exit()
    else:
        E_a = F.pop(0) 
        print(E_a.getElemento())
        if(Goaltest(E_a.getElemento())):
            muestraResultado(E_a.getElemento())
            TerminarPrograma()
        else:
            if(E_a.getNivel() < limite):
                OS = Expand(E_a.getElemento())
                OS = AsignarNivel(OS, E_a.getNivel()+1)
                F = F+OS
            #F.extend(OS) #Para busqueda larga seria OS.extend(F).    
        P_L(F, limite)
def AsignarNivel(OS, nivel):
    listNueva = []
    print(nivel)
    for x in range(len(OS)):
        listNueva.append(Nodo(OS[x]))
        listNueva[x].setNivel(nivel)
    return listNueva

def TerminarPrograma():
    print("Se encontro el elemento")
    exit()
#Metodo Ataque
def Ataques(V):
    atq = 0
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            if(V[i] == V[j]):
                atq += 2
            elif abs(i-j) == abs(V[i]-V[j]):
                atq += 2
    return atq

def muestraResultado(E_a):
      
    board = np.zeros((len(E_a),len(E_a),3))
    board += 0.5 
    board[::2, ::2] = 1 
    board[1::2, 1::2] = 1
    for x in range(len(E_a)):
        E_a[x] = E_a[x]-1        
    positions = E_a

    print(E_a)
    fig, ax = plt.subplots(nrows=1, num="Tablero Reinas")
    ax.imshow(board, interpolation='nearest')
    
    for y, x in enumerate(positions):
        ax.text(x, y, u'\u2655', size=30, ha='center', va='center')
    ax.set(xticks=[], yticks=[])
    ax.axis('image')
    plt.show()
    
#Metodo Goaltest
def Goaltest(V):
    return Ataques(V) == 0


import matplotlib.pyplot as plt
import numpy as np
import sys
from CodOptimizado.Utilerias import *
sys.setrecursionlimit(15000)
listaNegra = []  
E_I = Nodo(preguntar())
F = [E_I]
limite = int(input("Proporciona Limite!"))
P_L(F, limite)