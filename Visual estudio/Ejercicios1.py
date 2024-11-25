####Ejercicios
# 1)Crear una funcion llamada muliplicar que reciba 3 numeros, regresar el resultado
#usar funcion 
#'multiplicar(4,5,6)'
def multiplicar(num1,num2,num3): 
    res_multiplicacion=num1*num2*num3
    return res_multiplicacion
print(multiplicar(4,5,6))
# 2) Crear una funcion llamada largo_cadena que reciba texto y devuerlva la cantidad de caracteres de la misma 
#Usar funcion 
#'print(largo_cadena("El mundo es bonito"))'
def largo_cadena(texto): 
    cantidad=len(texto)
    return cantidad

# 3)Crear unafuncion llamada promedio que reciba 2 calicicaciones y devuelva el promedio
#Pedir calf. primer y segundo parcial
#'print("El promedio es: ", promedio (cal1,cal2))
def promedio(cal1,cal2): 
    prom=(cal1+cal2)/2
    return prom
cal1=int(input("Ingrese el promedio del primer parcial: "))
cal2=int(input("Ingrese el promedio del segundo parcial: "))
print(promedio(cal1,cal2))     
#crea una funcion que reciba el nombre de la persona, su edad y el mes de nacimiento 
# devuelva:
#las dos primeras letras del nombre-edad-primer letra del mes 
#Ejemplo: MA170
def disk_Curp(nom,edad,mes):
    letras=nom[0:2]
    print(letras)
    return letras
nom=int(input("Dime tu nombre: "))
edad=int(input("Dime tu edad: "))
mes=int(input("Dime en que mes naciste: "))

disk_Curp(nom,edad,mes)
nom
edad[0:1]