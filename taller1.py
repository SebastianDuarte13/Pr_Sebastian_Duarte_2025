
import math

numeros = []
for i in range(8):
	num = float(input(f"Ingrese el número {i+1}: "))
	numeros.append(num)

menor = min(numeros)
mayor = max(numeros)
promedio = sum(numeros) / len(numeros)
promedio_mayor_menor = (mayor + menor) / 2

# Media geométrica
producto = 1
for n in numeros:
	producto *= n
media_geometrica = producto ** (1/len(numeros))

print(f"El número menor es: {menor}")
print(f"El número mayor es: {mayor}")
print(f"El promedio de los números es: {promedio}")
print(f"El promedio entre el mayor y el menor es: {promedio_mayor_menor}")
print(f"La media geométrica de los números es: {media_geometrica}")

