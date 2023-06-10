#1.1

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
Dada una cadena de texto (string), devolver verdadero si ´
esta es palındroma (se lee igual en ambos sentidos), falso en
caso contrario.

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
def reemplazaVocales (s: chr) ->  chr: