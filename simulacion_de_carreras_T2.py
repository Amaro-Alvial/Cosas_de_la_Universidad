#____Bibliotecas____
import random as rd
import matplotlib.pyplot as plt

#____CLASES____

class Equipo():

    def __init__(self,equipo):
        self.nombre=equipo[0]
        self.pilotos=[]

class Piloto():

    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return(self.nombre)

#Clase en la cual almacenaremos los datos de cada circuito, para luego utilizarlos en la simulación.

class circuito():
    def __init__(self,datos):
        self.qualy_laps=datos[2]
        self.tiempo_record=datos[0]
        self.tiempo_estimado=datos[1]

#____FUNCIONES____

#Funcion con la que obtenemos los datos de cada equipo, siendo "n", el número del equipo

def equipos(n):
    a = open("equipos.csv","r")
    lista = (a.readlines())
    equipo = lista[n]
    stringg = ""
    contador = 0
    lista_de_datos_equipo = []

    for i in equipo:
        stringg = stringg + i
        contador = contador + 1
        if i == ",":
            stringg = stringg[:-1]
            lista_de_datos_equipo.append(stringg)
            stringg = ""

    if contador == len(equipo):
        stringg = stringg[:-1]
        lista_de_datos_equipo.append(stringg)

    a.close()

    return lista_de_datos_equipo

#Funcion con la que obtenemos las estadisticas de cada equipo, siendo "n", el número del equipo

def track(n):
    a = open("tracks.csv","r")
    lista = (a.readlines())
    datos = lista[n]
    stringg = ""
    contador = 0
    lista_de_datos_tracks = []

    for i in datos:
        stringg = stringg + i
        contador += 1
        if i == ",":
            stringg = stringg[:-1]
            lista_de_datos_tracks.append(stringg)
            stringg = ""

    if contador == len(datos):
        if n!=5:
            stringg = stringg[:-1]
        lista_de_datos_tracks.append(stringg)

    a.close()

    return lista_de_datos_tracks

#Función con la cual podemos obtener los datos a utilizar del archivo "tracks", introduciendo todos los datos del circuito

def datos_tracks(pista):
    tiempo_record=pista[6]
    tiempo_estimado=pista[7]
    qualy_laps=pista[9]
    return [tiempo_record,tiempo_estimado,qualy_laps]

#Funcion con la cual rellenamos los datos del equipo ingresado, siendo "b" el equipo y other, los datos del equipo ingresado

def rellenador_de_datos(b,other):
    cantidad_de_pilotos=((len(b))-1)/2
    cantidad_de_pilotos=int(cantidad_de_pilotos)
    contador=0
    for i in range(cantidad_de_pilotos):
        c=b[(contador+1)]
        auxiliar=Piloto(c)
        contador=contador+2
        other.pilotos.append(str(auxiliar))
    pass

#Funcion con la cual rellenamos los datos de una lista introduciendo en ella a cada piloto seguido de su "seed" generada de manera aleatoria

def rellenador_de_datos2(datos):
    lista=[]
    cantidad_de_pilotos=len(datos.pilotos)
    for i in range(cantidad_de_pilotos):
        seed=rd.randrange(100000,999999)
        lista.append(datos.pilotos[i])
        lista.append(seed)
    return lista

#Funcion en la cual simulamos el tiempo obtenido por el piloto, introduciendo el circuito y la "seed" generada anteriormente por "rellenador_de_datos2"

def simulacion(pista,seed):
    datos_vuelta=[]
    rd.seed(seed)
    for i in range(1,int(pista.qualy_laps)+1):
        rand=rd.uniform(float(pista.tiempo_record),float(pista.tiempo_estimado))
        rand=str(round(rand,2))
        datos_vuelta.append(rand)
    return datos_vuelta

#Funcion en la cual utilizamos los datos obtenidos anteriormente, los cuales los ordenará en una lista con el ordern "Nombre, Nombre de equipo, Tiempo obtenido"

