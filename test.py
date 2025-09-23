lista = []

i1 = int(input('Ingrese un numero: '))
i2 = int(input('Ingrese un numero: '))
i3 = int(input('Ingrese un numero: '))
i4 = int(input('Ingrese un numero: '))
i5 = int(input('Ingrese un numero: '))

lista.append(i1)
lista.append(i2)
lista.append(i3)
lista.append(i4)
lista.append(i5)

mayor = max(lista)

print(f'El numero mayor es {mayor}')
