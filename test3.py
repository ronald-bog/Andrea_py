leones = 0
tigres = 0
jirafas = 0

fin = 'si'
while fin != 'no':
    animal = input('Digite la letra de inicio de animal que quiere contar. ')
    if animal == 'l':
        leones = leones + 1
    elif animal == 't':
        tigres += 1
    else:
        jirafas += 1
    fin = input('quiere agregar mas animales (s=si, enter=no)?')

print(f'El total de leones es: {leones}\n')
print(f'El total de tigres es: {tigres}\n')
print(f'El total de jirafas es: {jirafas}\n')
