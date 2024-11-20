from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = .025
right = [1,2,3,4,8,9]
left = [1,3,5,6]
back = [2,4,8]
forward = [3,5,6,7]
while True:
     x, y, z = cp.acceleration
     if x < -5:
        if cp.button_a:
          cp.pixels.fill((0,0,0))
          for n in right:
               cp.pixels[n] = (255,0,0)
          time.sleep(.200)
     elif x > 5:
         if cp.button_a:
               cp.pixels.fill((0,0,0))
               for n in left:
                    cp.pixels[n] = (0,255,0)
               time.sleep(.200)
     if y > 5:
         if cp.button_a:
               cp.pixels.fill((0,0,0))
               for n in back:
                    cp.pixels[n] = (0,0,255)
               time.sleep(.200)
     if y < -5:
          if cp.button_a:
               cp.pixels.fill((0,0,0))
               for n in forward:
                    cp.pixels[n] = (255,165,0)
               time.sleep(.200)
       