frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

frutos = [
    {"nombre": "Mandarina", "precio": 10.99, "cantidad": 5},
    {"nombre": "Melón", "precio": 8.50, "cantidad": 3},
    {"nombre": "Kiwi", "precio": 12.00, "cantidad": 7}
]
total_venta = 0.0
for fruto in frutos:
    print(fruto["nombre"])
    print(fruto["precio"])
    print(fruto["cantidad"])
    total_venta += fruto["precio"] * fruto["cantidad"]
print(f"Total de venta: {total_venta}")

#    {"nombre":"manzana", "precio": 10.99, "cantidad" : 3},
    #{"nombre":"banana", "precio": 5.00, "cantidad" : 10},
    #{"nombre":"cereza", "precio": .99, "cantidad" : 9}     ]
 
#total_venta = 0.0
 
#for fruta in frutas: #calcular el total de la venta (precio * cantidad)
 #   total_fruta =fruta["precio"] * fruta["cantidad"]
  #  total_venta = (total_venta + total_fruta )
 
#print(f"Tu total de venta es : {total_venta}")

frutas = []
 
while True:
    nombre = input("Ingresa el nombre de la fruta que deseas agregar: ")
 
    if nombre == "salir": # salir cuando el usuario ingrese 'salir'
        break
    precio = float(input(f"Ingresa el precio de {nombre}: "))
 
    fruta = {
        "nombre" :nombre,
        "precio" : precio
    }
    frutas.append(fruta)
    print(f"Ingresando la fruta: {nombre} con el precio de {precio}")
 
print("Frutas ingresadas:", frutas)