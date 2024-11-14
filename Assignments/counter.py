from adafruit_circuitplayground import cp
import time
import random



a = 0
while True:
    if cp.button_a:
        a = a+1
        cp.pixels.fill((0,0,0))
        for i in range(a):
            cp.pixels[i] = (0,1,0)
        time.sleep(.400)
    if cp.button_b:
        cp.pixels.fill((0,0,0))
        a = a - 1
        for i in range(a):
            cp.pixels[i] = (0,1,0)
        time.sleep(.400)