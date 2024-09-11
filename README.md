# imagenes con Python


Este proyecto en Python tiene como objetivo gestionar fotos de jugadores almacenadas en una carpeta o directorio, compararlas con los datos de un archivo CSV y proporcionar opciones para visualizar y eliminar jugadores, utilizando las bibliotecas `pandas`, `matplotlib`, y `os`.

## Bibliotecas 

Hay que tener las siguientes bibliotecas instaladas:

- `pandas`: Para trabajar con DataFrames y el archivo CSV.
- `matplotlib`: Para mostrar las imágenes y crear gráficos.
- `os`: Para interactuar con el sistema de archivos.

## Funcionalidades principales
* Cargar datos del CSV: El archivo argentina.csv se carga en un DataFrame de pandas. Luego, se convierte en una lista para su posterior manipulación.

* Listar fotos: Se busca en la carpeta fotos/ las imágenes de los jugadores. Solo se consideran las imágenes en formato .jpg.

* Filtrar imágenes en blanco y negro: El programa detecta automáticamente las imágenes que están en blanco y negro y las almacena en una lista.

* Coincidencias entre CSV y fotos: Se crea un conjunto de datos a partir del archivo CSV y otro conjunto a partir de las fotos. Se muestran las coincidencias y los jugadores que no tienen fotos.

# Menú interactivo:

        -------------------
        ¿Qué deseas hacer?
        -------------------
        1. Ver todos los jugadores
        2. Ver un jugador en particular
        3. Borrar un jugador
        4. Salir del menú
        ---------------------------------


* Ver todos los jugadores: Muestra los jugadores y sus fotos.
* Ver un jugador en particular: Permite seleccionar un jugador por su número y muestra su foto.
* Borrar un jugador: Elimina a un jugador tanto del archivo CSV como de la carpeta de fotos.
* Salir: Cierra el programa.
