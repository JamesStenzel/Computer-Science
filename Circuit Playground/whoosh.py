from adafruit_circuitplayground import cp
import time
while True:
    if cp.button_a == True:
        for i in range(0,10):
            cp.pixels[i-1] = (0,0,0)
            cp.pixels[i] = (0,1,0)
            time.sleep(.1)
        cp.pixels.fill((0,0,0))