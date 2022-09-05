#Crianco a classe que armazena os nós da Arvores de Busca Binaria

class TreeNode:
    #Construtor da classe
    def __init__(self, key, value, left = None, right = None, parent = None):
        self.key = key                  #Chave
        self.value = value              #Valor
        self.left_child = left          #Filho a esquerda
        self.right_child = right        #Filho a direita
        self.parent = parent            #Pai

    #Tem filho a esqueda
    def has_left_child(self):
        return self.left_child
    
    #Tem filho a direita
    def has_right_child(self):
        return self.right_child

    #Atualizaçao do nó

    def replace_node_data(self, key, value, leftChild, rightChild):
        self.key = key                      #nova chave
        self.value = value                  #novo valor
        self.left_child = leftChild         #novo filho a esquerda
        self.right_child = rightChild       #novo filho a direita

        if self.has_left_child():           #pai de um novo filho a esquerda
            self.has_left_child == self

        if self.has_right_child():          #pai de um novo filho a direita
            self.has_right_child == self

#Implementação da classe de busca binaria

class BST:
    #Construtor
    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size

    def __len__(self):
        return self.size
    
    #inputar nó na arvore, se tiver raiz: procura onde inputar o no, se nao tiver raiz: torna a raiz

    def put(self, key, value):
        #Ja existe raiz
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)

        self.size += 1

    def _put(self, key, value, current):
        #Elemento deve ir para a esquerda
        if key < current.key:
            if current.has_left_child():
                self._put(key, value, current.left_child)
            else:
                current.left_child = TreeNode(key, value, parent = current)
        else: #Elemento deve ir para a direita
            if current.has_right_child():
                self._put(key, value, current.right_child)
            else:
                current.right_child = TreeNode(key, value, parent = current)
    
    def __setitem__(self, k, v):
        self.put(k,v)
    
    #obter valor da arvore pela chave
    def get(self, key):
        #Arvore com Raiz
        if self.root:
            result = self._get(key, self.root)

            #Encontrou o elemento
            if result:
                return result.value
            #Não encontrou o elemento
            else:
                return None
        #Arvore sem raiz
        else:
            return None

    def _get(self, key, current):
        #se no corrente não existe, não existe elemento
        if not current:
            return None
        
        #Se a chave do elemento = chave busca, encontrou
        elif current.key == key:
            return current
        
        #Se a chave < chave nó
        elif key < current.key:
            #Busco na arvore a esqueda
            return self._get(key, current.left_child)
        
        else:
            #Busco na Arvore a direita
            return self._get(key, current.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    #Percorrer a arvore Pre Ordem
    def preorder(self, current_node):
        #imprime o valor da raiz
        print(current_node.key, end=',')

        #visita subarvore a esquerda
        if current_node.left_child:
            self.preorder(current_node.left_child)
        
        #visita a subarvore a direita
        if current_node.right_child:
            self.preorder(current_node.right_child)

    #Percorrer a arvore em Ordem
    def inorder(self, current_node):

        #visita subarvore a esquerda
        if current_node.left_child:
            self.inorder(current_node.left_child)
        
        #imprime o valor da Raiz
        print(current_node.key, end=',')

        #Visita a Arvore a direita
        if current_node.right_child:
            self.inorder(current_node.right_child)
        
    #Percorrer a arvore Pos Ordem
    def postorder(self, current_node):

        #visita a arvore a esquerda
        if current_node.left_child:
            self.postorder(current_node.left_child)

        #Visita a Arvore a direita
        if current_node.right_child:
            self.postorder(current_node.right_child)

        #imprime o valor da Raiz
        print(current_node.key, end=',')




T = BST()
array = [50, 17, 72, 12, 23, 54, 76, 9, 14, 19, 67]
for i in range(len(array)):
    chave = array[i]
    if not chave in T:
        T[chave] = chave

#Percorre o array e imprime as chaves

print('Pré Ordem:')
T.preorder(T.root)

print('\n\nEm Ordem:')
T.inorder(T.root)

print('\n\nPós Ordem:')
T.postorder(T.root)