# Programa para simular el abastecimiento de una tienda de Zapatos
# Cada zapato tendrá Talla, estilo y color

import random
import zapatilla

print("Aplicación para simular la venta de 100 zapatos\n");
print("Los estilos disponibles son:");

estilos = ["Tenis",
           "Botas",
           "Crocs Metaleras",
           "Mocasines",
           "Sandalia Gladiadora"]

for estilo in estilos:
    print(f"- {estilo}")

print("\nLos Colores Disponibles son:");

colores = ["Verde Selva",
           "Azul Petróleo",
           "Rojo Sangre",
           "Café derrumbe de montaña"
           ]

for color in colores:
    print(f"- {color}")

print("\nLas tallas disponibles son:")

tallas = [28, 30, 32, 34, 36, 38, 40, 42, 44]

for talla in tallas:
    print(f"- {talla}")

print("=========== LAS VENTAS FUERON =================")

# zapatilla1=zapatilla.Zapatilla()

ventas = []

# print(zapatilla.get_talla(),"gggg")

#Darle argumentos a la clase
for i in range(10):
    a = estilos[random.randint(0, len(estilos) - 1)]
    b = tallas[random.randint(0, len(tallas) - 1)]
    c = colores[random.randint(0, len(colores) - 1)]
    zapatilla = zapatilla.Zapatilla(a, b, c)
    ventas.append(zapatilla)

#
for i in range(len(ventas) - 1):
    print(vars(ventas[i]))
    # for attr, value in kk.__dict__.items():
    # print(f"{attr}:{value}")


