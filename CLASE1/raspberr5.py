"""
PROGRAMA PARA REALIZAR EL CONTROL DE GIRO Y VELOCIDAD DE MOTOR
DC Y LA LECTURA DE DISTANCIA MEDIANTE ULTRASONIDO
IMPLEMENTADO EN UNA INTERFAZ GRAFICA (TKINTER)}
"""
from tkinter import *
import RPi.GPIO as GPIO

# configurar los pines GPIO de la raspberry
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# ESTABLECER PINES DE SALIDA
# 16,18,32 COMO SALIDA DIGITAL
# 16 y 18 para control del giro del motor
pines = (16, 18, 32, 11)
GPIO.setup(pines, GPIO.OUT)
# PIN 13 COMO ENTRADA SE CONECTA AL ECHO DEL ULTRASONIDO
GPIO.setup(13, GPIO.IN)
# USO DEL PWM
# CREAR OBJETO CON FRECUENCIA DE 5KHZ Y EN EL CANAL 32
# T=1ms
pwm1 = GPIO.PWM(32, 1000)
# método start(duty cycle)
pwm1.start(0)

# crear objeto de la clase Tk
api = Tk()
# utilizar método geometry
api.geometry("400x400")
api.title("INTERFAZ GRAFICA EN RASPBERRY")


# --agregar botones
def anti_horario():
    print("GIRO ANTIHORARIO")
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)


def horario():
    print("GIRO HORARIO")
    GPIO.output(16, GPIO.HIGH)  # IN1=1
    GPIO.output(18, GPIO.LOW)  # IN2=0


def encender():
    # GPIO.output(32,GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    print("ENCENDER")


# FUNCIÓN APAGAR
def apagar():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    # DUTY CYCLE IGUAL A 0 , VOLTAJE EN MOTOR ES 0 VOLTS
    pwm1.ChangeDutyCycle(0)
    print("APAGAR")


# FUNCIÓN VINCULADA AL MOVIMIENTO DE SCROLL (Scale)
def scroll(indice):
    print("SCROLL IGUAL A; ", int(indice))
    pwm1.ChangeDutyCycle(int(indice))


apagar()
b1 = Button(api, text="BOTON ENCENDER", command=encender, fg="green")
b2 = Button(api, text="BOTON APAGAR", command=apagar, fg="red")
b3 = Button(api, text="BOTON HORARIO", command=horario, fg="blue")
b4 = Button(api, text="BOTON ANTI-HORARIO", command=anti_horario, fg="orange")
# CREAR UN SLIDER (BARRA) PARA VARIAR LA VELOCIDAD
s1 = Scale(api, command=scroll)
s1.place(x=100, y=200)
# CREAR UN LABEL PARA MOSTRAR MENSAJO ESTATICO
texto = Label(api, text="ACELERADOR")
texto.place(x=100, y=180)
# Text
lb2 = Label(api, text="MEDIDOR DE DISTANCIA")
lb2.place(x=220, y=180)
dist = Text(api, width=8, height=1)
dist.place(x=260, y=200)

b1.place(x=0, y=0)
b2.place(x=200, y=0)
b3.place(x=0, y=100)
b4.place(x=200, y=100)
import time

tref = time.time()
while True:
    api.update()
    api.update_idletasks()
    # BLOQUE DE CODIGO PARA LEER LA DISTANCIA
    # GENERAR PULSO DE 10 us
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.000001)
    GPIO.output(11, GPIO.LOW)
    t1 = time.time()
    while GPIO.input(13) == GPIO.LOW:
        t1 = time.time()
    t2 = time.time()
    while GPIO.input(13) == GPIO.HIGH:
        t2 = time.time()
    duracion = t2 - t1
    distancia = duracion * 340
    distancia = int(100 * distancia)
    # TEMPORIZAR 1 SEGUNDO

    if (time.time() - tref) >= 0.5:
        tref = time.time()
        # COLOCAR EL MENSAJE EN EL TEXTO dist
        dist.delete(1.0, END)
        dist.insert(1.0, str(distancia) + "cm")

print("PROGRAMA HA FINALIZADO")