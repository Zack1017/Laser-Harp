import time
import board
import neopixel
from rainbowio import colorwheel

pixel_pin = board.A1
LED_COUNT = 144
ZONE_COUNT = 8
LEDS_PER_ZONE = LED_COUNT // ZONE_COUNT



current_color_index = 0

def set_zone_brightness(zone, base_color, brightness):
    start = zone * LEDS_PER_ZONE
    end = start + LEDS_PER_ZONE

    r = (base_color[0] * brightness) // 255
    g = (base_color[1] * brightness) // 255
    b = (base_color[2] * brightness) // 255

    for i in range(start, end):
        strip[i] = (r, g, b)
    strip.show()

def pulse_zone(zone, color, speed):
    for b in range(0, 256, speed):
        set_zone_brightness(zone, color, b)
        time.sleep(0.004)
    for b in range(255, -1, -speed):
        set_zone_brightness(zone, color, b)
        time.sleep(0.004)

def set_zone_color(zone, color, brightness):
    start = zone * LEDS_PER_ZONE
    end = start + LEDS_PER_ZONE

    # Scale color values by brightness (brightness is 0-255)
    r = (color[0] * brightness) // 255
    g = (color[1] * brightness) // 255
    b = (color[2] * brightness) // 255

    for i in range(start, end):
        strip[i] = (r, g, b)

    strip.show()