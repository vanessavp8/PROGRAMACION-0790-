print ("Hola. Este programa está diseñado para ordenar tres números enteros, tanto en forma ascendente como de forma descendente.")
n1 = int (input("Ingrese el primer número entero: "))
n2 = int (input("Ingrese el segundo número entero: "))
n3 = int (input("Ingrese el tercer número entero: "))

# Comenzamos haciendo las comparaciones para definir cual será el menor, el del medio y el mayor haciendo uso de los operadores booleanos.
menor = (n1 <= n2) and (n1 <= n3)
medio = (n2 <= n1 or n2 <= n3) and not menor
mayor = not menor and not medio

# Ahora ordenamos los números de forma ascendente, utilizando la función sort 
ascendente = [n1, n2, n3]
ascendente.sort()
print ("Así se ven los números ordenados de forma ascendente" , ascendente)

# Ordenamos los números descendente utilizando la función sorted(),a su vez utilizamos el reserve = true para invertir la lista 
descendente= sorted([n1, n2, n3], reverse=True)
print("Así se ven los números ordenados de forma descendente" , descendente)
