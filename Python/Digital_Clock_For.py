import time
import os

clear = lambda: os.system('cls')

#Ciclo para horas, minutos y segundos.
#Mientras sea verdadero, los ciclos for se repetiran.
while True:
    for h in range(24):
        for m in range(60):
            for s in range(60):
                #Se imprime en pantala los valores de la hora.
                print(f"{h}:{m}:{s}")
                #Se alenta la ejecución del ciclo para poder ver su progresión en consola.
                time.sleep(.00001)
                #Se limpia pantalla después de que pasa cada segundo.
                clear()



 
