import time
from neopixel import ws, Color, Adafruit_NeoPixel
from Servo import Servo

# servo init
left_ear = Servo(0)
right_ear = Servo(1)

# servo origins
LEFT_EAR_ORIG = 0.5
RIGHT_EAR_ORIG = 0.45
JAWS_ORIG = 0

# move servos to origin
left_ear.write(LEFT_EAR_ORIG)
right_ear.write(RIGHT_EAR_ORIG)

# Neo pixel vars
LED_COUNT = 128  # 64
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 15
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.WS2811_STRIP_GRB

# Color vars
# conftable
con_outer = Color(80, 242, 90)
con_inner = Color(0, 208, 50)
# surprise
sur_outer = Color(142, 170, 219)
sur_inner = Color(47, 84, 150)
# sad
sad_outer = Color(142, 170, 219)
sad_inner = Color(47, 84, 150)
# happy
hap_outer = Color(250, 250, 147)
hap_inner = Color(255, 255, 0)
# calm
cal_outer = Color(142, 170, 219)
cal_inner = Color(47, 84, 150)
# energetic
ene_outer = Color(250, 151, 62)
ene_inner = Color(255, 121, 0)

# Eyes matrix
con_eye = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, con_outer, con_outer, 0, 0, 0,
    0, 0, con_outer, con_outer, con_outer, con_outer, 0, 0,
    0, con_outer, con_outer, con_inner, con_inner, con_outer, con_outer, 0,
    0, con_outer, con_outer, con_inner, con_inner, con_outer, con_outer, 0,
    0, 0, con_outer, con_outer, con_outer, con_outer, 0, 0,
    0, 0, 0, con_outer, con_outer, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]

sur_eye = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, sur_outer, sur_outer, sur_outer, sur_outer, 0, 0,
    0, sur_outer, sur_outer, sur_inner, sur_inner, sur_outer, sur_outer, 0,
    0, sur_outer, sur_outer, sur_inner, sur_inner, sur_outer, sur_outer, 0,
    0, sur_outer, sur_outer, sur_inner, sur_inner, sur_outer, sur_outer, 0,
    0, sur_outer, sur_outer, sur_inner, sur_inner, sur_outer, sur_outer, 0,
    0, 0, sur_outer, sur_outer, sur_outer, sur_outer, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]

sad_eye = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, sad_outer, sad_outer, 0, 0,
    0, 0, 0, sad_outer, sad_outer, sad_outer, sad_outer, 0,
    0, 0, 0, sad_outer, sad_inner, sad_inner, sad_outer, 0,
    0, 0, 0, sad_outer, sad_inner, sad_inner, sad_outer, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, sad_outer, sad_outer, 0, 0, 0, 0,
    0, sad_outer, sad_outer, sad_outer, sad_outer, 0, 0, 0,
    0, sad_outer, sad_inner, sad_inner, sad_outer, 0, 0, 0,
    0, sad_outer, sad_inner, sad_inner, sad_outer, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]

hap_eye = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, hap_outer, hap_outer, hap_outer, hap_outer, 0, 0,
    0, hap_outer, hap_outer, hap_inner, hap_inner, hap_outer, hap_outer, 0,
    0, hap_outer, hap_inner, hap_inner, hap_inner, hap_inner, hap_outer, 0,
    0, hap_outer, hap_inner, hap_inner, hap_inner, hap_inner, hap_outer, 0,
    0, hap_outer, hap_outer, hap_inner, hap_inner, hap_outer, hap_outer, 0,
    0, 0, hap_outer, hap_outer, hap_outer, hap_outer, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]

cal_eye = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, cal_outer, cal_outer, cal_outer, cal_outer, 0, 0,
    0, cal_outer, cal_outer, cal_inner, cal_inner, cal_outer, cal_outer, 0,
    0, cal_outer, cal_outer, cal_inner, cal_inner, cal_outer, cal_outer, 0,
    0, 0, cal_outer, cal_outer, cal_outer, cal_outer, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]

ene_eye = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, ene_outer, ene_outer, ene_outer, ene_outer, 0,
    0, 0, 0, ene_outer, ene_outer, ene_outer, ene_outer, 0,
    0, 0, 0, ene_outer, ene_outer, ene_inner, ene_inner, 0,
    0, 0, 0, ene_outer, ene_outer, ene_inner, ene_inner, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, ene_outer, ene_outer, ene_outer, ene_outer, 0, 0, 0,
    0, ene_outer, ene_outer, ene_outer, ene_outer, 0, 0, 0,
    0, ene_inner, ene_inner, ene_outer, ene_outer, 0, 0, 0,
    0, ene_inner, ene_inner, ene_outer, ene_outer, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]

# util vars
wait_ms = 50
wait_s = 3


def print_conEye(strip):
    """Prints a eye based on a emotion"""
    j = 0
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, con_eye[j])
        if j == 63:
            j = 0
        else:
            j += 1
    strip.show()
    # Ears
    right_ear.write(0.6)
    left_ear.write(0.3)
    time.sleep(wait_s)
    # to origin
    right_ear.write(RIGHT_EAR_ORIG)
    left_ear.write(LEFT_EAR_ORIG)


def print_surEye(strip):
    j = 0
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, sur_eye[j])
        if j == 63:
            j = 0
        else:
            j += 1
    strip.show()
    # Ears
    right_ear.write(0.6)
    left_ear.write(0.3)
    time.sleep(wait_s)
    right_ear.write(RIGHT_EAR_ORIG)
    left_ear.write(LEFT_EAR_ORIG)


def print_sadEye(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, sad_eye[i])
    strip.show()
    # TODO: put servo movements here!!!
    time.sleep(wait_s)


def print_hapEye(strip):
    for i in range(strip.numPixels() / 2):
        strip.setPixelColor(i, hap_eye[i])
    for j in range(strip.numPixels() / 2):
        strip.setPixelColor(j + 64, hap_eye[j])
    strip.show()
    # Ears
    left_ear.write(0.6)
    right_ear.write(0.3)
    time.sleep(wait_s)
    right_ear.write(RIGHT_EAR_ORIG)
    left_ear.write(LEFT_EAR_ORIG)


def print_calEye(strip):
    j = 0
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, cal_eye[j])
        if j == 63:
            j = 0
        else:
            j += 1
    strip.show()
    time.sleep(wait_s)


def print_eneEye(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, ene_eye[i])
    strip.show()
    time.sleep(wait_s)


def colorWipe(strip, color, wait_ms=50):
    """Puts a color on every pixel"""
    for i in range(strip.numPixels() * 2):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


# main function
if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
                              LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL,
                              LED_STRIP)
    strip.begin()

    print("Color wipe")
    colorWipe(strip, Color(255, 255, 255))

    while (True):
        print("Begin eyes animations")
        print("Confortable eyes")
        print_conEye(strip)
        print("Surprise eyes")
        print_surEye(strip)
        print("End eyes animations")
