frutas = ["manzana", "banana", "cereza", "durazno", "kiwi"]

print(frutas[0])  # Imprime "manzana"
print(frutas[-1]) # Imprime "kiwi"
frutas.append("naranja") # Agrega "naranja" al final de la lista
print(frutas)
frutas.insert(2, "mango") # Inserta "mango" en la posición 2
print(frutas)

#sistema de gestion de alumnos en Python
alumnos = []
alumno1= input("Ingrese el nombre del alumno 1: ")
alumno2= input("Ingrese el nombre del alumno 2: ")
alumno3= input("Ingrese el nombre del alumno 3: ")
alumno4= input("Ingrese el nombre del alumno 4: ")
alumno5= input("Ingrese el nombre del alumno 5: ")

alumnos.append(alumno1)
alumnos.append(alumno2)
alumnos.append(alumno3)
alumnos.append(alumno4)
alumnos.append(alumno5)

print(alumnos)

alumnos.insert(2, input("Ingrese el nombre del nuevo alumno ")) # Inserta "nuevo alumno" en la posición 2
print(alumnos)
alumnos.remove(input("Ingrese el nombre del alumno a eliminar: ")) # Elimina el alumno especificado
print(alumnos)
