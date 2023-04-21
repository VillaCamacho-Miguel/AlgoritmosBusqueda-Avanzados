
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

def B_P(F):
    
    if(len(F) == 0):
            print("no se encontro el elemento")
            exit()
    else:
        E_a = F.pop(0) 
        print(E_a)
        if(Goaltest(E_a)):
            muestraResultado(E_a)
            TerminarPrograma()
        else:
            OS = Expand(E_a)
            F = OS+F
    B_P(F)

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

from CodOptimizado.Utilerias import *
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(15000)
listaNegra = []  
E_I = preguntar()
F = [E_I]
B_P(F)