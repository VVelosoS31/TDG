from itertools import permutations
from time import time

def Ciclo_Hamiltoniano(grafo):
    start = time()
    vertices = grafo.__len__()

    rotas = permutations(grafo)
    
    rotas_hamilton = []
    zera_rotas = []
    last = -1
    count_j = 0
    count_k = 0
    count_rotas = 0
  
    for i in rotas:
        count_rotas += 1
        path = []
        last = -1
        for j in i:
            count_j += 1
            if(last == -1):
                last = j
                path.append(j)
                continue
            for k in range(vertices):
                count_k += 1
                if(grafo[j][k] == 1 and k == last):
                    last = j
                    path.append(j)
                    break

            if(len(path) == vertices):
                if(grafo[last][path[0]] == 1):
                    path.append(path[0])
                    rotas_hamilton.append(path)
                    if(path[0] == 0):
                        zera_rotas.append(path)

    return(f"Podemos encontrar {len(rotas_hamilton)} ciclos hamiltonianos dentro do grafo. E demorou {((time()) - start):.2f}s para executar o algoritmo!")



grafo = {
    0: [0,1,0,1,1,0,0],
    1: [1,0,1,0,1,0,0],
    2: [0,1,0,1,1,0,0],
    3: [1,0,1,0,1,1,0],
    4: [1,1,1,1,0,1,1],
    5: [0,0,0,1,1,0,1],
    6: [0,0,0,0,1,1,0] 
}

print(f'{Ciclo_Hamiltoniano(grafo)}')

'''
Grafo AC3 - EX3
Matriz de Adjacencia:
0,1,0,1,1,0,0 - Denver
1,0,1,0,1,0,0 - Sâo Francisco
0,1,0,1,1,0,0 - Los Angeles
1,0,1,0,1,1,0 - Dallas
1,1,1,1,0,1,1 - Chicago
0,0,0,1,1,0,1 - New York
0,0,0,0,1,1,0 - Boston
'''