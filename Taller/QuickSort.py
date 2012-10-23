import random
import time

def QuickSort (lista,izquierdo,derecho) : 
  if izquierdo<derecho : 
    pivote=lista[(izquierdo+derecho)/2] 
    i,d=izquierdo,derecho 
    while i<=d : 
      while lista[i]<pivote : i+=1 
      while lista[d]>pivote : d-=1 
      if i<=d : 
        lista[i],lista[d]=lista[d],lista[i] 
        i+=1 
        d-=1 
    if izquierdo<d : QuickSort(lista,izquierdo,d) 
    if i<derecho : QuickSort(lista,i,derecho) 
  return lista  
  
def reset():
    TamLista = input("INGRESE TAMAÑO DE NUMEROS A ORDENAR EJ:10-100-1000\n")
    lista = []
    
    for i in range(TamLista):
        lista.append(random.randint(0,(TamLista*10)))
    print lista
    izquierdo =0
    derecho = len(lista)-1
    
    print ("LISTA ORDENADA")
    
    Tiempo_inicia1 = time.clock()
    QuickSort(lista,izquierdo,derecho)
    Tiempo_Termina1 = time.clock()
    print"Tiempo De Ordenamiento: %f"%(Tiempo_Termina1 - Tiempo_inicia1)
    print lista
    print"Tiempo De Ordenamiento: %f"%(Tiempo_Termina1 - Tiempo_inicia1)
    
    reset()

reset()


