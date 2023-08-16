#Desafio: realize o cubo dos valores: 2, 5, 7, 8. 10, 15, 20 -> Utilizar função ou classe

import math
valor = [2, 5, 7, 8, 10, 15, 20]
cubo = lambda x: f' O numero {x} ao cubo é:  {math.pow(x, 3)}'

for i in range(0, len(valor)):
    print(cubo(valor[i]))
