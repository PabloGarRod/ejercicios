def sumatorioNumeros(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

numero=int(input("Introduzca número: "))
print("La suma de todos los dígitos da:",sumatorioNumeros(numero))
