#Avery Sledz
#4cpx1
#6/24/25
from adafruit_circuitplayground import cp
import time

def all_on():
   for i in range(10):
        cp.pixels[i] = (50, 0, 0)
def all_off():
   for i in range(10):
        cp.pixels[i] = (0, 0, 0)




while True:
    if cp.touch_A1:
        all_on()
    else:
        all_off()
