# Como crear diccionarios en python

autos = ["Mazda", "Toyota", "Renault"]
precio = [23900, 18500, 17800]

# Este es un metodo para crear diccionarios
datos = {"Mazda": 23900, "Toyota": 18500, "Renault": 17800}

print(datos)

# Este es otro metodo para crear diccionarios mas eficazmente
datos = dict(zip(autos, precio))

print(datos)

