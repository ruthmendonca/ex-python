#Código de ordenação lista, sem utilizar > ou <, min ou max, ou os métodos sorted()/sort()

Lista= [14, 25, 5, 19500, 36, 400, 99, 2, 10, 0, -1, -30]

for v in range(len(Lista)-1):
    for i in range(len(Lista)-1):
      primeiro = Lista[i]
      segundo= Lista[i+1]
      maior = ((primeiro + segundo) + abs(primeiro - segundo)) / 2
      if primeiro == maior:
        #swap
        Lista[i], Lista[i+1] = Lista[i+1], Lista [i]
print(Lista)
