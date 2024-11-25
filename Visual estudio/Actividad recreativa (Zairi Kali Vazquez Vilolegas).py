opcion=1
print("Hola bienvenido al programa")
while opcion!=0:  
    print("Ingresa 1. para Area Triangulo")  
    print("Ingresa 2. para Area Rectangulo")  
    print("Ingresa 3. para Area circulo")  
    print("Ingresa 4. para Convertir Temperatura °F a °C")  
    print("Ingresa 5. para Convertir temperatura °C a °F")  
    print("Ingresa 0. para salir")
    op=int(input("¿Que actividad desea realizar?"))  
    if (op==1): 
        altura=int(input("Ingrese el altura del triangulo: "))
        base=int(input("Ingresa la base del triangulo:"))
        area=(base*altura)/2
        print("El area del triangulo es: ", area)
    elif (op==2):
        altura=int(input("Ingrese el altura del rectangulo: "))
        base=int(input("Ingresa la base del rectangulo: "))
        area=base*altura
        print("El area del rectangulo es: ", area)
    elif (op==3):
        radio=int(input("Ingresa el radio del circulo: "))
        area=3.1416*radio*radio
        print("El area del circulo es: ", area)
    elif(op==4): 
        Fahrenheit=int(input("Ingresa la temperatura en Fahrenheit: "))
        celsius=((Fahrenheit-32)*5)/9
        print("La temperaura en Celsius es: ", celsius)
    elif(op==5):
        celsius=int(input("Ingrese la temperatira en Celsius:"))
        Fahrenheit=(celsius*9/5)+32
        print("La temperatura en Fahrenheit es: ", Fahrenheit)
    else:
        print("Lo siento lo que ingresaste no es valido")
    opcion=int(input("Deseas continuar, si no presiona 0 para salir"))
