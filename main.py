# Isso é uma biblioteca do python para trabalhar com operações com heap, que é uma fila de prioridade
import heapq

# Grafo com apenas cidades da nossa região (valores fictícios em km)
# Tanto o grafo quanto a heuristica são dicionarios: Chave valor. (no caso, grafo é um dicionário para dicionário)
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

# Heurística = distância reta até Montes Claros. (valores totalmente reais)
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

def a_estrela(inicio, objetivo):
    # Fila de prioridade: f, cidade, caminho até agora, g. (Cada item é uma tupla com esses quatro valres)
    fila = []
    # Talvez aqui surja a dúvida do por que está salvando a heuristica no lugar que deveria ser para
    # a soma da própria com o custo real (g). Acontece que, no começo, esse custo real é igual a zero,
    # então f = h (heuristica). Nos próximos passos g vai ganhar 'peso' e o cálculo começa a ser feito.
    # heapq.heappush adciona um item na flia
    heapq.heappush(fila, (heuristica[inicio], inicio, [inicio], 0))

# Esse while vai rodar enquanto tiver elementos na lista
    while fila:
        # f_atual é a soma da heuristica + custo real, mais promissor (menor).
        # O  heapq.heappop remove e retorna o menor elemento da lista.
        f_atual, atual, caminho, g = heapq.heappop(fila)

        print(f"\n🔎 Explorando: {atual} | f={f_atual} | g={g}")

        if atual == objetivo:
            print("\nCaminho encontrado!")
            # Esse join() serve para unir elemento em uma única string, e a -> é o delimitador (NESSE CASO)
            # Como se estivesse fazendo assim: "Cidade" + "->" + "Cidade" +...
            print(" -> ".join(caminho))
            print(f"Custo total: {g} km")
            return
        # Esse for percorre todos os vizinhos do atual e muda suas informações com as informações do anteriores
        for vizinho, custo in grafo[atual].items():
            g_novo = g + custo
            h_novo = heuristica[vizinho]
            f_novo = g_novo + h_novo

            print(f"  ↳ Vizinho: {vizinho} | g={g_novo} | h={h_novo} | f={f_novo}")
            # Ta adicionando os vizinhos na fila, já com f mudado
            heapq.heappush(fila, (f_novo, vizinho, caminho + [vizinho], g_novo))

    print("\n!!! Caminho não encontrado. !!!")

# Execução do A*
if __name__ == "__main__":
    a_estrela('São João do Paraíso', 'Montes Claros')
