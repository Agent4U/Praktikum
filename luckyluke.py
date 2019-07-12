from RPi import GPIO
from time import localtime
from time import sleep
import time
import random 
farben = ["gruen","gelb","rot","blau"]
input_pin1 = 40 #gelb
input_pin2 = 38 #gruen
input_pin3 = 18 #rot
input_pin4 = 32 #blau

GPIO.setmode(GPIO.BOARD)
GPIO.setup(input_pin1 ,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(input_pin2 ,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(input_pin3 ,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(input_pin4 ,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
def creatfarbe():
    return   random.choice(farben)
   

def farbegpio(farbe):
    if farbe == "rot":
       return 33
    if farbe == "gelb":
       return 35
    if farbe == "gruen":
       return 37
    if farbe == "blau":
       return 31
  
    

for x in range(150):
    farbe = creatfarbe()
    gpo = farbegpio(farbe)
    
    GPIO.output(gpo, False)
    time.sleep(0.05)
    GPIO.output(gpo, True)
    
time.sleep(2.0)
spielzeit = time.time()
Punktzahl = 0
while (time.time() - spielzeit < 60.0):
        farbe = creatfarbe()
        gpo = farbegpio(farbe)
        GPIO.output(gpo, False)
        time.sleep(0.25)
        GPIO.output(gpo, True)
    
     
        tastenzeit = time.time() 
        while (time.time() - tastenzeit < 0.4):
            if farbe == "gelb":
               isttastergedrueckt = GPIO.input(input_pin1)
               if(isttastergedrueckt):
                  Punktzahl = Punktzahl + 1
                  print( farbe + " : Die Punktzahl ist  : " + "" + str(Punktzahl)) 
                  break
            if farbe == "gruen":
               isttastergedrueckt = GPIO.input(input_pin2)
               if(isttastergedrueckt):
                  Punktzahl = Punktzahl + 1
                  print( farbe + " : Die Punktzahl ist  : " + "" + str(Punktzahl)) 
                  break
            if farbe == "rot":
               isttastergedrueckt = GPIO.input(input_pin3)
               if(isttastergedrueckt):
                  Punktzahl = Punktzahl + 1
                  print( farbe + " : Die Punktzahl ist  : " + "" + str(Punktzahl)) 
                  break
               if farbe == "blau":
                isttastergedrueckt = GPIO.input(input_pin4)
               if(isttastergedrueckt):
                  Punktzahl = Punktzahl + 1
                  print( farbe + " : Die Punktzahl ist  : " + "" + str(Punktzahl)) 
                  break      
#GPIO.cleanup() 
time.sleep(2.0)
for x in range(150):
    farbe = creatfarbe()
    gpo = farbegpio(farbe)
    GPIO.output(gpo, False)
    time.sleep(0.05)
    GPIO.output(gpo, True)   
    
GPIO.cleanup() 