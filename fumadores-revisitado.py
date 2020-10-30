import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaforoAgentes = threading.Semaphore(2) #limito a dos la cantidad de agentes
semaforoFumadorPapel = threading.Semaphore(0)
semaforoFumadorFosforo = threading.Semaphore(0)
semaforoFumadorTabaco = threading.Semaphore(0)

def agenteConPapel(): # Agente que agrega el papel
    
    while True:
        semaforoAgentes.acquire()
        logging.info(f'poniendo el papel en la mesa')
        papel.append("Papel")
        time.sleep(1)

def agenteConFosforo(): # Agente que agrega el fósforo
    
    while True:
        semaforoAgentes.acquire()
        logging.info(f'poniendo el fósforo en la mesa')
        fosforo.append("fosforo")
        time.sleep(1)

def agenteConTabaco(): # Agente que agrega el tabaco
    
    while True:
        semaforoAgentes.acquire()
        logging.info(f'poniendo el tabaco en la mesa')
        tabaco.append("tabaco")
        time.sleep(1)

def fumadorConPapel():
    while True:
        while len(fosforo)!=0 and len(tabaco)!=0:   # si hay fósforos y tabaco en la mesa
            fosforo.pop(0)
            tabaco.pop(0) # tomarlos
            logging.info(f'Estoy armando el cigarrillo...')
            time.sleep(1)
            logging.info(f'Fumando el cigarrillo...') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(2.5)
            semaforoAgentes.release()
            semaforoAgentes.release()

def fumadorConFosforos():
    while True:
        while len(papel)!=0 and len(tabaco)!=0:   # si hay fósforos y tabaco en la mesa
            tabaco.pop(0)
            papel.pop(0) # tomarlos
            logging.info(f'Estoy armando el cigarrillo...')
            time.sleep(1)
            logging.info(f'Fumando el cigarrillo...') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(2)
            semaforoAgentes.release() 
            semaforoAgentes.release()
       

def fumadorConTabaco():
    
    while True:
        while len(fosforo)!=0 and len(papel)!=0:   # si hay fósforos y tabaco en la mesa
            fosforo.pop(0)
            papel.pop(0) # tomarlos
            logging.info(f'Estoy armando el cigarrillo...')
            time.sleep(1)
            logging.info(f'Fumando el cigarrillo...') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(2)
            semaforoAgentes.release()
            semaforoAgentes.release()

papel = []
fosforo = []
tabaco = []

agentePapel = threading.Thread(target=agenteConPapel, name='Agente con papel')
agenteFosforo = threading.Thread(target=agenteConFosforo, name='Agente con fósforo')
agenteTabaco = threading.Thread(target=agenteConTabaco, name='Agente con tabaco')
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel, name='Fumador con papel')
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos, name='Fumador con fósforo')
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco, name='Fumador con tabaco')

agentePapel.start()
agenteFosforo.start()
agenteTabaco.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()