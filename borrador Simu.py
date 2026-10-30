"""
El simulador deberá presentar como salida la siguiente información:
 El estado del procesador (proceso que se encuentra corriendo en ese instante)
 La tabla de particiones de memoria, la cual deberá contener (Id de partición, dirección de comienzo de
partición, tamaño de la partición, id de proceso asignado a la partición, fragmentación interna)
 El estado de la cola de procesos listos y listos/suspendidos.
 Al finalizar la simulación se deberá presentar un informe estadístico con, tiempo de retorno y espera para cada
proceso y los respectivos tiempos promedios. También deberá calcular el rendimiento del sistema para la
simulación (cantidad de trabajos terminados por unidad de tiempo)



para hace el simulador: 
main: el menu de opciones e info.
// si se quiere: una funcion para inicializar colas.
funcion 1: existencia del archivo
funcion 2: carga procesos a la cola de nuevos y ordenar
funcion 3: carga a la cola de listos / cargar en memoria
funcion 11: calcualr espacio disponible en memoria.
f4: carga de la cola de listos y suspendidos.
f5: seleccionar proceso en cola de listo, segun srtf
f6: poner proceso en ejecucion 
f7: quitar proceso en ejecucion ( e internamente se llama a las f3 y 4.
f8: contar tiempo y restra Ti
f9: liberar memoria
f10: cargar cola de terminados.

Estrcturas a usar:
*arreglos para las colas: nuevo, listo, LyS, terminados.
contadores: cant procesos, tiempo, GM
registros/clases/ diccionario: para el proceso,
lista: memoria  (a  ver, pq es variable)
bandera: cola de ejecucion.
acumuladores: promedios de tiempo, rendimiento sistema (cant trabajos terminados por u de timepo).
"""


#declaracion de variables:

#en mi opinion, delcarar los procesos como diccionarios es lo ideal, ya que estos ya estan creados, no es que los voy a tener q armar yo
proceso1 = { "TA": 3, "TI": 5, "memoria": 20, "estado": "nuevo"}

#asi tal cual estarian cargados en el archivo. Sino, uso clases:
class Proceso:

  def __init__(self, nombre, TA, TI, memoria, estado):
    self.nombre = nombre
    self.TA = TA
    self.TI = TI
    self.memoria = memoria
    self.estado = estado

p1 = Proceso("P1", 3, 5, 20, "nuevo")
# entonces en el arcivo solo estan cargados como columnas: P1 3 5 20 , el "nuevo" agregaria yo. 
#creo que no hace falta el campo "nombre".

nuevo = []
listo = []
lisSuspendidos = []
terminados = []


"""def <nombre> ()
return"""

