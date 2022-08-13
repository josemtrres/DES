# Funcion de expansion para la F
def E (R):
    E = [   
            32,1,2,3,4,5,
            4,5,6,7,8,9,
            8,9,10,11,12,13,
            12,13,14,15,16,17,
            16,17,18,19,20,21,
            20,21,22,23,24,25,
            24,25,26,27,28,29,
            28,29,30,31,32,1
        ]
    
    for x in range(0,len(E)):
        i = E[x]
        E[x] = R[i-1]
    return E

# Funcion XOR
def XOR(A,B):
    C= ""
    for i in range (0,len(A)):
        if A[i] == B[i]:
            C += str(0)
        else:
            C += str(1)
    return C

# Funcion necesaria para obtener binarios de 4 digitos dado que usar el int, format o bin
# arroja binarios dependiendo de su longitud, por lo tanto en lugar de obtener 0001 da 1
def ABin(Sbox):
    tmp=""
    for x in Sbox:
        if len(bin(x)[2:]) < 4:
            b = bin(x)[2:]
            for i in range (0,4-len(bin(x)[2:])):
                b = str(0) + b
            tmp+=b    
        else:
            tmp += bin(x)[2:]
    return tmp

# Funcion S-box
def S(xor):
    sbox =[]
    a = 1
    b = 5
    S = [
            #S1
            [
                [14, 4, 13, 1, 2, 15, 11, 18, 3, 10, 6, 12, 5, 9, 0, 7],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
            ],
            #S2
            [
                [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7 ,11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
            ],
            #S3
            [
                [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                [13, 7, 0, 9, 2, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
            ],
            #S4
            [
                [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
            ],
            #S5
            [
                [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
            ],
            #S6
            [
                [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
            ],
            #S7
            [
                [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
            ],
            #S8
            [
                [13, 2, 5, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
            ]
        ]
    for x in range (0,8):
        sbox.append(S[x][int(xor[x*6]+xor[(x+1)*6-1],2)][int(xor[a:b],2)])
        a+=6
        b+=6
    return ABin(sbox)

# Funcion de permutación de F
def P(Sbox):
    tmp = ""
    p = [
            16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25
        ]
    
    for x in range(0,len(p)):
        i = p[x]
        p[x] = Sbox[i-1]

    for x in p:
        tmp += str(x)
    return tmp

# Funcion Feistel
def F (R, key):
    R_e = E(R) #expansion de R para obtener 48 bits
    xor = XOR(R_e, key) #xor de R expandida con la key, retorna 48 bits
    Sbox = S(xor) #Sbox que retorna 32 bits
    f = P(Sbox) #Hace el shuffle de 32 bits
    return f

# Algoritmo DES de encriptacion
def DES(L, R, key):
    # Se realiza la funcion Feistel
    f = F(R, key)
    R1 = XOR(L, f)
    return R+R1

# Algoritmo DES de desencriptacion
def SED(L,R, key):
    f = F(L,key)
    L0 = XOR(f,R)
    return L0 + L

def main():
    a = int(input("Seleccione el proceso que quiere realizar\n 0. Cifrado DES\n 1. Descifrado DES\n"))

    if a == 0:
        texto = str(input("Inserte la cadena de 64 bits a cifrar\n"))
        if len(texto) < 64 or len(texto) > 64:
            raise Exception("Ingrese 64 bits")
        clave = str(input("Inserte la llave de 48 bits para cifrar\n"))
        if len(clave) < 48 or len(clave) > 48:
            raise Exception("Ingrese 48 bits")
        print("El texto cifrado es: ",DES(texto[:32], texto[32:],clave))
    elif a == 1:
        texto = str(input("Inserte la cadena de 64 bits a descifrar\n"))
        if len(texto) < 64 or len(texto) > 64:
            raise Exception("Ingrese 64 bits")
        clave = str(input("Inserte la llave de 48 bits para descifrar\n"))
        if len(clave) < 48 or len(clave) > 48:
            raise Exception("Ingrese 48 bits")
        print("El texto claro es: ", SED(texto[:32], texto[32:], clave))
    else:
        raise Exception("Digite un número valido")

main()