def resultados_pilotos(pilotos,pista,equipo):
    lista=[]
    nombre_equipo=equipo.nombre
    largo=len(pilotos)
    largo=int(largo/2)
    for i in range(1,largo+1):
        rango=(i*2)-1
        rango1=i*2-2
        lista.append(pilotos[rango1])
        lista.append(nombre_equipo)
        seed=pilotos[rango]

        simulado=(simulacion(pista,seed))
        for i in range(1,int(pista.qualy_laps)+1):
            ran=i-1
            lista.append(float(simulado[ran]))
        lista.append("\n")
    return lista

#Funcion con la cual tansformamos una lista de resultados en un string para poder ingresarlos en un archivo ".csv"

def str_de_la_lista(resultados):
    string=str(resultados[0])
    largo=len(resultados)
    stringf=""
    for i in range(1,int(largo)):
        if (resultados[i]=="\n"):
            string=string+"\n"
            stringf=stringf+string
            string=""
        if (resultados[i]!="\n"):
            if (string==""):
                string=resultados[i]
            elif (string!=""):
                string=string+", "+str(resultados[i])
    return(stringf)

#Funcion con la cual ordenamos los datos de cada piloto en una lista de listas

def lista_de_datos(resultados,pista):
    lista=[]
    listaf=[]
    auxiliar=[]
    qualy=int(pista.qualy_laps)
    for i in resultados:
        if (type(i)==float):
            lista.append(i)
    tamano=len(lista)
    cantidad=int(tamano/qualy)
    for i in range (1,cantidad+1):
        rango=(i*qualy)-qualy
        for e in range(rango,(qualy*i)):
            auxiliar.append(lista[e])
        listaf.append(auxiliar)
        auxiliar=[]
    return listaf


#Funcion con la cual se generan los datos a graficar con matplotlib

def grafico(datos1,datos2,datos3,datos4,datos5,figura,equipo):
    cantidad=len(datos1)
    pilotos=equipo.pilotos
    lista_de_pistas=["Zandvoort","Spa","Monaco","Silverstone","Abudhabi"]
    for i in range(cantidad):
        nombre=pilotos[(i)]
        a=todos(datos1,datos2,datos3,datos4,datos5,i)
        plt.plot(a, label=nombre)
        plt.xticks(range(5), lista_de_pistas)

#Funcion con la cual rellenamos los datos necesarios para la función "Grafico"

def todos(datos1,datos2,datos3,datos4,datos5,num):
    lista=[]
    largo1=len(datos1[0])
    largo2=len(datos2[0])
    largo3=len(datos3[0])
    largo4=len(datos4[0])
    largo5=len(datos5[0])
    d1=datos1[num][largo1-1]
    d2=datos2[num][largo2-1]
    d3=datos3[num][largo3-1]
    d4=datos4[num][largo4-1]
    d5=datos5[num][largo5-1]
    lista.append(d1)
    lista.append(d2)
    lista.append(d3)
    lista.append(d4)
    lista.append(d5)
    return  lista


#_____PROGRAMA_____

#A continuación, la plantilla de como debemos de ingresar los equipos a nuestro programa.
#****************************************
equipo1 = equipos(1)
datos_equipo1 = Equipo(equipo1)
rellenador_de_datos(equipo1,datos_equipo1)
pilotos1=rellenador_de_datos2(datos_equipo1)
#****************************************

#A continuación, la plantilla de como debemos ingresar los circuitos a nuestro programa
#****************************************
datos_monaco= track(1)
datos_monaco1=datos_tracks(datos_monaco)
monaco=circuito(datos_monaco1)
#****************************************

#Equipos

equipo2=equipos(2)
datos_equipo2=Equipo(equipo2)
rellenador_de_datos(equipo2,datos_equipo2)
pilotos2=rellenador_de_datos2(datos_equipo2)

equipo3=equipos(3)
datos_equipo3=Equipo(equipo3)
rellenador_de_datos(equipo3,datos_equipo3)
pilotos3=rellenador_de_datos2(datos_equipo3)

#Datos de circuitos

