import random
import time

def HeapSort(a):  
    def sift(iniciar, count):  
        raiz = iniciar  
  
        while raiz * 2 + 1 < count:  
            nino = raiz * 2 + 1  
            if nino < count - 1 and a[nino] < a[nino + 1]:  
                nino += 1  
            if a[raiz] < a[nino]:  
                a[raiz], a[nino] = a[nino], a[raiz]  
                raiz = nino  
            else:  
                return  
  
    count = len(a)  
    iniciar = count / 2 - 1  
    fin = count - 1  
  
    while iniciar >= 0:  
        sift(iniciar, count)  
        iniciar -= 1  
  
    while fin > 0:  
        a[fin], a[0] = a[0], a[fin]  
        sift(0, fin)  
        fin -= 1  
  
def reset():
    TamLista = input("INGRESE TAMAÑO DE NUMEROS A ORDENAR EJ:10-100-1000\n")
    a = []
    
    for i in range(TamLista):
        a.append(random.randint(0,(TamLista*10)))
    print a
        
    
    print ("LISTA ORDENADA")
    for i in range(10):
        Tiempo_inicia1 = time.clock()
        HeapSort(a)
        Tiempo_Termina1 = time.clock()
        print"Tiempo De Ordenamiento: %f"%(Tiempo_Termina1 - Tiempo_inicia1)
    print a
    print"Tiempo De Ordenamiento: %f"%(Tiempo_Termina1 - Tiempo_inicia1)
    
    reset()

reset()



