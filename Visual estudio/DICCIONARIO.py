materia = {    
    "nombre": "programacion",
    "codigo": "INF02",
    "profesor":"Mari Garcia",
    "horarios": ["Lunes 9:00-11:00", "Miercoles 9:00-11:00"]  
    "creditos": 8,
    "nivel":"intermedio"
    "prerequisitos": ["Computacion 1"]
    "descripcion": "Desarrollo de algoritmos"
 }

print(materia["profesor"])
alumno = {
    "nombre": "Zari Vazquez",
    "matricula": "A123213243",
    "edad": 17,
    "semestre": "quinto",
    "calificaciones": { 
        "Matematicas": 3.5,
        "Fisica":9.0,
        "Programacion":9.5,
        "Quimica": 8.8
    }

    "direccion": {  
        "calle":"Av. libertad 456" 
        "ciudad": "Ciudad X", # type: ignore
        "Codigo_postal":"1234"
        },
        "telefono":"423-3401-234",
        "email":"kalivazquez44@gmail.com"
    }
print(alumno["nombre"])
print(alumno["calificaciones"])

print("La calificacion del alumno es: ")
print(alumno["calificaciones"]["programacion"])



