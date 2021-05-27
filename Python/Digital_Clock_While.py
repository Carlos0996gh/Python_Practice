import time
import os

clear = lambda: os.system('cls')

#Se establece la hora para comenzar el ciclo.
h = 23
m = 58
s = 0

#Ciclo para horas, minutos y segundos.
while h < 24:
    while m < 60:
        while s < 60:
            #Se imprime en pantala los valores de la hora.
            print(f"{h}:{m}:{s}")
            #Se alenta la ejecución del ciclo para poder ver su progresión en consola.
            time.sleep(.00009)

            #Al llegar a la hora 23:59:59 se reinician los valores para volver a comenzar el loop.
            if(h == 23 and m == 59 and s == 59):
                h = 0
                m = 0
                s = 0
            #Se limpia pantalla después de que pasa cada segundo.
            clear()
            
            s+=1
        m+=1
        s = 0
    h+=1
    m = 0

