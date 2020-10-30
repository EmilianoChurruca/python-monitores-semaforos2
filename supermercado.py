import threading
import time
import logging
import random

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)



despertarCajero = threading.Condition()
atendidos = 0 

class Cajero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cajero'
    self.tiempo = random.randint(1, 5)  

  def run(self):
    global atendidos     
    with despertarCajero:
        despertarCajero.wait()
        logging.info('Estaba descansando')
    while (True):
      while len(cantidadGente)==0:

        time.sleep(1)# 
        print('parece que no hay más clientes')

        while len(cantidadGente)==0: # este while espera unos segundos por si se vació la fila y todavía hay gente comprando
          logging.info(f'Clientes atendidos: {atendidos}')
          exit()
      logging.info('Cobrando los productos.....')
      atendidos += 1    
      cantidadGente.pop(0)    
      time.sleep(self.tiempo)
      

      
    

class Cliente(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Cliente {numero}'
    
  def tiempo(self):
    return random.randint(1, 15)

  def run(self):

    time.sleep(self.tiempo())
    while(self.puedoEntrar()):
      self.comprar()
    logging.info(f'¡Está lleno, me voy')
    exit()  

  def puedoEntrar(self):
    return len(cantidadGente)<10

  def comprar(self):
    cantidadGente.append(self)
    logging.info(f'¡Entro a comprar...')
    time.sleep(self.tiempo())
    logging.info(f'¡Terminé me voy a la caja') 
    filaCaja.append(self)
    while len(filaCaja)==1:
        self.despertarCajero()
    exit()
    

  def despertarCajero(self):
    with despertarCajero:
      logging.info(f'¡que bueno no hay nadie en la fila, despierto al cajero')
      despertarCajero.notify()
      exit()







cantidadGente = [] 
filaCaja = []

Cajero().start()


for i in range(200):
  Cliente(i).start()

