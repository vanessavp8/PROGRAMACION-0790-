bisiesto= int (input("Ingrese el año que desea saber si es bisiesto o no:  "))
if bisiesto%4==0 :
	print ("Este año si es bisiesto")
elif bisiesto%4==0 and not bisiesto%100==00 : 
	print ("Este año si es bisiestro")
elif bisiesto%100==0 and bisiesto%400==0 :
	print ("Este año es bisiestro")
else:
	print ("Este año no es bisiestro")