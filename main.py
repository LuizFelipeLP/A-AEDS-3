import heapq
import networkx as nx
import matplotlib.pyplot as plt

# === Grafo e heurística (iguais ao anterior) ===
grafo = {
    'São João do Paraíso': {'Taiobeiras': 20, 'Rio Pardo de Minas': 25},
    'Taiobeiras': {'Salinas': 35, 'Itaobim': 55},
    'Rio Pardo de Minas': {'Porteirinha': 40},
    'Salinas': {'Francisco Sá': 50, 'Araçuaí': 60},
    'Itaobim': {'Valfenda': 40, 'Bizâncio': 35},
    'Porteirinha': {'Janaúba': 30, 'Porto Branco': 25, 'Francisco Sá': 45},
    'Francisco Sá': {'Montes Claros': 25},
    'Araçuaí': {'Montes Claros': 60},
    'Janaúba': {'Montes Claros': 35},
    'Valfenda': {},
    'Bizâncio': {},
    'Porto Branco': {},
    'Montes Claros': {}
}

heuristica = {
    'São João do Paraíso': 90,
    'Taiobeiras': 80,
    'Rio Pardo de Minas': 75,
    'Salinas': 60,
    'Itaobim': 70,
    'Porteirinha': 50,
    'Francisco Sá': 30,
    'Araçuaí': 35,
    'Janaúba': 25,
    'Valfenda': 90,
    'Bizâncio': 85,
    'Porto Branco': 45,
    'Montes Claros': 0
}

# === Algoritmo A* com retorno do caminho ===
def a_estrela(inicio, objetivo):
    fila = []
    heapq.heappush(fila, (heuristica[inicio], inicio, [inicio], 0))

    while fila:
        f_atual, atual, caminho, g = heapq.heappop(fila)

        if atual == objetivo:
            return caminho, g  # Retorna caminho e custo

        for vizinho, custo in grafo[atual].items():
            g_novo = g + custo
            h_novo = heuristica[vizinho]
            f_novo = g_novo + h_novo
            heapq.heappush(fila, (f_novo, vizinho, caminho + [vizinho], g_novo))

    return None, float('inf')

# === Visualização com networkx ===
def desenhar_grafo(caminho=None):
    G = nx.DiGraph()

    # Adiciona as arestas com peso
    for origem, vizinhos in grafo.items():
        for destino, peso in vizinhos.items():
            G.add_edge(origem, destino, weight=peso)

    pos = nx.spring_layout(G, seed=42)  # Layout automático fixo

    # Desenha todos os nós e arestas
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=1800, font_size=9, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

    # Se houver caminho, destacar em azul
    if caminho:
        path_edges = list(zip(caminho, caminho[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=caminho, node_color='skyblue')

    plt.title("Mapa de cidades com caminho A* destacado")
    plt.show()

# === Execução ===
if __name__ == "__main__":
    inicio = 'São João do Paraíso'
    destino = 'Montes Claros'
    caminho, custo = a_estrela(inicio, destino)

    if caminho:
        print("\n✅ Caminho encontrado:")
        print(" -> ".join(caminho))
        print(f"Custo total: {custo} km")
    else:
        print("❌ Caminho não encontrado.")

    desenhar_grafo(caminho)
