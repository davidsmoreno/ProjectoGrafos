# -*- coding: utf-8 -*-
"""
@author: Dana Acosta y David Moreno

"""
#Primero vamos a crear una clase grafo la cual nos va a ayudar a representar el grafo del caballo.
class Vertice:
    def __init__ (self, llave): #Vamos a crer la clase Vertice que va a tener una llave un color y una lista de conexiones
        self.id=llave
        self.conectadoa={}
        self.color = 'blanco' #Inicializamos el grafo con el color blanco , el cual el algoritmo lo va a tomar como que es un vertice que no se ha visitado
        
    def addvecino(self,a,peso=0): #agregamoos un vertice al grafo que sea vecino 
        self.conectadoa[a]=peso   
        
    def __str__(self):
        return str(self.id)+'   Conectado a '+ str([i.id for i in self.conectadoa]) #Creamos una función print 
    
    def getConexiones(self):
        return self.conectadoa.keys()  #Funcion get para obtener las coneciones del vertice
    
    def getid(self):
        return self.id    #Fucnion get del id único de cada vertice
    
    def getpeso(self,a):
        return self.conectadoa[a]  #Peso del vertice que siempre va a ser 0

    def setColor(self, color):   #Función de categorizar si un vértice ya fue recorrido
        self.color = color

    def getColor(self):
        return self.color    #Función get color

    
    
class Grafo:
    
    def __init__(self):  
        self.vertList={} #Lista de vertices del grafo
        self.numVertices=0 #Inicializamos el grafo con número de vertices 0
        
    def addVertice(self,llave): #Agregar  un Vértice
        self.numVertices=self.numVertices+1
        newNode=Vertice(llave)
        self.vertList[llave]=newNode
        return newNode

        
    def getVertice(self,i):
    	if i in self.vertList:
    		return self.vertList[i]
    	else:
    		return None

        
    def __contains__(self,n):
        return n in self.vertList
    
    def addArista(self,a,b,c=0):
        if a not in self.vertList:
            self.addVertice(a)
        if b not in self.vertList:
            self.addVertice(b)
        self.vertList[a].addvecino(self.vertList[b],c)


    def __iter__(self):
        return iter(self.vertList.values())



def Movimientos_Legales(x,n): # Función de los movimientos legales del tablero
    if x >= 0 and x < n:
        return True
    else:
        return False



def Idboard(fila,columna,n): # queremos mapear las posiciones (0,0) a (0) (1,0) a 1 (2,0) a 2 y asi sucesivamente para cualquier tablero de ajedrez nxn
	return fila*n+columna


def getMoves(x,y,n):
    Movimientos = []
    MovimientosCaballo = [(-1,-2),(-1,2),(-2,-1),(-2,1),( 1,-2),( 1,2),( 2,-1),( 2,1)] #Movimientos del caballos, el caballo se puede mover uno a la izquierda y dos abajo, uno a la izquierda dos arriba, etc.
    for i in MovimientosCaballo:
        newX = x + i[0]
        newY = y + i[1]
        if Movimientos_Legales(newX,n) and Movimientos_Legales(newY,n):
        	Movimientos.append((newX,newY))
    return Movimientos


def GrafoCaballo(n):
	Cgrafo=Grafo()
	for i in range(n):
		for j in range(n):
			Nodeid=Idboard(i,j,n)
			pos_opciones=getMoves(i,j,n)
			for k in pos_opciones:
				newid=Idboard(k[0],k[1],n)
				Cgrafo.addArista(Nodeid,newid)
	return Cgrafo


def CicloeulerianoCaballo(n,camino,v,limite_Tablero):
    v.setColor('Negro') #Para que el algoritmo sepa que ya visitamos un vertice le vamos a poner el color negro
    camino.append(v)
    if n<limite_Tablero:
        nList=list(v.getConexiones())
        i=0;
        Terminado=False
        while i<len(nList) and not Terminado:
            if nList[i].getColor()=='blanco':
                Terminado=CicloeulerianoCaballo(n+1,camino,nList[i],limite_Tablero)
            i=i+1
        if not Terminado:
            camino.pop()
            v.setColor('blanco')
    else:
        Terminado=True
    return Terminado

# Ahora vamos a imploementar el algoritmo  Warsdorff
    
#Vamos a crear una función que nos diga exactamente el movimiento con menor número de mínimo de grado para para iteración
    
def Warnsdorff(n):#Recive el grafo camino del caballo 
    re = []
    for i in n.getConexiones():
        if i.getColor() == 'blanco':
            c = 0
            for k in i.getConexiones():
                if k.getColor() == 'blanco':
                    c += 1
            re.append((c,i))
    re.sort()
    return [m[1] for m in re]
    
    
    

def CicloeulerianoCaballoWarnsdorff(n,camino,v,limite_Tablero):
    v.setColor('Negro') #Para que el algoritmo sepa que ya visitamos un vertice le vamos a poner el color negro
    camino.append(v)
    if n<limite_Tablero:
        nList=Warnsdorff(v)
        i=0;
        Terminado=False
        while i<len(nList) and not Terminado:
            if nList[i].getColor()=='blanco':
                Terminado=CicloeulerianoCaballoWarnsdorff(n+1,camino,nList[i],limite_Tablero)
            i=i+1
        if not Terminado:
            camino.pop()
            v.setColor('blanco')
    else:
        Terminado=True
    return Terminado

    



        
Caballo = GrafoCaballo(5)  #Grafo del caballo en un tablero 8*8
CicloHamiltoniano = []
CicloHamiltoniano2 = []
Pos_Inicial = Caballo.getVertice(0)


CicloeulerianoCaballo(0,CicloHamiltoniano,Pos_Inicial,24)
print("Cicloeuleriano" )
res=[]
for i in CicloHamiltoniano:
    print(i.getid())
    res.append(i.getid())
    
    
CicloeulerianoCaballoWarnsdorff(0,CicloHamiltoniano2,Pos_Inicial,24)
res1=[]
print(" CicloeulerianoCaballoWarnsdorff" )
for i in CicloHamiltoniano:
    print(i.getid())
    res1.append(i.getid())
    


#Ahora vamos a utilizar el algorimto de 




