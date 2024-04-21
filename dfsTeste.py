def tsp_dfs(grafo, start, visitado=None, caminho=None, custo=0, custo_min=float('inf')):
    if visitado is None:
        visitado = set()
    if caminho is None:
        caminho = [start]
    visitado.add(start)
    if len(visitado) == len(grafo):
        custo += grafo[start][caminho[0]]
        caminho.append(caminho[0])
        if custo < custo_min:
            custo_min = custo
            print(" -> ".join(caminho), " | Cost:", custo_min)
        return custo_min
    for proximo_no, peso in grafo[start].items():
        if proximo_no not in visitado:
            novo_custo = custo + peso
            if novo_custo < custo_min:
                tsp_dfs(grafo, proximo_no, visitado.copy(), caminho + [proximo_no], novo_custo, custo_min)
    return custo_min





# Exemplo de uso
grafo = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 5, 'D': 12},
    'C': {'A': 15, 'B': 5, 'D': 8},
    'D': {'A': 7, 'B': 12, 'C': 8}
  }
# Exemplo de uso:
print("Grafo 1:")
custo_minimo = tsp_dfs(grafo, 'A')
print("Menor custo:", custo_minimo)

caminho, custo = dfs_com_insercao_mais_proxima(grafo, 'A')
print("Caminho encontrado:", caminho)
print("Custo total:", custo)