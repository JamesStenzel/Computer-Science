from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = .025
step = 0
def fail():
     cp.pixels.fill((255,0,0))
     cp.play_tone(500,.500)
     cp.pixels.fill((0,0,0))
def win():
     global step
     cp.pixels.fill((0,255,0))
     cp.play_tone(800,.500)
     cp.pixels.fill((0,0,0))
     step = 0
while True:
     if step == 0:
          if cp.button_a:
               cp.pixels[0] = (0,255,165)
               step +=1
               time.sleep(.200)
          elif cp.button_b:
               fail()
               step = 0
               time.sleep(.200)
     elif step == 1:
          if cp.button_a:
               cp.pixels[1] = (0,255,165)
               step += 1
               time.sleep(.200)
          elif cp.button_b:
               fail()
               step = 0
               time.sleep(.200)
     elif step == 2:
          if cp.button_b:
               cp.pixels[2] = (0,255,165)
               step += 1
               time.sleep(.200)
          elif cp.button_a:
               fail()
               step = 0
               time.sleep(.200)
     elif step == 3:
          if cp.button_a:
               cp.pixels[3] = (0,255,165)
               step += 1
               time.sleep(.200)
          elif cp.button_b:
               fail()
               step = 0
               time.sleep(.200)
     elif step == 4:
          if cp.button_b:
               cp.pixels[4] = (0,255,165)
               step += 1
               time.sleep(.200)
          elif cp.button_a:
               fail()
               step = 0
               time.sleep(.200)
     elif step == 5:
          if cp.button_b:
               cp.pixels[5] = (0,255,165)
               step += 1
               time.sleep(.200)
          elif cp.button_a:
               fail()
               step = 0
               time.sleep(.200)
     elif step == 6:
          if cp.button_b:
               cp.pixels[6] = (0,255,165)
               step += 1
               time.sleep(.200)
          elif cp.button_a:
               fail()
               step = 0
               time.sleep(.200)
     elif step == 7:
          if cp.button_a:
               cp.pixels[7] = (0,255,165)
               step += 1
               time.sleep(.200)
          elif cp.button_b:
               fail()
               step = 0
               time.sleep(.200)
     elif step == 8:
          if cp.button_a and cp.button_b:
               cp.pixels[8] = (0,255,165)
               win()
               time.sleep(.200)
          