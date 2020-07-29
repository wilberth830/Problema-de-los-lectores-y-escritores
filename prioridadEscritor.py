import threading as th
import random
import time

Lector = 0
semaf = th.Semaphore(1)
baseDatos = th.Semaphore(1)
cont = 0
Nod = th.Semaphore(1)

def escritor():
    global cont
    Nod.acquire()
    baseDatos.acquire()
    print("Ingresando escritor")
    cont = cont + 1
    print ("Escribiendo")
    time.sleep(1)
    print("Escritor liberando recurso")
    baseDatos.release()
    Nod.release()

def lector():
    global Lector, cont
    Nod.acquire()
    Nod.release()
    semaf.acquire()
    Lector = Lector + 1
    if Lector == 1:
        baseDatos.acquire()
    print("Ingresando lector")
    cont = cont + 1
    semaf.release()
    print ("Leyendo")  
    time.sleep(1)
    print("Lector liberando recurso")
    semaf.acquire()
    Lector = Lector - 1
    if Lector == 0:
        baseDatos.release()
    semaf.release()

print("Lista de los que quieren ingresar")
print("-----------------------------------------")
lista=[]
for persona in range(0,10):
    randPerson=random.randint(0, 1) 
    if randPerson == 0:
        print("En fila lector")
        lista.append(th.Thread(target=lector))
    elif randPerson ==1:
        print("En fila Escritor ")
        lista.append(th.Thread(target=escritor))
    else:
        print("ERROR---------------")
        break
print("\n")
for hilo in (lista): 
    hilo.start()

