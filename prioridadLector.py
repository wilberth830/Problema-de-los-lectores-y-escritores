import threading as th
import random
import time

Lector = 0
Semaf = th.Semaphore(1)
BaseDatos = th.Semaphore(1)
cont = 0

def escritor():
    global cont
    BaseDatos.acquire() 
    print("Ingresando escritor")
    cont = cont + 1
    print ("Escribiendo")
    time.sleep(1)
    print("Escritor liberando base de datos")    
    BaseDatos.release()
def lector():
    global Lector, cont
    Semaf.acquire()
    Lector = Lector + 1
    if Lector == 1:
        BaseDatos.acquire()    
    print("Ingresando lector")
    cont = cont + 1
    Semaf.release()
    print ("Leyendo") 
    time.sleep(1)
    print ("lector liberando recurso")
    Semaf.acquire()
    Lector = Lector - 1
    if Lector == 0:
        BaseDatos.release()
    Semaf.release()

print("Lista de los que quieren ingresar")
print("-----------------------------------------")
listaIngre=[]
for persona in range(0,10):
    randPerson=random.randint(0, 1) 
    if randPerson == 0:
        print("En fila lector")
        listaIngre.append(th.Thread(target=lector))
    if randPerson ==1:
        print("En fila Escritor ")
        listaIngre.append(th.Thread(target=escritor))

print("\n")
for philo in (listaIngre): 
    philo.start()

