from collections import defaultdict
  

class Grafo:
  
    def __init__(self,vertices):
        self.V= vertices 
        self.grafo = defaultdict(list) 
  
    def addEdge(self,u,v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)
  
    def DFSUtil(self,v,v_visitado):
        v_visitado[v]= True
 
        for i in self.grafo[v]:
            if v_visitado[i]==False:
                self.DFSUtil(i,v_visitado)
  

    def are_connected(self):

        v_visitado =[False]*(self.V)
 

        for i in range(self.V):
            if len(self.grafo[i]) > 1:
                break
 

        if i == self.V-1:
            return True
 

        self.DFSUtil(i,v_visitado)
 

        for i in range(self.V):
            if v_visitado[i]==False and len(self.grafo[i]) > 0:
                return False
         
        return True
 
 
    '''
       0 - Grafo não Euleriano
       1 - Há um caminho Euleriano
       2 - Há um cliclo Euleriano
    '''
    def euler(self):
        
        if self.are_connected() == False:
            return 0
        else:
            
            count = 0
            for i in range(self.V):
                if len(self.grafo[i]) % 2 !=0:
                    count +=1

        if count == 0:
            return 'Há um ciclo de Euler'
        elif count == 2:
            return 'Há um caminho de Euler'
        else:
            return 'Não há um ciclo nem caminho de Euler'
  

""" GRAFO AC2 Ex1 A """
g = Grafo(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,4)
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
print(g.euler())


""" GRAFO AULA 5 SLIDE 13 """
g1 = Grafo(6)
g1.addEdge(0,1)
g1.addEdge(0,5)
g1.addEdge(1,2)
g1.addEdge(2,3)
g1.addEdge(3,4)
g1.addEdge(3,5)
print(g1.euler())


""" GRAFO AULA 3 SLIDE 18 """
g2 = Grafo(10)
g2.addEdge(0,9)
g2.addEdge(0,1)
g2.addEdge(1,2)
g2.addEdge(1,9)
g2.addEdge(1,6)
g2.addEdge(2,3)
g2.addEdge(2,4)
g2.addEdge(2,5)
g2.addEdge(3,4)
g2.addEdge(5,6)
g2.addEdge(6,9)
g2.addEdge(6,7)
g2.addEdge(7,8)
g2.addEdge(8,9)
print(g2.euler())