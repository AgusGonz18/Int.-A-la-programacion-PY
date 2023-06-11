#1.1

import random


def pertenece(s: list, e: int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False

#1.2
def divideATodos (s:list, e:int) -> bool:
    for i in range(len(s)):
        if (s[i] % e != 0):
            return False
    return True


#1.3
def sumaTotal (s: list) -> int:
    e: int
    e=0
    for i in range (len(s)):
        e = e + s[i]

    return e

#1.4
def ordenados (s: list)-> bool:
    for i in range(len(s) -1 ):
        if (s[i] >= s[i+1]):
            return False
    return True

#1.5
def lista (s:list)-> bool:
    for i in range(len(s)):
        if (len(s[i]) > 6):
            return True
    return False

#1.6
"""Dada una cadena de texto (string), devolver verdadero si 
esta es palindroma (se lee igual en ambos sentidos), falso en
caso contrario."""

def palin(s: str)->bool:
    for i in range(len(s)):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True

#Ej 1.7
def contraseña (contraseña: str) -> str:
    tieneMayuscula: bool = False
    tieneNumero: bool = False
    tieneMinuscula: bool = False
    for i in range (0, len (contraseña), 1):
        if (contraseña[i] >= "a" and contraseña[i] <= "z"):
            tieneMinuscula = True
            print ("cumple m")
        elif (contraseña[i] >= "A" and contraseña[i] <="Z"):
            tieneMayuscula = True
            print ("cumple M")
        elif (contraseña [i] >= "0" and contraseña[i] <= "9"):
            tieneNumero = True
            print ("cumple num")
    if (len(contraseña) > 8) and tieneMayuscula and tieneMinuscula and tieneNumero:
        return "Verde"
    if (len (contraseña) < 5):
        return "Rojo"
    return "Amarillo"

#Ej 1.8
def movimientos (movis) ->int:
    saldo:int
    saldo = 0
    for i in range(len(movis)):
        tipo = movis[i][0]
        monto = movis[i][1]
        if tipo == "I":
            saldo += monto
        elif tipo == "R":
            saldo -= monto
    return saldo 

#Segunda Parte
#2.1 
def posiciones_pares(numeros: list) -> list:
    for i in range(len(numeros)):
        if ((i % 2) == 0):
            numeros[i] = 0
    
    return numeros

#2.2
def borraEnPares2Nehuen (lista:list[int]) -> list[int]:
    lista2: list = []

    for i in range(len(lista)):
        if i%2 == 0:
            lista2.append(0)
        else:
            lista2.append(lista[i])

    return lista2

#2.3
def sin_vocal(lista: str) ->str:
    lista2: str =""
    for i in lista:
        if (i != "a" and i != "e" and i != "o" and i != "u" and i != "i"):
            lista2 += i

    return lista2

#2.4
def reemplazaVocales (s:str) -> str:
    s2:str = ''
    for i in s:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            s2 += '_'
        else:
            s2 += i
    return s2

#2.5
def daVueltaStr (s: str) -> str:
    s2: str = ""
    for i in s:
        s2 = i + s2
    return s2

#3.1
def listaEstudiantes() -> list[str]:
    listaNombres: list[str] = []
    nombre: str = input("Ingresar nombre del estudiante: ")

    while nombre != 'listo':
        listaNombres.append(nombre)
        nombre = input("Ingresar nombre del estudiante: ")

    return listaNombres


#3.2
def monedero_simulacion():
    monedero = 0
    historial = []
    i = 0

    accion = input("Ingrese la acción a realizar, usando C, D o X: ")
    historial.append((accion, 0))

    while accion != "X":
        if accion == "C":
            monto = int(input("Ingrese el monto que desea cargar: "))
            monedero += monto
            historial.append((accion, monto))
        elif accion == "D":
            monto = int(input("Ingrese el monto a descontar: "))
            monedero -= monto
            historial.append((accion, monto))

        i += 1
        accion = input("Ingrese la acción a realizar, usando C, D o X: ")

    print("Historial:")
    for accion, monto in historial:
        print(accion, monto)

    return "Saldo actual:", monedero

def sieteYMedio():
    total: int = 0
    seguirONo: str = 'y'
    historialCartas: list[int] = []
    
    while seguirONo == 'y':
        carta: int = random.choice([1,2,3,4,5,6,7,10,11,12])
        historialCartas.append(carta)
        print('Tu carta es: ', carta)
        
        if carta < 10:
            total += carta
        else:
            total += .5

        if total <= 7.5:
            seguirONo = input('¿Pedis carta? (y/n): ')
        else:
            return print('Perdiste, tu total es de: ', total, '\nTus cartas fueron: ', historialCartas)

    return print('Ganaste!, tu total es de: ', total, '\nTus cartas fueron: ', historialCartas)

# Ejercicio 4
# 4.1)
def perteneceACadaUno(s:list[list[int]], e:int) -> bool:
    for i in s:
        if not (pertenece(i, e)):
            return False
    return True

# 4.2)
def esMatriz(s:list[list[int]]) -> bool:
    if len(s) == 0 or len(s[0]) == 0:
        return False
    
    for i in range(1,len(s)):
        if len(s[i]) != len(s[i-1]):
            return False
    return True

# 4.3)
def filasOrdenadas(m:list[list[int]]) -> bool:
    for i in m:
        if not ordenados(i):
            return False
    return True

# 4.4)
def generaMatriz(d:int, f:float) -> list[list[int]]:
    matriz:list[list[int]] = np.random.randint(0,10,(d,d))

    return elevaMatriz(matriz, f)

def elevaMatriz(matriz:list[list[int]], f:int) -> list[list[int]]:
    matrizElevada: list[list[int]] = []

    if f == 1:
        return matriz

    for i in range(len(matriz)):
        matrizElevada.append([])
        for j in range(len(matriz)):
            matrizElevada[i].append(0)
            for n in range(len(matriz)):
                matrizElevada[i][j] += matriz[i][n] * elevaMatriz(matriz, f-1)[n][j]
    
    return matrizElevada