datos_silverstone= track(2)
datos_silverstone1=datos_tracks(datos_silverstone)
silverstone=circuito(datos_silverstone1)

datos_spa= track(3)
datos_spa1=datos_tracks(datos_spa)
spa=circuito(datos_spa1)

datos_zandvoort= track(4)
datos_zandvoort1=datos_tracks(datos_zandvoort)
zandvoort=circuito(datos_zandvoort1)

datos_abudhabi= track(5)
datos_abudhabi1=datos_tracks(datos_abudhabi)
abudhabi=circuito(datos_abudhabi1)

#Zandvoort

archivo=open("resultados_zandvoort.csv","w")
archivo.write("Piloto, Equipo, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16, L17, L18"+"\n")

pilotos1=rellenador_de_datos2(datos_equipo1)
resultados_pilotos1=resultados_pilotos(pilotos1,zandvoort,datos_equipo1)
str_resultados_pilotos1=str_de_la_lista(resultados_pilotos1)
archivo.write(str_resultados_pilotos1)

pilotos2=rellenador_de_datos2(datos_equipo2)
resultados_pilotos2=resultados_pilotos(pilotos2,zandvoort,datos_equipo2)
str_resultados_pilotos2=str_de_la_lista(resultados_pilotos2)
archivo.write(str_resultados_pilotos2)

pilotos3=rellenador_de_datos2(datos_equipo3)
resultados_pilotos3=resultados_pilotos(pilotos3,zandvoort,datos_equipo3)
str_resultados_pilotos3=str_de_la_lista(resultados_pilotos3)
archivo.write(str_resultados_pilotos3)

matp_datos1_zandvoort=(lista_de_datos(resultados_pilotos1,zandvoort))
matp_datos2_zandvoort=(lista_de_datos(resultados_pilotos2,zandvoort))
matp_datos3_zandvoort=(lista_de_datos(resultados_pilotos3,zandvoort))

archivo.close()

#Spa

archivo=open("resultados_Spa.csv","w")
archivo.write("Piloto, Equipo, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13"+"\n")

pilotos1=rellenador_de_datos2(datos_equipo1)
resultados_pilotos1=resultados_pilotos(pilotos1,spa,datos_equipo1)
str_resultados_pilotos1=str_de_la_lista(resultados_pilotos1)
archivo.write(str_resultados_pilotos1)

pilotos2=rellenador_de_datos2(datos_equipo2)
resultados_pilotos2=resultados_pilotos(pilotos2,spa,datos_equipo2)
str_resultados_pilotos2=str_de_la_lista(resultados_pilotos2)
archivo.write(str_resultados_pilotos2)

pilotos3=rellenador_de_datos2(datos_equipo3)
resultados_pilotos3=resultados_pilotos(pilotos3,spa,datos_equipo3)
str_resultados_pilotos3=str_de_la_lista(resultados_pilotos3)
archivo.write(str_resultados_pilotos3)

matp_datos1_spa=(lista_de_datos(resultados_pilotos1,spa))
matp_datos2_spa=(lista_de_datos(resultados_pilotos2,spa))
matp_datos3_spa=(lista_de_datos(resultados_pilotos3,spa))

archivo.close()

#Monaco

archivo=open("resultados_monaco.csv","w")
archivo.write("Piloto, Equipo, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16, L17, L18, L19, L20"+"\n")

pilotos1=rellenador_de_datos2(datos_equipo1)
resultados_pilotos1=resultados_pilotos(pilotos1,monaco,datos_equipo1)
str_resultados_pilotos1=str_de_la_lista(resultados_pilotos1)
archivo.write(str_resultados_pilotos1)

pilotos2=rellenador_de_datos2(datos_equipo2)
resultados_pilotos2=resultados_pilotos(pilotos2,monaco,datos_equipo2)
str_resultados_pilotos2=str_de_la_lista(resultados_pilotos2)
archivo.write(str_resultados_pilotos2)

