num_men = int(input("ingresa un numero"))
num_may = int(input(f"ingresa un numero mayor que{num_men}"))

while num_may <= num_men:
    num_may = int(input(f"El {num_may} no es mayor que el {num_men} prorfavor ingrese un numero de nuevo"))
else:
    print(f"los numeros que ha escrito son {num_men} , {num_may}")
