from adafruit_circuitplayground import cp
import time
import random
while True:
    if cp.button_a:
        x = random.randint(0,10)
        for i in range(0,x):
            cp.pixels[i] = (0,1,0)
        time.sleep(.4)
    elif cp.button_b:
        cp.pixels.fill((0,0,0))