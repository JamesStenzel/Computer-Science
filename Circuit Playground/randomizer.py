from adafruit_circuitplayground import cp
import time
import random

cp.pixels.brightness = .05


while True:
    x,y,z = cp.acceleration
    shake_threshold = 15
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        for i in range(0,10):
            r = random.randint(1,256)
            g = random.randint(1,256)
            b = random.randint(1,256)
            cp.pixels[i] = (r,g,b)
    time.sleep(.500)
