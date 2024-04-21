def dfs_com_insercao_mais_proxima(grafo, no_inicial):
 
  caminho = [no_inicial]
  visitados = set([no_inicial])
  custo_total = 0

  # Enquanto não tiver visitado todas as cidades.
  while len(visitados) < len(grafo):
    # Encontra a cidade mais próxima não visitada.
    cidade_mais_proxima = None
    min_distancia = float('inf')
    for cidade_adjacente in grafo[caminho[-1]]:
      if cidade_adjacente not in visitados:
        distancia = grafo[caminho[-1]][cidade_adjacente]
        if distancia < min_distancia:
          min_distancia = distancia
          cidade_mais_proxima = cidade_adjacente

    # Adiciona a cidade mais próxima ao caminho e atualiza as variáveis.
    caminho.append(cidade_mais_proxima)
    visitados.add(cidade_mais_proxima)
    custo_total += min_distancia

  # Adiciona o custo do último nó até o primeiro.
  custo_total += grafo[caminho[-1]][caminho[0]]

  # Retorna o caminho e o custo total.
  return caminho, custo_total

grafo = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 5, 'D': 12},
    'C': {'A': 15, 'B': 5, 'D': 8},
    'D': {'A': 7, 'B': 12, 'C': 8}
  }


caminho, custo = dfs_com_insercao_mais_proxima(grafo, 'A')
print("Caminho encontrado:", caminho)
print("Custo total:", custo)