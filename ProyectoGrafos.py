# -*- coding: utf-8 -*-
"""
@author: Dana Acosta y David Moreno

"""


#Primero vamos a crear una clase grafo la cual nos va a ayudar a representar el grafo del caballo.


class Vertice:
    def __init__ (self, llave):
        self.id=llave
        self.conectadoa={}
        
    def addvecino(self,a,peso=0): #agregamoos un vertice al grafo que sea vecino 
        self.conectadoa[a]=peso
        
        
    def __str__(self):
        return str(self.id)+'Conectado a '+ str([i.id for i in self.conectadoa])
    
    def getConexiones(self):
        return self.conectadoa.keys()
    
    def getid(self):
        return self.id
    
    def getpeso(self,a):
        return self.conectadoa[a]
    
    
class Grafo:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
        
    def addVertice(self,llave):
        self.numVertices=self.numVertices+1
        newNode=Vertice(llave)
        self.vertLisr[llave]=newNode
        return newNode
    
    def __contains__(self,n):
        return n in self.vertList
    
    def addArista(self,a,b,c=0):
        if a not in self.vertList:
            n=self.addVertice(a)
        if b not in self.vertList:
            n=self.addVertice(b)
        self.vertList[a].addvecino(self.vertList[a],c)
        
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())



    

        
        
        
        
        
