import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
}

operatorPrecedence = ['(', ')']

class root(object):
    def __init__(self, values, start='', end=''):
        self.op = values[1] #+, -, *, /
        self.left = values[0]
        self.right = values[2]

        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.value}'

    def resolve(self):
        resultLeft = self.left.resolve() if type(self.left) == root else self.left
        resultRight = self.right.resolve() if type(self.right) == root else self.right

        return ops[self.op](float(resultLeft), float(resultRight))

        
def toList(string):
    result = []
    countPreOpen = 0 #Quantidade de operadores de precêdencia de abertura
    countPreClose = 0 #Quantidade de operadores de precedência de fechamento

    indexOpen = 0 #Indíce do primeiro operador de precedência de abertura
    indexClose = 0 #Indíce do último operador de precedência de fechamento
    
    currentNumber = '' #Número atual
    
    for x in range(0,len(string)):
        if string[x] == '(':
            countPreOpen += 1
            
            if countPreOpen == 1:
                indexOpen = x
                
        if string[x] == ')':
            countPreClose += 1
            indexClose = x

            
        if countPreClose == countPreOpen: #O primeiro operador já abriu e fechou ou nós não temos nenhum operador de precedência 
            if countPreOpen == 0: #Nenhum operador de precedência foi encontrado
                if string[x].isdigit() or string[x] == '.': #Caso seja um valor número ou um ponto (para caso de valores quebrados), adiciona varíavel currentNumber
                    currentNumber += string[x]

                else: #Caso contrário, é um operador aritmético. Então adiciona o currentNumber ao resultado e também adiciona o operador aritmético
                    if currentNumber != '':
                        result.append(currentNumber)
                    result.append(string[x])
                    currentNumber=''
            else: #Quando algum operador foi encontrado, ele chama a função recursivamente para o intervalo do indíce de abertura e fechamento
                auxResult = toList(string[indexOpen+1 : indexClose])
                result.append(auxResult)

                #Reinicia as variaveis
                currentNumber = ''  
                countPreOpen = 0
                countPreClose = 0 

                indexOpen = 0 
                indexClose = 0
    if currentNumber != '':
        result.append(currentNumber)

    x=0

    
    return result
    
def toRoot(listExpression):
    setNodes(listExpression, ['/', '*'])
    setNodes(listExpression, ['+', '-'])

    return listExpression[0]
    
def setNodes(listExpression, operators):
    t = 0

    
    while t != len(listExpression):
        if listExpression[t] in operators: #O indíce T é um operador que está sendo criado na árvore
            if t > 0: #A ramificação tem algum elemento a esquerda
                if type(listExpression[t-1]) == list: #O elemento a esquerda precisa ser ramificado recursivamente
                    listExpression[t-1] = toRoot(listExpression[t-1])
                

            if t+1 < len(listExpression): #Existe algum elemento a direita
                if type(listExpression[t+1]) == list:#O elemento a direita precisa ser ramificado recursivamente
                    listExpression[t+1] = toRoot(listExpression[t+1])
                    
                    
            listExpression[t] = root(listExpression[t-1:t+2]) #converte para o tipo Root o elemento atual, o anterior e o próximo
            del(listExpression[t+1])
            del(listExpression[t-1])         
            t -= 1

        
        t += 1
        
                
def resolve(string):
    r = toRoot(toList(string.replace(' ', '')))
    return r.resolve()


    
