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
    cantidad = int(input(f"Ingresa la cantidad de {nombre}: "))
    fruta = {
        "nombre" :nombre,
        "precio" : precio,
        "cantidad": cantidad
    }
    frutas.append(fruta)
    print(f"✅ Agregado: {cantidad} {nombre} - ${precio:.2f}")
 
print("Frutas ingresadas:", frutas)
print("\n" + "=" * 40)
print("TICKET DE COMPRA".center(40))
print("=" * 40)

total_venta = 0.0
for fruta in frutas:
    subtotal = fruta["precio"] * fruta["cantidad"]
    total_venta += subtotal
    print(f"{fruta['nombre'].ljust(12)} {fruta['cantidad']:>2} x ${fruta['precio']:>5.2f} = ${subtotal:>6.2f}")

print("=" * 40)
print(f"TOTAL: ${total_venta:>7.2f}".rjust(40))
print("=" * 40)

#total_venta = 0.0
frutas = []
 
def ingresar_productos():
 
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
 
#def imprimir_ticket():
    
    print("\n--- Ticket de Compra ---")
    for fruta in frutas:
        print(f"Fruta: {fruta['nombre']}, Precio: {fruta['precio']}")
 
#if __name__ == "__main__":
    ingresar_productos()
    imprimir_ticket()
    
 