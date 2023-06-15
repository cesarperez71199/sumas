#Programa que busca  si un numero  multiplicado y sumado sus uniidades de el mismo resultado 
#ejemplo  1+2+3 es lo mismo que 1*2*3

#Funcion suma de digitos
def adicion(caso):
    suma=0
    for k in range(caso):
        suma=suma+lista_digitos[k]
        
    return suma


#Funcion que realiza multiplicacion de digitos
def multiplicacion(caso):
    producto=1
    for k in range(caso):
        producto=producto*lista_digitos[k]
        
    return producto

#Funcion que delimita el rango 

def digitos(numero):
    global lista_digitos
    if (numero<=10):
        caso=1
    elif(numero<=100):
        caso=2
    elif(numero<=1000):
        caso=3
    elif(numero<=10000):
        caso=4
    elif(numero<=10000):
        caso=5
    else:
        caso=6
        
    for k in range(caso):
        
        lista_digitos.append(numero%10)  #Obtencion del residuo
        numero=numero//10               #Obtencion del cociente
        
        
        #Los digitos estan almacenados en el vector lista_digitos[k]
        #El numero de digitos es el valor del caso
        
    return caso



#Funcion que compara los resultados de las funciones adicion y multiplicacion
def comparacion(suma,producto):
    resultado= False
    if(suma==producto):
        resultado=True
        
    return resultado

#Programa principal
lista_digitos=[]

print("Dame un numero: ")
numero=int(input())

caso=digitos(numero)
print("Lista digitos ", lista_digitos)

suma=adicion(caso)
producto=multiplicacion(caso)
resultado=comparacion(suma, producto)

if(resultado):
    print("El numero cumple la condicion")
else:
    print("El numero no cumple la condicion")    
    

