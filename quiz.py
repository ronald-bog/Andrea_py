'''
VAR
    cant_mangos, cant_fresas, cant_pinas: ENTERO

INICIO
    // Inicializar contadores
    cant_mangos ← 0
    cant_fresas ← 0
    cant_pinas ← 0
    
    // Solicitar cantidades de cada producto
    ESCRIBIR "¿Cuántos MANGOS tiene la caja?"
    LEER cant_mangos
    SUMAR A cant_mangos INICIAL cant_mangos LEIDO
    
    ESCRIBIR "¿Cuántas FRESAS tiene la caja?"
    LEER cant_fresas
    SUMAR A cant_fresas INICIAL cant_fresas LEIDO
    
    ESCRIBIR "¿Cuántas PIÑAS tiene la caja?"
    LEER cant_pinas
    SUMAR A cant_pinas INICIAL cant_pinas LEIDO
     
    // Mostrar resultados
    ESCRIBIR "=== INVENTARIO DE LA CAJA ==="
    ESCRIBIR "Mangos: ", cant_mangos
    ESCRIBIR "Fresas: ", cant_fresas
    ESCRIBIR "Piñas: ", cant_pinas
    ESCRIBIR "============================="
    ESCRIBIR "TOTAL PRODUCTOS: ", (cant_mangos + cant_fresas + cant_pinas)
    
FIN
'''

lista = [0, 1, 1, 4, 5, 6, 7, 8, 8, 12, 13, 15]

# Convierta el 12 en un 9 tal que: lista = [0,1,1,4,5,6,7,8,8,9,13,15]
lista[9] = 9
print(lista)

# Elimine todos los 8 tal que: lista = [0,1,1,4,5,6,7,9,13,15]

while 8 in lista:
    lista.remove(8)
print(lista)

# Tome la lista desde la posicion 2 en adelante tal que: lista = [1,4,5,6,7,9,13,15]
lista = lista[2:]
print(lista)

# Convierta el 4 en un 3 tal que: lista = [1,3,5,6,7,9,13,15]
lista[1] = 3
print(lista)

# Elimine el 6 tal que: lista = [1,3,5,7,9,13,15]
lista.remove(6)
print(lista)

# Agregue el numero 11 entre el 9 y el 13 tal que: lista = [1,3,5,7,9,11,13,15]
lista.insert(5, 11)
print("La respuesta final es ", lista)
