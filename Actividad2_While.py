##Hacer una tabla de multiplicar con while que comience al reves es decir desde10 hasta 1
i=10
num=int(input("Ingrese un numero: "))
while i>=1:
    print(num,"*",i,"=",num*i)
    i-=1
print("Fin del ciclo ")