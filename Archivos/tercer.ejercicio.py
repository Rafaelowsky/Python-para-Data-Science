nombres_carros = ("Mazda", "Renault", "Chevrolet", "Susuki", "Kia", "Ferrari", "Lamborghini")

# Para desempaquetar una tupla

carro1, carro2, carro3, carro4, carro5, carro6, carro7 = nombres_carros

print(carro1, carro2, carro3, carro4, carro5, carro6, carro7)

# Para desempaquetar por iteración}

for i in nombres_carros:
    print(i)

# Para desempaquetar por iteración con enumerate

for i, carro in enumerate(nombres_carros):
    print(i, carro)
    
# Si se quieren omitir algunos elementos de la tupla se puede hacer de la siguiente forma
# _ / *_ se ocupa para omitir los elementos que no se quieren desempaquetar

_, A, _, B, *_ = nombres_carros

print(A, B)

precio_carros = (100, 200, 300, 400, 500, 600, 700)

# zip() se ocupa para unir dos tuplas

for i in zip(nombres_carros, precio_carros):
    print(i)
    
# Y podemos trabajar con zip e iteraciones al mismo tiempo

for i, j in zip(nombres_carros, precio_carros):
    if j > 500:
        print(i, j)


