
from functions import createTree

#Cria a estrutura da árvore
r = createTree('(1 / 1) + 2 - (3 * 1)')

#Resolve a expressão
print(r.resolve())

#Desenha a árvore gerada
r.draw()
