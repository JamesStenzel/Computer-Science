from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = .02

a = 0
while True:
    if a > 6:
        a = 0
    while a == 0:
        cp.pixels.fill((255,0,0))
        if cp.button_a:
            a+=1
            time.sleep(.250)
    while a == 1:
        cp.pixels.fill((207, 96, 0))
        if cp.button_a:
            a+=1
            time.sleep(.250)
    while a == 2:
        cp.pixels.fill((227, 193, 25))
        if cp.button_a:
            a+=1
            time.sleep(.250)
    while a == 3:
            cp.pixels.fill((0,255,0))
            if cp.button_a:
                a+=1
                time.sleep(.250)
    while a == 4:
        cp.pixels.fill((0,0,255))
        if cp.button_a:
            a+=1
            time.sleep(.250)
    while a == 5:
        cp.pixels.fill((255,0,255))
        if cp.button_a:
            a+=1
            time.sleep(.250)
    while a == 6:
        cp.pixels.fill((191, 11, 100))
        if cp.button_a:
            a+=1
            time.sleep(.250)