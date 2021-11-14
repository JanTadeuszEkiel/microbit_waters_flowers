def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 1)
    led.plot(0, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P0, 0)
    led.unplot(0, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

pins.digital_write_pin(DigitalPin.P0, 0)
led.unplot(0, 0)

def on_every_interval():
    pins.digital_write_pin(DigitalPin.P0, 1)
    led.plot(0, 0)
    basic.pause(150000)
    pins.digital_write_pin(DigitalPin.P0, 0)
    led.unplot(0, 0)
loops.every_interval(86400000, on_every_interval)
