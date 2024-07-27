#Ejercicio 2: Encontrar el Máximo
#Escribe un programa que encuentre el valor máximo en una lista de números

Lista = [3, 7, 2, 9, 5]
valor_max = Lista[0]

for numero in Lista:
    if numero > valor_max:
        valor_max = numero
print(valor_max)
