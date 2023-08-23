import bisect
import random

#BUSQUEDA BINARIA
def binary_search(needle,haystack):
    imin, imax = 0, len(haystack)
    
    while True:
        if imin > imax:
            return -1
        midpoint = (imin + imax) // 2
        #dividir el array por su mitad
        # para verificar que lado contiene el elemento a buscar
        if haystack[midpoint] > needle: 
            #descartar todos los elementos a la derecha de haystack[midpoint]
            imax = midpoint 
        elif haystack[midpoint] < needle:
            #descartar todos los elementos a la izquierda de haystack[midpoint]
            imin = midpoint+1
        else:
            #el elemento needle coincide con el que buscamos, asi que retornamos el índice
            return midpoint
        
lista_de_prueba =  [3,6,9,10,16,17,19,22,23,27,34,38]
lista_de_prueba2 = [1,2,5,4,7,9,15]
lista_de_prueba3 = [0,5,10,7,2,1]
print(binary_search(27,lista_de_prueba)) #devuelve 9
#print(binary_search(4,lista_de_prueba)) #error 
print(binary_search(5,lista_de_prueba)) #devuelve 9


def find_closest(haystack, needle):
    # La función busca el índice en la lista 'haystack' que tiene el valor más cercano
    # al valor 'needle' utilizando la búsqueda binaria.
    # bisect.bisect_left retornará el primer valor en la lista
    # mayor que el elemento 'needle'.
    
    i = bisect.bisect_left(haystack, needle)
    
    if i == len(haystack):
        return i - 1
    elif haystack[i] == needle:
        return i
    elif i > 0:
        j = i - 1
        
        # Comparamos las diferencias entre el valor en 'i' y 'needle' 
        # con el valor en 'j' y 'needle' para determinar cuál está más cerca.
        if haystack[i] - needle > needle - haystack[j]:
            return j
    return i

important_numbers = []
for i in range(10):
    # Generamos números aleatorios entre 0 y 1000 y los insertamos en la lista
    new_number = random.randint(0, 1000)
    bisect.insort(important_numbers, new_number)

print(important_numbers)

# Buscamos el valor más cercano a -250 en la lista 'important_numbers'
closest_index = find_closest(important_numbers, -250)
print(f"Valor más cercano a -250: {important_numbers[closest_index]}")

# Buscamos el valor más cercano a 500 en la lista 'important_numbers'
closest_index = find_closest(important_numbers, 500)
print(f"Valor más cercano a 500: {important_numbers[closest_index]}")

# Buscamos el valor más cercano a 1100 en la lista 'important_numbers'
closest_index = find_closest(important_numbers, 1100)
print(f"Valor más cercano a 1100: {important_numbers[closest_index]}")