print ("Hola, bienvenido a EduTech Solutions")
nota1 = int(input("Introduce tu Nota 1: ")) 
nota2 = int(input("Introduce tu Nota 2: "))
nota3 = int(input("Introduce tu Nota 3: "))
nota4 = int(input("Introduce tu Nota 4: "))
nota5 = int(input("Introduce tu Nota 5: "))
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print("Tu promedio es:", promedio)
if promedio >= 60:
    print("Aprobado")
elif 40 <= promedio <=59:
    print("En Recuperacion")
else:
    print("Reprobado")