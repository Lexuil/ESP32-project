import machine
import time

servo = machine.PWM(machine.Pin(13), freq=50)
servo.duty(24) #Duty in % 0 - 1023

print("Inicio")
time.sleep(1)
servo.duty(68)
time.sleep(1)
servo.duty(116)
time.sleep(1)
servo.deinit()