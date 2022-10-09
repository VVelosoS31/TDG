from cmath import inf


class Graph:   
   def __init__(self, vertices):
      self.V = vertices 
      self.graph = [] 


   def addEdge(self, u, v, w):
      self.graph.append([u,v,w])
      self.graph.append([v,u,w])
   
   
   def distancia_minima(self, dist, T):
      min = inf

      for v in range(self.V):
         if dist[v] < min and T[v]==False:
            min = dist[v]
            min_index = v

      return min_index
   
   
   def dijsktra(self, vertice_inicial):
      dist = [inf]* self.V 
      dist[vertice_inicial] = 0 
      T = [False] * self.V 

      for count in range(self.V):
         u = self.distancia_minima(dist, T)
         for v in range(self.V):            
            for item in self.graph:
               if (item[0]==u) and (item[1]==v):
                  if item[2] > 0 and T[v]==False and dist[v] > dist[u]+item[2]:
                     dist[v] = dist[u]+item[2]
         T[u] = True

      print("Vertice\t Peso")
      for node in range(self.V):
         print(f'{node} \t {dist[node]}')


'''
GRAFO AULA 5 SLIDE 19
0-a
1-b
2-d
3-z
4-e
5-c
'''

g = Graph(6)
g.addEdge(0, 1, 2)
g.addEdge(0, 5, 3)
g.addEdge(1, 2, 5)
g.addEdge(1, 4, 2)
g.addEdge(2, 3, 2)
g.addEdge(2, 4, 1)
g.addEdge(3, 4, 4)
g.addEdge(4, 5, 5)
g.dijsktra(0)

