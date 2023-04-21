#CLASE ESTADO
class estado:

    def __init__(self, nombre):
        self.nombre = nombre
        self.visitado = False
        self.offspring = []
        self.nivel = 0
    def getNivel(self):
        return self.nivel
    def setNivel(self, nivel):
        self.nivel = nivel
    def setOffspring(self, offspring):
        self.offspring = offspring
    def setVisitado(self, visitado):
        self.visitado = visitado

def B_A(F, limite):
    if(len(F) == 0):
            print(limite," --> ",limite+2)
            return            
    E_a = F.pop(0) 
    print(E_a.nombre + " -> ")
    if(Goaltest(E_a)):
        TerminarPrograma()
    else:
        
        if(E_a.getNivel() < limite):
            OS = Expand(E_a)
            F.extend(OS) #Para busqueda larga seria OS.extend(F).
            F = AsignarNivel(F, E_a.getNivel()+1)
    B_A(F, limite)

def AsignarNivel(F, nivel):
    for x in range(len(F)):
        F[x].setNivel(nivel)
    return F 

def Goaltest(E_a):
    return E_a ==  E_f

def Expand(E_A):
    OS = []
    for x in E_A.offspring:
        if  x not in listaNegra:
            listaNegra.append(x)
            OS.append(x)
    return OS

def TerminarPrograma():
    print("Se encontro el elemento")
    exit()



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
Rinova = estado("Rinova")
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

limite = 2
while(True):
    listaNegra = []
    E_i = Arad
    listaNegra.append(E_i)
    E_f = Lugoj
    
    F = [E_i]
    B_A(F, limite)
    limite = limite+2