from timeit import default_timer as timer
from networkx.algorithms import tree
import matplotlib.pyplot as plt
import networkx as nx
import random


arq = open("saida.txt", "a")

g = nx.Graph()

n = int(input("Numero de vertices: "))
m = int(input("Numero de arestas: "))

arq.write(f"VERTICES: {n} / ARESTAS: {m}\n")

for no in range(n):
    g.add_node(no)

cont = 0
arestas = []
while(cont < m):
    aresta = random.sample(range(0, n), 2)      # gera vetor de dois numeros aleatorios entre 0 e n
    if aresta not in arestas:
        arestas.append(aresta)
        cont += 1

g.add_edges_from(arestas)

nx.draw(g, with_labels=True, font_weight='bold')
plt.show()

start = timer()
kruskal = tree.minimum_spanning_edges(g, algorithm='kruskal', weight='weight', keys=True, data=True, ignore_nan=False)
k = nx.Graph()
k.add_edges_from(list(kruskal))
k.add_nodes_from(g.nodes)
end = timer()

arq.write(f"Tempo de execução Kruskal: {end-start}s\n")

nx.draw(k, with_labels=True, font_weight='bold')
plt.show()

kArestas = k.edges()    # arestas que são da AGM
gArestas = [aresta for aresta in g.edges() if aresta not in kArestas]   # arestas que não são da AGM

pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g, pos, with_labels=True)
nx.draw_networkx_labels(g, pos)
nx.draw_networkx_edges(g, pos, edgelist=kArestas, edge_color='blue')    # plota arestas que são da AGM de azul
nx.draw_networkx_edges(g, pos, edgelist=gArestas)                       # plota arestas que não são da AGM com a cor default
plt.show()

start = timer()
prim = tree.minimum_spanning_edges(g, algorithm='kruskal', weight='weight', keys=True, data=True, ignore_nan=False)
p = nx.Graph()
p.add_edges_from(list(prim))
p.add_nodes_from(g.nodes)
end = timer()

arq.write(f"Tempo de execução Prim:    {end-start}s\n\n")

nx.draw(p, with_labels=True, font_weight='bold')
plt.show()

pArestas = p.edges()    # arestas que são da AGM
gArestas = [aresta for aresta in g.edges() if aresta not in pArestas]   # arestas que não são da AGM

pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g, pos,with_labels=True)
nx.draw_networkx_labels(g, pos)
nx.draw_networkx_edges(g, pos, edgelist=kArestas, edge_color='blue')    # plota arestas que são da AGM de azul
nx.draw_networkx_edges(g, pos, edgelist=gArestas)                       # plota arestas que não são da AGM com a cor default
plt.show()

arq.close()
