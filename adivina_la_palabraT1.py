#Adivina la palabra

#contadores

puntaje1=0
puntaje2=0
suma=0
tamano=0
contador=0
fallo=0

#funciones

def comprobacion_1 (a): #Función que comprueba que la palabra cumpla con los criterios, devolviendo 1 en caso de ser cierto y 0 en caso de ser falso
    tamaño=len(a)
    if (tamaño<=20 and a.islower() and a.isalpha()):
        return 1
    else:
        return 0
    
def comprobacion(a): #Funcion que restrinje a 3 intentos las palabras ingresadas según los criterios
    textof=a
    contador=0
    c=comprobacion_1(a)
    while(c<1 and contador<2):
        texto=input("Ingrese una palabra de no más de 20 carácteres, en minuscula del alfabeto español. ")
        contador=contador+1
        c=comprobacion_1(texto)
        textof=texto
    if(c==0): #c será 0 si no se cumplen las condiciones de la función "comprobacion_1"
        return 0
    else:
        return str(textof)

def letra(a, b, c):
    suma=0
    numeracion=0
    intentosrealizados=0
    caracteres=len(a)
    vacio=("*")
    listax=vacio*caracteres
    print(listax) #Ingresa asteriscos por la cantidad de letras de la palabra a adivinar
    lista=a
    cintentos=intentos
    while(suma<intentos):
        print("Te quedan :",cintentos,"intentos.")
        suposicion=input(b+", ingrese una letra que crea pueda estar en la palabra ")
        intentosrealizados=intentosrealizados+1
        print("\n")
        suma=suma+1
        contador=0
        cintentos=cintentos-1 #intentos
        for i in a:
            if (i==suposicion):
                posiciones=([i for i, a in enumerate(lista) if a==suposicion])
                veces=lista.count(suposicion)
                r=list(listax)
                for i in range(veces):
                    aux=posiciones[i]
                    r[aux]=suposicion
                    listax="".join(r)
                if(veces>1 and numeracion==4 and suposicion!=l3):
                    print(listax)
                    print("La letra ingresada se encuentra en la/las posicion/es:",posiciones)
                    numeracion=5
                    l4=suposicion
                if(veces>1 and numeracion==3 and suposicion!=l2):
                    print(listax)
                    print("La letra ingresada se encuentra en la/las posicion/es:",posiciones)
                    numeracion=4
                    l3=suposicion
                if(veces>1 and numeracion==2 and suposicion!=l1):
                    print(listax)
                    print("La letra ingresada se encuentra en la/las posicion/es:",posiciones)
                    numeracion=3
                    l2=suposicion
                if(veces>1 and numeracion==1 and suposicion!=l):
                    print(listax)
                    print("La letra ingresada se encuentra en la/las posicion/es:",posiciones)
                    numeracion=2
                    l1=suposicion
                if(veces>1):
                    if (numeracion==0):
                        print(listax)
                        print("La letra ingresada se encuentra en la/las posicion/es:",posiciones)
                        numeracion=1
                        l=suposicion
                elif(veces<=1):
                    print(listax)
                    print("La letra ingresada se encuentra en la/las posicion/es:",posiciones)
            else:
                contador=contador+1
                if(contador==caracteres):
                    print("La letra ingresada, no se encuentra en la palabra")
        if (listax==a):
            suma=intentos
    if(listax==a):
        print("Felicidades, has adivinado la palabra")
        c=c+calculo_de_puntaje(caracteres, intentosrealizados, intentos)
        return c
    elif(cintentos==0):
        print("No te quedan intentos")
        print("La palabra a adivinar era [",a,"]")
        return 0

def calculo_de_puntaje(a, b, c):
    puntaje=(1-(b/c))*a
    return puntaje

#Fase de configuración
    
print("Bienvenido a Adivina la Palabra. ")
nombre1=input("Ingrese el nombre del jugador 1. ")#Nombre del primer jugador
nombre2=input("Ingrese el nombre del jugador 2. ")#Nombre del segundo jugador
cantidad=int(input("¿Cuantas palabras desean adivinar cada uno? "))#Cantidad de palabras que debe de adivinar cada jugador
intentos=int(input("¿Cuantos intentos quieren tener para adivinar cada palabra? "))#Cantidad de intentos por palabra

#Fase de proposición-adivinación

for i in range(cantidad):
    auxiliar=intentos
    suma=suma+1
    if (fallo!=2):
        print("\n"+"RONDA ",str(suma)+"\n")
        print("Ahora juega el Proponedor: "+nombre1+".")
        palabra=input("Ingrese una palabra. ")
        fallo=comprobacion(palabra)
        if(fallo!=0):
            palabra=fallo
            print("Ahora juega Adivinador: "+nombre2+".")
            puntaje2=puntaje2+letra(palabra, nombre2, puntaje2)
        elif(fallo==0):
            print(nombre1+" ha perdido el juego por fallar 3 veces en la elección de la palabra.")
            fallo=2
        
#Ronda con el proponedor y el adivinador alternados
        
    if (fallo!=2):
        print("\n"+"ROLES INTERCAMBIADOS"+"\n")
        print("Ahora juega el Proponedor: "+nombre2)
        palabra=input("Ingrese una palabra. ")
        fallo=comprobacion(palabra)
        if(fallo!=0):
            palabra=fallo
            print("Ahora juega Adivinador: "+nombre1+".")
            puntaje1=puntaje1+letra(palabra, nombre1, puntaje1)
        elif(fallo==0):
            print(nombre2+" ha perdido el juego por fallar 3 veces en la elección de la palabra.")
            fallo=2

#Fase de cierre

if(puntaje1>puntaje2 and fallo!=2):
    print("\n"+nombre1,"acumuló",round(puntaje1,2),"puntos.")
    print(nombre2,"acumuló",round(puntaje2,2),"puntos.")
    print("¡Felicidades",nombre1,"eres el/la ganador/a!")
    
elif(puntaje2>puntaje1 and fallo!=2):
    print("\n"+nombre1,"acumuló",round(puntaje1,2),"puntos.")
    print(nombre2,"acumuló",round(puntaje2,2),"puntos.")
    print("¡Felicidades",nombre2,"eres el/la ganador/a!")

elif(puntaje2==puntaje1 and fallo!=2):
    print("\n"+nombre1,"acumuló",round(puntaje1,2),"puntos.")
    print(nombre2,"acumuló",round(puntaje2,2),"puntos.")
    print("¡Felicidades a ambos, ha ocurrido un empáte!")