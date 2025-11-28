import os  # Importamos esto para poder obtener la ruta absoluta al final

def es_primo(numero):
    """Función auxiliar para determinar si un número es primo."""
    if numero < 2:
        return False
    # Verificamos si es divisible por algún número entre 2 y el número mismo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Configuración del archivo

nombre_archivo = 'results.txt'

print("Iniciando búsqueda de números primos entre 1 y 250...")

# Abrimos el archivo en modo escritura ('w' de write)

with open(nombre_archivo, 'w') as archivo:
    # Iteramos desde el 1 hasta el 250 (el rango en Python excluye el último número, así que usamos 251)
    for num in range(1, 251):
        if es_primo(num):
            # Escribimos el número en el archivo seguido de un salto de línea
            archivo.write(str(num) + '\n')
            # Opcional: Imprimir en consola para ver el progreso
            # print(f"Encontrado: {num}")

# Parte final: Obtener y mostrar la ruta absoluta

ruta_absoluta = os.path.abspath(nombre_archivo)

print("-" * 30)
print("¡Proceso completado con éxito!")
print(f"El script se ha guardado y ejecutado.")
print(f"Los resultados están en: {ruta_absoluta}")