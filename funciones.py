

def mensaje_de_bienvenida():
    print("¡Bienvenido a nuestro programa!")
mensaje_de_bienvenida()


def saludar(nombre):
    print(f"Hola, {nombre}!")

mensaje_de_bienvenida()
saludar("Carlos")
saludar(input("Ingresa tu nombre: "))

def saludo_contabiliza_dias(nombre, edad):
    dias_vividos = edad * 365
    print(f"Hola, {nombre}. Has vivido aproximadamente {dias_vividos} días.")

nombre = "jose"
edad = 33

saludo_contabiliza_dias(nombre, edad)

 #def saludo(nombre, edad):
    #total_dias = calculo_anios_por_edad(edad)
    #print(f"Hola, {nombre}! que bueno tenerte de regreso, han pasado {total_dias} desde que naciste")
 
#def calculo_anios_por_edad(edad):
    dias_anio = 365
    dias_totales = dias_anio * edad
    return dias_totales
 
#saludo("Gabriel", 42)
 