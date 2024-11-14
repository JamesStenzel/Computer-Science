from adafruit_circuitplayground import cp
import time




while True:
    x = cp.temperature
    real_temp = (x * 9 / 5) + 32
    if real_temp < 78:
        cp.pixels.fill((0,0,0))
        cp.pixels[0] = (0,0,1)
    elif real_temp > 78:
        cp.pixels.fill((0,0,0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
    elif real_temp > 79:
        cp.pixels.fill((0,0,0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
    elif real_temp > 80:
        cp.pixels.fill((0,0,0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
    elif real_temp > 81:
        cp.pixels.fill((0,0,0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
    elif real_temp > 82:
        cp.pixels.fill((0,0,0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
        cp.pixels[5] = (1,1,0)
    elif real_temp > 83:
        cp.pixels.fill((0,0,0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
        cp.pixels[5] = (1,1,0)
        cp.pixels[6] = (1,1,0)
    elif real_temp > 84:
        cp.pixels.fill((0,0,0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
        cp.pixels[5] = (1,1,0)
        cp.pixels[6] = (1,1,0)
        cp.pixels[7] = (1,0,0)
    elif real_temp > 85:
        cp.pixels.fill((0,0,0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
        cp.pixels[5] = (1,1,0)
        cp.pixels[6] = (1,1,0)
        cp.pixels[7] = (1,0,0)
        cp.pixels[8] = (1,0,0)
    elif real_temp > 86:
        cp.pixels.fill((0,0,0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
        cp.pixels[5] = (1,1,0)
        cp.pixels[6] = (1,1,0)
        cp.pixels[7] = (1,0,0)
        cp.pixels[8] = (1,0,0)
        cp.pixels[9] = (1,0,0)