# este programa es un contador de horas y conversor en tiempo real a horas militar
# @german-giraldom - $german giraldo marquez $
import time

horas = 11
minutos = 50
hora = ""
ampm = "AM"

while True:

    if (minutos == 60):
        horas += 1
        minutos = 0

    if (horas == 12 and minutos == 0):
        if (ampm == "PM"):
            ampm = "AM"
        else: ampm ="PM"
    elif (horas == 13):
        horas = 1
    
    if (horas<10): hora = "0"
    hora += str(horas)+":"

    if (minutos<10): hora += "0"
    hora += str(minutos)+ampm

    print("Hora: ",hora,end="   ||    ")

    #conversion a hora militar

    subhora = int(hora[0:2]) #extrae la hora y convierte en entero

    if (("PM" in hora) and (subhora < 12)) or ((subhora == 12) and ("AM" in hora)):
        subhora = (subhora+12)%24
        hora = hora[:-2]
    else:hora = hora[:-2]

    hora = hora.replace(hora[:2],str(subhora),1)

    print ("""
           hora militar:    
                """,hora)
    print ()

    minutos += 1
    hora = ""

    time.sleep(1.5)
