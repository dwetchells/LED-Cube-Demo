import board
import time
import neopixel
import touchio
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.pulse import Pulse

setcolor = 0x005555
leds = neopixel.NeoPixel(board.A0, 64*6, brightness=0.2, auto_write=False)
pulse = Pulse(leds, speed=0.1, color = 0x110011, period = 2)
rainbowsparkle = RainbowSparkle(leds, speed=0.1, num_sparkles=15)
sparklepulse = SparklePulse(leds, speed=0.1, color = setcolor)

rainbowcomet = RainbowComet(leds, speed=0.05, tail_length=20)

touched = time.monotonic()

touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touching = 0

while True:
    if time.monotonic() - touched < 0.15:

        continue
    if touch1.value or touching == 1:
        rainbowsparkle.animate()
        touching = 1

    if touch2.value or touching == 2:
        rainbowcomet.animate()
        touching = 2

    if touch3.value or touching == 3:
        sparklepulse.animate()
        touching = 3

    leds.show()



