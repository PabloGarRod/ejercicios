
'''
Declaramos dos variables locales, una es la variable menu, 
que es un diccionario donde se guardan los platos y su precio
y la otra es total, inicializada a 0, para ir almacenando 
el precio de cada plato
'''


menu = {
        'Macarrones': 5,
        'Sopa': 6,
        'Cocido': 8,
        'Ensalada': 4,
        'Lentejas': 5,
        'Filete': 7,
        'Lubina': 9,
        'Hamburguesa': 6,
        'Pollo': 7,
        'Tarta': 3,
        'Fruta': 2,
        'Flan': 4
        }
total = 0

'''
Con esta funcion mostramos el menú por pantalla, 
utilizando el bucle for para recorrer el diccionario
'''

def displayMenu():
        print("MENU")
        print("=" * 20)
        for i in range(len(menu)):
                print(list(menu)[i]+":",menu[list(menu)[i]],"€")
        print("=" * 20)
'''
Esta funcion servirá para añadir platos al menú
esta funcion llama a la siguiente funcion para
preguntar si queremos seguir añadiendo platos
'''
def addMenu():
        plato = input("Introduzca plato: ")
        precio = int(input("Introduzca precio: "))
        menu[plato]=precio
        print("El menú quedaría así: ")
        displayMenu()
        preguntaAddMenu()

'''
Esta funcion pregunta si queremos seguir añadiendo platos
y en funcion de la respuesta, nos devuelve a la anterior funcion
o finaliza mostrándonos como quedaría el menú
'''
def preguntaAddMenu():
        print("Desea añadir plato??: ")
        resp=input("Si:Y, No:N ")

        if resp == "Y":
                addMenu()
        elif resp == "N":
                print("Menú finalizado. Quedaría así:")
                displayMenu()
        else:
                print("Comando incorrecto. Escriba la respuesta correctamente")
                preguntaAddMenu()

'''
Con esta funcion elegimos los platos entro los que se han almacenado en
el diccionario menu y vamos sumando el precio a la variable total.
Depues de pedir un plato llama a la siguiente funcion.
'''


def pedirPlato():

        pedido = input("Qué plato desea tomar? ")
        if pedido not in menu:
                print("No tenemos este plato, por favor pida otro.")
                pedirPlato()
        else:
                global total
                total += menu[pedido]
                print("Su cuenta asciende a:", total, "€")
                preguntaPedirPlato()

'''
Esta funcion nos pregunta si queremos seguir pidiendo platos,
en funcion de lo que respondamos llamará a la anterior funcion
o nos mostrará el total por pantalla
'''
def preguntaPedirPlato():
        print("¿Desea pedir otro plato?")
        respuesta = input("Sí: Y, No: N: ")
        if respuesta == "Y":
                pedirPlato()
        elif respuesta == "N":
                print("Muchas gracias, el total asciende a", total, "€")
        else:
                print("Comando incorrecto. Escriba la respuesta correctamente")
                preguntaPedirPlato()

'''
Con la ultima funcion calculamos cuantos billetes de cada tipo
necesitamos para pagar. Cuando llamemos a esta función le
pasaremos como argumento la variable global "total" a la que
le hemos ido añadiendo el precio de cada plato
'''

def calculoBilletes(precio):

        quinientos = precio//500
        precio = precio%500
        doscientos = precio//200
        precio = precio%200
        cien = precio // 100
        precio = precio%100
        cincuenta = precio//50
        precio = precio%50
        veinte = precio//20
        precio = precio%20
        diez = precio//10
        precio = precio%10
        cinco = precio//5
        resto = precio%5

        print("Para pagar necesita: ")
        if quinientos > 0 :
                if quinientos == 1:
                        print(quinientos, "billete de 500€")
                else:
                        print(quinientos, "billetes de 500€")
        
        if doscientos > 0:
                if doscientos == 1:
                        print(doscientos, "billete de 200€")
                else:
                        print(doscientos, "billetes de 200€")
        if cien > 0:
                if cien == 1:
                        print(cien, "billete de 100€")
                else:
                        print(cien, "billetes de 100€")
        if cincuenta > 0:
                if cincuenta == 1:
                        print(cincuenta, "billete de 50€")
                else:
                        print(cincuenta, "billetes de 50€")
        if veinte > 0:
                if veinte == 1:
                        print(veinte, "billete de 20€")
                else:
                        print(veinte, "billetes de 20€")
        if diez > 0:
                if diez == 1:
                        print(diez, "billete de 10€")
                else:
                        print(veinte, "billetes de 10€")
        if cinco > 0:
                if cinco == 1:
                        print(cinco, "billete de 5€")
                else:
                        print(cinco, "billetes de 5€")
        if resto > 0:
                if resto == 1:
                        print(resto, "euro en monedas.")
                else:
                        print(resto, "euros en monedas.")

'''
Empezamos la ejecución del programa con un string de bienvenida, llamamos a las
funciones en un orden determinado y finalizamos el programa
con un string de despedida.
'''

print("Bienvenido a nuestro restaurante")
displayMenu()
preguntaAddMenu()
pedirPlato()
calculoBilletes(total)
print("Muchas gracias por elegir nuestro restaurante. Vuelva pronto. ")