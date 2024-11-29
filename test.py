counter = 0
pos = 0
lista = []

while counter <= 20:
    num = input()
    lista.append(num)
    counter = counter + 1

lista.reverse()

while pos <= 20:
    print(f'N[{pos}] = {lista[pos]}')
    pos = pos + 1