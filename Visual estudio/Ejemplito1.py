print("Hola")

edad=int(input("Ingresa tu edad: "))

if(edad>=18):
 print("Eres mayor de edad")
else:
 print("Eres menor de edad")

 temp=float(input("Ingresa la temperatura: "))

if(temp<=0):
 print("Hace frio abrigate")
elif(temp>0 and temp <=35):
 print("Esta templado")
elif(temp>35 and temp<=100):
 print("Hace calor")
else:
 print("Temperatura no valida")