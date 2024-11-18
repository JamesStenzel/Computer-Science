from adafruit_circuitplayground import cp
import time



light = 0
while True:
    if cp.light > 30:
        light = 1
        for i in range(light):
            cp.pixels[i] = (0,1,0)
        for i in range(light,10):
            cp.pixels[i] =(0,0,0)
    elif cp.light < 27 and cp.light > 24:
        light = 2
        for i in range(light):
            cp.pixels[i] = (0,1,0)
        for i in range(light,10):
            cp.pixels[i] =(0,0,0)
    elif cp.light < 24 and cp.light > 21:
        light = 3
        for i in range(light):
            cp.pixels[i] = (0,1,0)
        for i in range(light,10):
            cp.pixels[i] =(0,0,0)
    elif cp.light < 21 and cp.light > 18:
        light = 4
        for i in range(light):
            cp.pixels[i] = (0,1,0)
        for i in range(light,10):
            cp.pixels[i] =(0,0,0)
    elif cp.light < 18 and cp.light > 15:
        light = 5
        for i in range(light):
            cp.pixels[i] = (0,1,0)
        for i in range(light,10):
            cp.pixels[i] =(0,0,0)
    elif cp.light < 15 and cp.light > 12:
        light = 6
        for i in range(light):
            cp.pixels[i] = (0,1,0)
        for i in range(light,10):
            cp.pixels[i] =(0,0,0)
    elif cp.light < 12 and cp.light > 9:
        light = 7
        for i in range(light):
            cp.pixels[i] = (0,1,0)
        for i in range(light,10):
            cp.pixels[i] =(0,0,0)
    elif cp.light < 9 and cp.light > 6:
        light = 8
        for i in range(light):
            cp.pixels[i] = (0,1,0)
        for i in range(light,10):
            cp.pixels[i] =(0,0,0)
    elif cp.light < 6 and cp.light > 3:
        light = 9
        for i in range(light):
            cp.pixels[i] = (0,1,0)
        for i in range(light,10):
            cp.pixels[i] =(0,0,0)
    elif cp.light < 3:
        light = 10
        for i in range(light):
            cp.pixels[i] = (0,1,0)