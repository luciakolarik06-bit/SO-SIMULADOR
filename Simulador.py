

class Proceso:
  def __init__(self, id, TA, TI, memoria, estado):
    self.id = id
    self.TA = TA
    self.TI = TI
    self.memoria = memoria
    self.estado = estado
#agregar: tiempo de retorno, tiempo de espera,
    self.TR = 0. # TR =  T_fin – TA, siendo TA= tiempo de arribo
    self.TE = 0. # TE = TR – TI, donde TI es la duración de la ráfaga de CPU requerida).

      
p1 = Proceso(3, 5, 20, "nuevo")
# entonces en el arcivo solo estan cargados como columnas: P1 3 5 20 , el "nuevo" agregaria yo. 

memoria = []
#100k para el SO, 450k para procesos.
# la idea es que quede una lista de elementos que marque: proceso que ocupa el espacio, donde comienza, cuanta memoria lleva.
# por lo tanto, deberia haber una funcion que calcule el espacio disponible.

#En si, inicializar de esta forma no hace falta, lo hago para tener en cuenta las estrcturas a usar.
nuevo = []
listos = []
listSuspendidos = []
terminados = []

cantProcesos = 0
finArch = True

def leerArchivo (varArchivo, fLinea):
  fLinea = varArchivo.readline()
  if fLinea == "":
    return False
  return True


def existeArchivo(nombreArchivo):
  try:
    with open(nombreArchivo, 'r') as archivo:
      finArch = leerArchivo(archivo)
      if not finArch:
        print("El archivo esta vacio.")
        return False
      return True
  except FileNotFoundError:
    return False
    #si es false, se le da otra chance para cargar, o que se cree desde 0.

def cargarNuevos (nombreArchivo):
  if existeArchivo(nombreArchivo):
    while (cantProcesos <= 10 and finArch):
      with open(nombreArchivo, 'r') as archivo:
        for linea in archivo:
          #cada linea es un proceso, que tiene: Id, TA, TI, memoria.
          #lo cargo a la cola de nuevos y ordeno la cola de nuevos por TA, si hay dos con TA iguales, ordeno por id.
          pass #funcion que indica que el bloque aun esta vacio, es para que no mande error.
    #cargo linea por linea





