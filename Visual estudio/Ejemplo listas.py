print("Holiii")

deportes=["Futbol","Voleibol","Natacion","Basquetbol"]
print(deportes)
print(deportes[1])

#La posicion de Natacion
pos=deportes.index("Natacion")
print("La posicion de natacion es:",pos)
#Agregar otro deporte al final
deportes.append("Hamball")
print(deportes)
#Agregar elementos en una posicion
deportes.insert(2,"Tenis")
print(deportes) 


cantidad_de_saludos=int(input("Cuantos saludos quieres? "))
for i in range(cantidad_de_saludos):
    print("Hola")
    
num_deportes=int(input("Cuantos deportes deseas agregar? "))

for i in(range(num_deportes)):
  dep=input("ingresa el deporte ")
  deportes.append(dep)

print(deportes)
