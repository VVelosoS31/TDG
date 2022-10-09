from cmath import inf
from itertools import permutations

class Node:
    def __init__(self,value, vizinhos=None, peso = None):
        self.value = value
        if vizinhos is None:
            self.vizinhos = []
        else:
            self.vizinhos = vizinhos
  
    def add_vizinho(self,vizinho):
        self.vizinhos.append(vizinho)
  
class Grafo():
    def __init__(self, cidades = None):
        if cidades is None:
            self.cidades = []
        else:
            self.cidades = cidades

    def add_node(self,value,vizinhos=None):
        self.cidades.append(Node(value,vizinhos))
  
    def find_node(self,value):
        for node in self.cidades:
            if node.value == value:
                return node
        return None
  
    def add_edge(self,value1,value2,peso = 1):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if (node1 is not None) and (node2 is not None):
            node1.add_vizinho((node2,peso))
            node2.add_vizinho((node1,peso))
        else:
            print('Vertices não encontrado')
  
    def are_connected(self,node1,node2):
        node1 = self.find_node(node1)
        node2 = self.find_node(node2)

        for vizinho in node1.vizinhos:
            if vizinho[0].value == node2.value:
                return True
        return False

def Caixeiro_Viajante(cidades, start, g : Grafo):
    vertex = []

    for i in cidades:
        if i != start:
            vertex.append(i)

    caminho_minimo = inf
    next_permutation = Delete_caminho(list(permutations(vertex)),g,start)

    for perm in next_permutation:
        caminho = tuple(['Denver'] + list(perm) + ['Denver'])
        peso_atual = 0
        k = start
        n = None
        for j in range(len(perm)):
            n = g.find_node(k).vizinhos
            peso_atual += Find_Vizinho(n,perm[j])[1]
            k = perm[j]
        n = g.find_node(k).vizinhos
        if g.are_connected(k,start):
            peso_atual += Find_Vizinho(n,start)[1]
            caminho_minimo = min(caminho_minimo, peso_atual)

    return (caminho_minimo,caminho)

def Find_Vizinho(vizinhos,value):
    for n in vizinhos:
        if n[0].value == value:
            return n
    return None

def Delete_caminho(permutations : list, g, start):
    permNew = []
    for perm in permutations:
        connected = True
        if not g.are_connected(start,perm[0]):
            connected = False
        for i in range(len(perm) - 1):
            if not g.are_connected(perm[i],perm[i+1]):
                connected = False
                break
        if not g.are_connected(perm[len(perm)-1],start):
            connected = False
        if connected:
            permNew.append(perm)
    return permNew

g = Grafo()


cidades = ['Denver', 'San Francisco', 'Los Angeles', 'Dallas', 'Chicago', 'Boston', 'New York']

for i in cidades:
    g.add_node(i)
g.add_edge('Denver','San Francisco',957)
g.add_edge('Denver','Dallas',645)
g.add_edge('Denver','Chicago',908)
g.add_edge('San Francisco','Chicago',1855)
g.add_edge('San Francisco','Los Angeles',349)
g.add_edge('Los Angeles','Chicago',1736)
g.add_edge('Los Angeles','Dallas',1235)
g.add_edge('Dallas','Chicago',798)
g.add_edge('Dallas','New York',1372)
g.add_edge('Chicago','Boston',860)
g.add_edge('Chicago','New York',722)
g.add_edge('Boston','New York',191)

print(Caixeiro_Viajante(cidades,cidades[0],g))