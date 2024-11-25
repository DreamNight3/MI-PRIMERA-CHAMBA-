opcion=1
#En un ciclo while realiza operaciones hasta que el ususario escriba 0
while opcion!=0:
  num1=int(input("Ingresa un numero:"))
  num2=int(input("Ingresa un numero:"))
  print("Ingresa 1 Suma")
  print("Ingresa 2 Restar") 
  print("Ingresa 3 Multiplicar") 
  print("Ingresa 4 Dividir")
  op=int(input("¿Que operacion quieres hacer con estos numeros?"))
  if (op==1):
    res= num1+num2 
    print("La suma de los numeros es: ",res)
  elif (op==2):  
    print("La resta de los numeros es: ",res)
    res= num1-num2
  elif (op==3):    
    res= num1* num2
    print("La resta de los numeros es: ",res)
  elif (op==4):
    res=num1/num2
    print("La resta de los numeros es: ",res)
  else:  
    print("Lo siento lo que ingresaste no es valido")
  opcion=int(input("Deseas continuar, si no presiona 0 para salir"))
  




