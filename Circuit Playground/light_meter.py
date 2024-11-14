from adafruit_circuitplayground import cp
import time



light = 0
while True:
    
    if cp.light > 30:
        cp.pixels.fill((0,1,0))
        light = 1
        for i in range(light-1,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 27:
        cp.pixels.fill((0,1,0))
        light = 2
        for i in range(light-1,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 24:
        cp.pixels.fill((0,1,0))
        light = 3
        for i in range(light-1,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 21:
        cp.pixels.fill((0,1,0))
        light = 4
        for i in range(light-1,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 18:
        cp.pixels.fill((0,1,0))
        light = 5
        for i in range(light-1,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 15:
        cp.pixels.fill((0,1,0))
        light = 6
        for i in range(light-1,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 12:
        cp.pixels.fill((0,1,0))
        light = 7
        for i in range(light-1,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 9:
        cp.pixels.fill((0,1,0))
        light = 8
        for i in range(light-1,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 6:
        cp.pixels.fill((0,1,0))
        light = 9
        for i in range(light-1,10):
            cp.pixels[i] = (0,0,0)
    elif cp.light > 3:
        cp.pixels.fill((0,1,0))
        light = 10
        for i in range(light-1,10):
            cp.pixels[i] = (0,0,0)