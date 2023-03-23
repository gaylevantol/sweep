led = pins.D13.digital_write()
def on_forever():
    led.value = False
forever(on_forever)