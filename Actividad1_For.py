#Ejercicio1
#Imprimir la tabla de multiplicar del numeor que un usuario que ingrese por teclado utilizando ciclo for
i=1
num=int(input("Ingresa un numero:"))
for i in range(1,10):
    print (num,"*",i,"=",num*i)
    i+=1
    print("Fin del ciclo for")