# Árvores de expressão

Implementação e visualização de árvores binárias de expressão usando linguagem python 


## Como usar

O primeiro passo é importar e usar a função `createTree`, que é responsável por converter uma string para uma árvore binária de expressão.

```
#Importa a função
from functions import createTree

#Cria a estrutura da árvore
r = createTree('(1 / 1) + 2 - (3 * 1)')
```

Tendo uma instância da árvore, você pode chamar o método `resolve` para obter o resultado da expressão

```
r.resolve()
```

Além disso, também é possível visualizar a árvore graficamente, usando a biblioteca `networkx`. Para isso, basta chamar o método `draw`

```
r.draw()
```

Segue abaixo uma imagem contendo um jupyter notebook do algoritmo sendo utilizado:

![](https://github.com/MarlonFL15/Arvores-de-expressao/blob/main/jupyter_img.png)
