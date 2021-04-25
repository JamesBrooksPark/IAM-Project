from microbit import *

def Button_Press(chan, n, value):
    MIDI_Press = 0xB0
    if chan > 15:
        return
    if n > 127:
        return
    if value > 127:
        return
    msg = bytes([MIDI_Press | chan, n, value])
    uart.write(msg)

def Start():
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)

Start()
ButtonA = False
ButtonB = False
ButtonC = False
ButtonD = False

barcounter = 0
displaykey = 0

while True:
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    c = pin1.is_touched()
    d = pin2.is_touched()

    if a is True and ButtonA is False:
        Button_Press(0, 22, 127)
        displaykey = displaykey + 1
        if displaykey == 6:
            displaykey = 1

    if b is True and ButtonB is False:
        Button_Press(0, 23, 127)
        if displaykey == 3:
            barcounter = 0
            display.show(barcounter)
    if c is True and ButtonC is False:
        Button_Press(0, 24, 127)
    if d is True and ButtonD is False:
        Button_Press(0, 25, 127)
        barcounter = barcounter + 1
        display.show(barcounter)
    ButtonA = a
    ButtonB = b
    ButtonC = c
    ButtonD = d

    sleep(5)