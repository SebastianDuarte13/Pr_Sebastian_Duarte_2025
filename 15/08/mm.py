dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']


dias = dias[4:] + dias[:4]

dia = int(input('Introduce un número del 1 al 31: '))
if 1 <= dia <= 31:
    print(f'El día {dia} es un {dias[(dia - 1) % 7]}')