pilotos3=rellenador_de_datos2(datos_equipo3)
resultados_pilotos3=resultados_pilotos(pilotos3,monaco,datos_equipo3)
str_resultados_pilotos3=str_de_la_lista(resultados_pilotos3)
archivo.write(str_resultados_pilotos3)

matp_datos1_monaco=(lista_de_datos(resultados_pilotos1,monaco))
matp_datos2_monaco=(lista_de_datos(resultados_pilotos2,monaco))
matp_datos3_monaco=(lista_de_datos(resultados_pilotos3,monaco))

archivo.close()

#Silverstone

archivo=open("resultados_silverstone.csv","w")
archivo.write("Piloto, Equipo, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13"+"\n")

pilotos1=rellenador_de_datos2(datos_equipo1)
resultados_pilotos1=resultados_pilotos(pilotos1,silverstone,datos_equipo1)
str_resultados_pilotos1=str_de_la_lista(resultados_pilotos1)
archivo.write(str_resultados_pilotos1)

pilotos2=rellenador_de_datos2(datos_equipo2)
resultados_pilotos2=resultados_pilotos(pilotos2,silverstone,datos_equipo2)
str_resultados_pilotos2=str_de_la_lista(resultados_pilotos2)
archivo.write(str_resultados_pilotos2)

pilotos3=rellenador_de_datos2(datos_equipo3)
resultados_pilotos3=resultados_pilotos(pilotos3,silverstone,datos_equipo3)
str_resultados_pilotos3=str_de_la_lista(resultados_pilotos3)
archivo.write(str_resultados_pilotos3)

matp_datos1_silverstone=(lista_de_datos(resultados_pilotos1,silverstone))
matp_datos2_silverstone=(lista_de_datos(resultados_pilotos2,silverstone))
matp_datos3_silverstone=(lista_de_datos(resultados_pilotos3,silverstone))

archivo.close()

#Abudhabi

archivo=open("resultados_abudhabi.csv","w")
archivo.write("Piloto, Equipo, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15"+"\n")

pilotos1=rellenador_de_datos2(datos_equipo1)
resultados_pilotos1=resultados_pilotos(pilotos1,abudhabi,datos_equipo1)
str_resultados_pilotos1=str_de_la_lista(resultados_pilotos1)
archivo.write(str_resultados_pilotos1)

pilotos2=rellenador_de_datos2(datos_equipo2)
resultados_pilotos2=resultados_pilotos(pilotos2,abudhabi,datos_equipo2)
str_resultados_pilotos2=str_de_la_lista(resultados_pilotos2)
archivo.write(str_resultados_pilotos2)

pilotos3=rellenador_de_datos2(datos_equipo3)
resultados_pilotos3=resultados_pilotos(pilotos3,abudhabi,datos_equipo3)
str_resultados_pilotos3=str_de_la_lista(resultados_pilotos3)
archivo.write(str_resultados_pilotos3)

matp_datos1_abudhabi=(lista_de_datos(resultados_pilotos1,abudhabi))
matp_datos2_abudhabi=(lista_de_datos(resultados_pilotos2,abudhabi))
matp_datos3_abudhabi=(lista_de_datos(resultados_pilotos3,abudhabi))

archivo.close()

#___Matplotlib___

plt.figure(figsize=(8,6))
grafico1=grafico(matp_datos1_zandvoort,matp_datos1_spa,matp_datos1_monaco,matp_datos1_silverstone,matp_datos1_abudhabi,plt,datos_equipo1)
grafico2=grafico(matp_datos2_zandvoort,matp_datos2_spa,matp_datos2_monaco,matp_datos2_silverstone,matp_datos2_abudhabi,plt,datos_equipo2)
grafico3=grafico(matp_datos3_zandvoort,matp_datos3_spa,matp_datos3_monaco,matp_datos3_silverstone,matp_datos3_abudhabi,plt,datos_equipo3)
plt.xlabel("Pistas")
plt.ylabel("Tiempo")
plt.legend(loc="upper left")
plt.title("Resultados", fontdict={'family': 'serif', 'color' : 'darkblue','weight': 'bold','size': 18})
plt.show()