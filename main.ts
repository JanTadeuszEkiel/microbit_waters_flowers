input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    led.plot(0, 0)
})
input.onButtonPressed(Button.B, function () {
    pins.digitalWritePin(DigitalPin.P0, 0)
    led.unplot(0, 0)
})
pins.digitalWritePin(DigitalPin.P0, 0)
led.unplot(0, 0)
loops.everyInterval(86400000, function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    led.plot(0, 0)
    basic.pause(150000)
    pins.digitalWritePin(DigitalPin.P0, 0)
    led.unplot(0, 0)
})
