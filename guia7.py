#Ejercicio 1.1
def raizDe2 () -> float:
    return round(2**0.5, 4)

#Ej 1.2 

def imprimir_hola():
    print("Hola")

# Ej 1.3

def imprimir_un_verso():
    print("Te estas portando mal seras castigada")

# Ej 1.4

def factorial_2():
    return 4

# Ej 1.5


# Ej 1.6

def imprimir_par_10_a_40():
    ind:int = 10
    while (ind < 41):
        if (es_par(ind)):
            print (ind)
        ind += 1
        
# 2.1
def imprimir_saludo (nombre: str ) :
    print ("Hola "+str(nombre))

# 2.2
def raiz_cuadrada_de(numero: int) -> int:
    return ((numero)**0.5)

# 2.3
def imprimir_dos_veces(estribillo: str):
    print (((estribillo + "\n") *2))

# 2.4 
def es_multiplo_de(n: int, m: int) -> bool:
    return 0 == n % m 

#2.5
def es_par(n:int) -> bool:
    return es_multiplo_de(n, 2)

#2.6
def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int) -> int:
    cant: int
    cant = min_cant_de_porciones / 8 
    return (round (cant+0.5))

#3.1
def alguno_es_0(num1: int, num2: int) -> bool:
    return ((num1 == 0) or (num2 == 0))

#3.2
def ambos_son_0(num1: int, num2: int) -> bool:
    return ((num1 == 0) and (num2 == 0))

#3.3
def es_nombre_largo(nombre: str) -> bool:
    return (3 <= len(nombre) and 8 >= len (nombre))

#3.4
def es_bisiesto (año: int) -> bool:
    return (0== año % 400 or (0 == año % 4 and 0 != año % 100) )

#5.1
def devolver_el_doble_si_es_par (num: int):
    if (0 == num % 2):
        return num*2
    else:
        return num

""" 
devolver_el_doble_si_es_par (num: int):
    requiere: { num: N }
    asegura: { (0 == num % 2 -> resultado = 2*num )and(0 != num % 2 -> resultado = num) }
    asegura: { (0 == num % 2 and resultado = 2*num )or(resultado = num) }
    asegura: { (0 == num % 2 and resultado = 2*num )or(0 != num % 2 and resultado = num) }
"""
#5.2
"""
def devolver_el_doble_si_es_par (num: int):
    if (0 == num % 2):
        return num
    else:
        return (num+1)"""

#otra forma
def devolver_el_doble_si_es_par (num: int):
    if (0 != num % 2):
        return (num+1)
    if (0 == num % 2):
        return num 
    
#5.3
"""def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (num: int): 
    if (0 == num % 3):
        return (num*2)
    elif (0 == num % 9):
        return (num*3)
    else: 
        return num"""

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (num: int):
    return (0 == num % 3 and num*2) or (0 == num % 9 and num * 3) or (num)

"""
devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (num: int):
    requiere: {num: N}
    asegue: { (0 == num % 3 and res=num*2) or (0 == num % 9 and res=num*3) or (res=num)}
"""

#5.4
"""
persona = []
sexo = input("Ingrese su sexo, F para femenino o M para masculino: ")
persona.append(sexo)
edad = int(input ("Ingrese su edad: "))
persona.append(edad)

if (persona[0] == "F" and persona[1] >59):
    print("Anda de vacaciones")
elif(persona[0] == "M" and persona[1] > 64):
    print("Anda de vacaciones")
else:
    print("Te toca trabajar")
"""

#6.1
def imprimir_numeros():
    for n in range(1, 11):
        print(n)

#6.2
def numero_pares():
    for n in range(10, 41):
        if n % 2 == 0:
            print(n)

# Llamada a la función



    

    