import random

ventas = [random.randint(1000000, 5000000) for _ in range(30)]

total_ventas = sum(ventas)

promedio_ventas = total_ventas // len(ventas)

indices_viernes = [i for i in range(4, 30, 7)]
mayor_venta_viernes = max((ventas[i], i) for i in indices_viernes)
dia_viernes_mayor = mayor_venta_viernes[1] + 1  

indices_finde = [i for i in range(5, 30, 7)] + [i for i in range(6, 30, 7)]
mayor_venta_finde = max((ventas[i], i) for i in indices_finde)
dia_finde_mayor = mayor_venta_finde[1] + 1

print(f"Ventas diarias: {ventas}")
print(f"A) Total de ventas del mes: {total_ventas}")
print(f"B) Promedio de ventas diario: {promedio_ventas}")
print(f"C) El viernes con mayor venta fue el día {dia_viernes_mayor} con {mayor_venta_viernes[0]}")
print(f"D) El fin de semana con mayor venta fue el día {dia_finde_mayor} con {mayor_venta_finde[0]}")