
# Algoritmo em python para resolver o problema do ciclo hamiltoniano com Backtracking
 
class Grafo():
    def __init__(self, vertices):
        self.grafo = [[0 for column in range(vertices)]
                            for row in range(vertices)]
        self.V = vertices

# Verifica se este vértice é um vértice adjacente do vértice adicionado anteriormente e não é incluído no caminho anterior

    def isSafe(self, v, pos, caminho):

        # Verifica se o vértice atual e o último vértice no caminho são adjacentes
        if self.grafo[ caminho[pos-1] ][v] == 0:
            return False
 
        # Verifica se o vértice atual ainda não está no caminho
        for vertex in caminho:
            if vertex == v:
                return False
 
        return True
 
    # Função recursiva para resolver o problema do ciclo hamiltoniano
    def hamCycleUtil(self, caminho, pos):
 
        # Caso base: se todos os vértices forem incluídos no caminho
        if pos == self.V:

            # O último vértice deve ser adjacente ao primeiro vértice no caminho para fazer um ciclo
            if self.grafo[ caminho[pos-1] ][ caminho[0] ] == 1:
                return True
            else:
                return False
 
        # Tenta vértices diferentes como um próximo candidato no ciclo hamiltoniano. 
        # Não tentamos 0 como incluímos 0 como ponto de partida em hamCycle ()
        for v in range(1,self.V):
 
            if self.isSafe(v, pos, caminho) == True:
 
                caminho[pos] = v
 
                if self.hamCycleUtil(caminho, pos+1) == True:
                    return True
 
                #Remove o vértice atual se não leva a uma solução
                caminho[pos] = -1
 
        return False
 
    def hamCycle(self):
        caminho = [-1] * self.V
 
   # Vamos colocar o vértice 0 como o primeiro vértice no caminho. Se houver um ciclo hamiltoniano então o caminho pode ser iniciado de qualquer ponto do ciclo, pois o gráfico não é direcionado
        caminho[0] = 0
 
        if self.hamCycleUtil(caminho,1) == False:
            print ("A solucao nao existe \n")
            return False
 
        self.printSolution(caminho)
        return True
 
    def printSolution(self, caminho):
        print ("A Solução Existe: Seguindo ",
                  "é um ciclo hamiltoniano")
        for vertex in caminho:
            print (vertex, end = " ")
        print (caminho[0], "\n")
 
# Codigo do condutor 

# Criacao do grafo 1 de teste  
g1 = Grafo(5)
g1.grafo = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0], ]
 
# Printa solucao 
g1.hamCycle();

# Criacao do grafo 2 de teste 
g2 = Grafo(5)
g2.grafo = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0], ]
 
# Printa solucao
g2.hamCycle();