
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
elif int(edad) == 18:
    print("Tienes exactamente 18 años.")
else:
    print("Eres menor de edad.")

def definir_etapa_vida(edad):
    if edad < 0:
        return "Edad inválida"
    elif edad <= 12:
        return "Niñez"
    elif edad <= 19:
        return "Adolescencia"
    elif edad <= 64:
        return "Adultez"
    else:
        return "Vejez"
    