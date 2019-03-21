import machine
import time

pins = (13,12,14,27,26,25,33,32)

servo0 = machine.PWM(machine.Pin(pins[0]), freq=1000)
servo0.duty(20) #Duty in % 0 - 1023
servo1 = machine.PWM(machine.Pin(pins[1]), freq=1000)
servo1.duty(24) #Duty in % 0 - 1023
servo2 = machine.PWM(machine.Pin(pins[2]), freq=1000)
servo2.duty(36) #Duty in % 0 - 1023
servo3 = machine.PWM(machine.Pin(pins[3]), freq=1000)
servo3.duty(48) #Duty in % 0 - 1023
servo4 = machine.PWM(machine.Pin(pins[4]), freq=1000)
servo4.duty(60) #Duty in % 0 - 1023
servo5 = machine.PWM(machine.Pin(pins[5]), freq=1000)
servo5.duty(72) #Duty in % 0 - 1023
servo6 = machine.PWM(machine.Pin(pins[6]), freq=1000)
servo6.duty(84) #Duty in % 0 - 1023
# servo7 = machine.PWM(machine.Pin(pins[7]), freq=200, timer=1)
servo7 = machine.PWM(machine.Pin(pins[7]), freq=1000)
servo7.duty(96) #Duty in % 0 - 1023

servo = [servo0,servo1,servo2,servo3,servo4,servo5,servo6,servo7]

print("Ready")

# time.sleep(1)
# servo[0].duty(68)
# time.sleep(1)
# servo[0].duty(116)
# time.sleep(1)
# servo[0].deinit()