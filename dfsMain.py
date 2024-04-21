import matplotlib.pyplot as plt
import networkx as nx

def dfs(grafo, no_inicial, menor_custo, visitados, custo_atual):
  
  no_atual = no_inicial
  visitados.append(no_atual)
  
  if len(visitados) == len(grafo):
    custo_atual += grafo[no_inicial][visitados[0]]
    if menor_custo > custo_atual:
      menor_custo = custo_atual

  for no in grafo[no_atual]:
    if no not in visitados:
      custo_atual += grafo[no_atual][no]
      menor_custo, visitados = dfs(grafo, no, menor_custo, visitados, custo_atual)

  return(menor_custo, visitados)

grafo = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 5, 'D': 12},
    'C': {'A': 15, 'B': 5, 'D': 8},
    'D': {'A': 7, 'B': 12, 'C': 8}
  }

no_inicial = 'A'
menor_custo = float('inf')
visitados = []
custo_atual = 0

custo, caminho = dfs(grafo, no_inicial, menor_custo, visitados, custo_atual)
print("Caminho encontrado:", caminho)
print("Custo total:", custo)

# Criar um grafo direcionado
G = nx.DiGraph()

# Adicionar as arestas ao grafo
for no, vizinhos in grafo.items():
    for vizinho, peso in vizinhos.items():
        G.add_edge(no, vizinho, weight=peso)

# Posições dos nós para desenho
pos = nx.spring_layout(G)

# Plotar o grafo
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo')

# Plotar o melhor caminho encontrado
melhor_caminho_edges = [(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)]
G_cam = nx.DiGraph()
G_cam.add_edges_from(melhor_caminho_edges)
pos_cam = nx.spring_layout(G_cam)
plt.subplot(1, 2, 2)
nx.draw(G_cam, pos_cam, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold', edge_color='red', width=2)
plt.title('Melhor Caminho')

plt.text(0.0, 0.0, f'Melhor caminho: {" -> ".join(caminho)}', transform=plt.gca().transAxes, fontsize=12)
plt.text(0.0, -0.12, f'Custo total: {custo}', transform=plt.gca().transAxes, fontsize=12)

plt.show()