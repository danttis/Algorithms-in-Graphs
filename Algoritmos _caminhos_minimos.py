class shortestPaths:
    def __init__(self, graph: dict, adjacencyMatrix: list, vertex: int = None) -> None:

        """
        Essa classe tem métodos para retorno dos caminhos mínimos de um grafo, pelos algoritmos Dijkstra, Bellman-Ford e Floyd-Warshall

        Argumentos:
        graph: Dígrafo D = (V, E), em formato "dict", digrafo = {0: [1, 2], 1: [2, 3], 2: [3, 1], 3: [2, 1] }, onde o valor entre [], representa os vizinhos do vértice.
        adjacencyMatrix: Matriz de pesos, em formato "list", w = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], livre de ciclos negativos ou de valores negativos em geral para o "Dijkstra".
        vertex: Vértice inicial para Dijkstra, Bellman-Ford.

        Retorno:
        Lista com os caminhos mínimos do método adotado.

        Exemplos:
            >>> shortestPaths(digrafo, w, vertice).dijkstra()
            >>> shortestPaths(digrafo, w, vertice).bellmanFord()
            >>> shortestPaths(digrafo, w).floydWarshall()
        """
        self.graph = graph
        self.adjacencyMatrix = adjacencyMatrix
        self.vertex = vertex

    def dijkstra(self):
        """Retornará uma lista com o caminho mais curto do vértice selecionado para os demais"""
        import heapq
        c = [float('inf')] * len(self.graph) 
        for i in range(1,len(self.graph)):
            c[i] = self.adjacencyMatrix[self.vertex][i]
        c[self.vertex] = 0
        h = []
        for i in range(len(self.graph)):
            heapq.heappush(h, (c[i], i))
        while h:
            dist, w = heapq.heappop(h)
            for z in self.graph[w]:
                if c[w]+self.adjacencyMatrix[w][z] < c[z]:
                    c[z] = c[w]+self.adjacencyMatrix[w][z]
                    heapq.heappush(h, (c[z], z))
        return c
    

    def bellmanFord(self):
        """Retornará uma lista com o caminho mais curto do vértice selecionado para os demais"""
        c = [float('inf')] * len(self.graph)
        c[self.vertex] = 0
        for l in range(len(self.graph) - 1):
            for k in range(len(self.graph)):
                for j in self.graph[k]:
                    if c[j] > c[k] + self.adjacencyMatrix[k][j]:
                        c[j] = c[k] + self.adjacencyMatrix[k][j]  
        return c


    def floydWarshall(self):
        """Retornará uma matriz com distâncias entre todos os vértices"""
        for k in range(len(self.graph)):
            for i in range(len(self.graph)):
                for j in range(len(self.graph)):
                    self.adjacencyMatrix[i][j] = min(self.adjacencyMatrix[i][j], self.adjacencyMatrix[i][k]+self.adjacencyMatrix[k][j])
        return self.adjacencyMatrix

v1, v2, v3, v4, v5 = range(5)

digrafo = {
    v1: [v2, v3],          # Vizinhos do vértice v1
    v2: [v3, v4],          # Vizinhos do vértice v2
    v3: [v2, v4, v5],      # Vizinhos do vértice v3
    v4: [v5],              # Vizinhos do vértice v4
    v5: [v1, v4]           # Vizinhos do vértice v5
}

w = [
    [0, 10, 5, float('inf'),float('inf')],             # Pesos das arestas saindo do vértice v1
    [float('inf'), 0, 2, 1, float('inf')],             # Pesos das arestas saindo do vértice v2
    [float('inf'), 3, 0, 9, 2],                        # Pesos das arestas saindo do vértice v3
    [float('inf'), float('inf'), float('inf'), 0,4],   # Pesos das arestas saindo do vértice v4
    [7, float('inf'), float('inf'), 6, 0]              # Pesos das arestas saindo do vértice v5
]

def matriz(matriz):
    for l in matriz:
        for e in l:
            print('{:>5}'.format(e), end=' ')
        print()


print("Dígrafo D(V,E): ",digrafo,"\n")
print("Matriz de pesos W: \n")
matriz(w)
print("\nCaminhos mínimos do vértice selecionado para os demais pelo Algoritmo de Dijkstra: ", shortestPaths(digrafo,w,v1).dijkstra(),"\n")
w[1][3], w[2][4] = -7,-2
print("Matriz de pesos, com pesos negativos: \n")
matriz(w)
print("\nCaminhos mínimos do vértice selecionado para os demais pelo Algoritmo de Bellman-Ford: ", shortestPaths(digrafo,w,v1).bellmanFord(),"\n")
print("Caminhos mínimos entre todos os vértices pelo Algoritmo de Floyd-Warshall: \n")
matriz(shortestPaths(digrafo,w).floydWarshall())
