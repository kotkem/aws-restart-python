nombre = "Luis"
apellido = "Martinez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)
lugar = "PythonLandia"
mensaje = f"hola {nombre} bienvenido a {lugar}"


print(f"hola {nombre} bienvenido a {lugar}")
# hola (nombre) bienvenido a (lugar)
print(type(nombre))
print(nombre.upper())
print(nombre_completo.upper())
print(mensaje)
print(mensaje.upper().replace("A", "@"))

nombre1=input("Ingrese su nombre: ")
apellido1=input("Ingrese su apellido: ")
ciudad1=input("Ingrese su ciudad: ")
mensaje1=f"Su nombre es {nombre1}, su apellido es {apellido1} y su ciudad es {ciudad1}"
print(mensaje1)
print(f"Su nombre completo es: {nombre1} {apellido1}")
