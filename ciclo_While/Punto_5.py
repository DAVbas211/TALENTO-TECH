num_men = int(input("ingresa un numero"))
num_may = int(input(f"ingresa un numero mayor que {num_men}"))

while num_may > num_men:
    num_men = num_may
    num_may = int(input(f"ingresa un numero mayor que {num_men}"))
else:
    print(f"el numero {num_may} es menor que el numero {num_men}")
