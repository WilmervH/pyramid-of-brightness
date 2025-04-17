import machine
import neopixel
import time

WIDTH = 16
HEIGHT = 16
NUM_PIXELS = WIDTH * HEIGHT

PIN_NUM = 0
np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_PIXELS)

def set_pixel(x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        index = y * WIDTH + x
        np[index] = color
        np.write()

def sweep():
    color = (255, 255, 255)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            set_pixel(x, y, color)
            time.sleep(0.01)
    time.sleep(1)

sweep()
