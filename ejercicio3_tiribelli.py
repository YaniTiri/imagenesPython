import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from os import unlink

######################################
#DATAFRAME Y LISTA DEL CSV:
#####################
df=pd.read_csv("argentina.csv")
print(df)

#numpy array lista sin comas, tolist array con comas
lista=df.to_numpy().tolist()
""" print("####################")
print("LISTA CSV:")
print(lista) """

#####################################
#Listar Fotos de directorio:
###################################
carpeta= 'fotos'
fotos_carpeta= os.listdir(carpeta)
fotos_byn=[]

#guardar en fotos_byn las fotos en blanco y negro
def foto_ByN(ruta):
    ruta_imagen="fotos/"+str(ruta)
    #print(ruta_imagen)
    imagen= mpimg.imread(ruta_imagen)
    if len(imagen.shape) == 2:
        fotos_byn.append(ruta)
        

imagenes=[]
for dir in fotos_carpeta:
    if os.path.isfile(os.path.join(carpeta, dir)) and dir.endswith('.jpg'):
       quitar_jpg= os.path.splitext(dir)[0] 
       nombre_completo=quitar_jpg.split(' ',1)
       nombre= nombre_completo[0]
       apellido= nombre_completo[1]
       imagenes.append((apellido, nombre))
       foto_ByN(dir)
""" print("####################")
print("IMAGENES:")
print(imagenes) """


#########################
#SETS DE CADA DATA:
####################
csv_set= set((apellid,nombr) for _, apellid, nombr in lista)
fotos_set=set(imagenes)
""" 
print("##########################")
print("CSV SET")
print("##########################")
print(csv_set)
print("##########################")
print("FOTOS SET:")
print("##########################")
print(fotos_set) """

#########################
#COINCIDENCIAS DE SETS:
########################
coincidencias= csv_set & fotos_set
#print(coincidencias)

#########################
#FALTANTES EN FOTOS:
########################
fotos_faltantes= csv_set - fotos_set
""" print("##########################")
print("FALTANTES EN FOTOS:")
print(fotos_faltantes) """


#si no tiene foto borrar jugador
lista= [entrada for entrada in lista if(entrada[1], entrada[2]) in fotos_set]
""" print("##########################")
print("LISTA FILTRADA: ", lista)"""


columnas=['num', 'apellido', 'nombre']

df_soloFotos=pd.DataFrame(lista, columns=columnas)

print("################################")
print("LISTA FILTRADA SOLO CON FOTOS:")
print("################################")
print(df_soloFotos)
print("##########################")
print("FOTOS BLANCO Y NEGRO: ", fotos_byn)
print("##########################") 
        
    
###########
#opciones:
##########

while True:
    ####################################
    #-------------MENU------------------
    ####################################
    print("-------------------")
    print("¿Qué deseas hacer?")
    print("-------------------")
    print("1. Ver todos los jugadores")
    print("2. Ver un jugador en particular")
    print("3. Borrar un jugador")
    print("4. Salir del menú")
    print("---------------------------------")

    opcion = input("Ingresa el número de la opción: ")
    
    ####################################
    #-------------OPCIONES--------------
    ####################################
    if opcion == "1":
        print("------------------------------------------")
        print("Tu opción fue '1. Ver todos los jugadores'")
        print("------------------------------------------")
        # imprimir todos los jugadores
        print(df_soloFotos)
        plt.figure(figsize=(12, 7))
        
        for index, row in df_soloFotos.iterrows():
            nombre=row.nombre
            apellido=row.apellido
            id=index+1
            rutaFoto="fotos/"+ nombre + " " + apellido + ".jpg"
            #print(id)
            plt.subplot(4,3,id)
            img=mpimg.imread(rutaFoto)
            
            if len(img.shape)==2:
                plt.imshow(img, cmap='gray')
            else:
                plt.imshow(img)
                
            plt.axis('off')
            plt.title(nombre.upper() + " "+ apellido.upper())
            
       
       
        plt.tight_layout()
        plt.show()
        
    elif opcion == "2":
        print("---------------------------------------------")
        print("Tu opción fue '2. Ver un jugador en particular'")
        print("---------------------------------------------")
        # While para ver detalle de un jugador
        while True:
            
            opcionJugador = input("Ingresa el num del jugador: ")
            
            jugadorElegido=df_soloFotos[df_soloFotos.num == opcionJugador]
           
            

            

            if jugadorElegido.empty:
                print("--------------------------------------------------------------")
                print("No se encontró un jugador con ese num, intentalo nuevamente")

            else:
                #fila=jugadorElegido.index
            
                nombre=jugadorElegido['nombre'].values[0]
                apellido=jugadorElegido['apellido'].values[0]
                rutaFoto="fotos/"+ nombre + " " + apellido + ".jpg"
                
                print("-------------------")
                #print(jugadorElegido)
                print("RUTA:")
                print(rutaFoto)
                
                img=mpimg.imread(rutaFoto)
                plt.axis('off')
                plt.title(nombre.upper() + " "+ apellido.upper())
                plt.imshow(img)
                plt.show()
                
                #print(jugadorElegido.index)
                break
            
    elif opcion == "3":
        print("-----------------------------------------------------------")
        print("Tu opción fue '3. Borrar un jugador'")
        print("-----------------------------------------------------------")
        while True:
            
            opcionJugador = input("Ingresa el num del jugador: ")
            

            jugadorElegido=df_soloFotos[df_soloFotos.num == opcionJugador]
            
            nombre=jugadorElegido['nombre'].values[0]
            apellido=jugadorElegido['apellido'].values[0]
            rutaFoto="fotos/"+ nombre + " " + apellido + ".jpg"

            if jugadorElegido.empty:
                print("--------------------------------------------------------------")
                print("No se encontró un jugador con ese num, intentalo nuevamente")

            else:
                print("---------------------------------------------------------------")
                #print(jugadorElegido)
                #print(jugadorElegido.index)
                df_soloFotos.drop(jugadorElegido.index, inplace=True)
                print(df_soloFotos)
                df_soloFotos.to_csv("argentina.csv", index=False)
                unlink(rutaFoto)
                break
    
    elif opcion == "4":
        ########################################
        # Salir del bucle y terminar el programa
        ########################################
        print("--------------------")
        print("Saliendo del menú...")
        print("--------------------")
        break  
    else:
        print("------------------------------------------------------------")
        print("Opción no válida. Por favor, selecciona una opción correcta.")
        print("------------------------------------------------------------")
    
#ver un jugador (ingrese nro de camiseta) titulo de imagen apellido + nombre, sin mostrar los ejes
#ver todos (sin ejes, si nos animamos con grilla de formacion)
#borrar un jugador (ingrese nombre, ingrese apellido) (borrar foto y del csv y de la matriz)