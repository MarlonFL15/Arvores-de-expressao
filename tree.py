import operator
import networkx as nx
from hierarchy_pos import hierarchy_pos
from matplotlib import pyplot as plt

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
}

class tree(object):
    def __init__(self, values, start='', end=''):
        self.op = values[1] #+, -, *, /
        self.left = values[0]
        self.right = values[2]
        self.start = start
        self.end = end
        self.graph_networkx = None

    def __str__(self):
        return f'{self.op}'

    def resolve(self):
        resultLeft = self.left.resolve() if type(self.left) == tree else self.left
        resultRight = self.right.resolve() if type(self.right) == tree else self.right

        return ops[self.op](float(resultLeft), float(resultRight))

    #Converte para a variável "graph_networkx" essa instância só que na versão networkx
    def update_networkx(self, G=None, index=1):
        if index == 1:
            self.graph_networkx = G = nx.Graph() #Reinicializa o gráfico

        #Adiciona no graph_network as arestas
        G.add_edge(index, index * 2)
        G.add_edge(index, index * 2 + 1)

        G.nodes[index]['label'] = str(self.op)
        G.nodes[index * 2]['label'] = str(self.left)
        G.nodes[index * 2 + 1]['label'] = str(self.right)

        #Se os nós da esquerda ou direita também tiverem nós, chamar o método recursivamente
        if type(self.left) == tree:
            self.left.update_networkx(G, index=index * 2)
        if type(self.right) == tree:
            self.right.update_networkx(G, index=index * 2 + 1)

    def draw(self):
        if self.graph_networkx == None:
            self.update_networkx()

        pos = hierarchy_pos(self.graph_networkx, 1)

        #nx.draw(self.graph_networkx, pos, node_color='#FFFFFF')
        node_labels = nx.get_node_attributes(self.graph_networkx, 'label')
        nx.draw_networkx_labels(self.graph_networkx, pos, labels=node_labels)
        nodes = nx.draw_networkx_nodes(self.graph_networkx, pos)
        nodes.set_color('#FFFFFF')
        nodes.set_edgecolor('#000000')
        
        nx.draw_networkx_edges(self.graph_networkx, pos)
        plt.show()

