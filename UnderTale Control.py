from pynput.keyboard import Key, Controller
import cwiid
import time
#Setting up the Wii Remote
print ("Press 1 and 2 on your  Wii Remote now.")
attempt = 0
wm = None
while not wm:
    attempt += 1
    print("Attempt %i" %(attempt))
    try:
        wm=cwiid.Wiimote()
    except:
        print("Failed to connect to the Wiimote on try: %i" %(attempt))
#Rumble to alert the user of the connection success
for i in range(0,2):
    wm.rumble = True
    time.sleep(0.5)
    wm.rumble = False
print("Found Wii Remote on try %i." %(attempt))
##Setting the report modes and LED
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
wm.led = 1
#Setting up the keyboard management
keyboard= Controller()
#Variables to help remember the state of the buttons we are virutally pressing
pressingup=False
pressingdown=False
pressingleft=False
pressingright=False
pressingx=False
pressingshift=False
pressingenter=False
pressingctrl=False
pressingesc=False

print("Press the Home Buttont to exit")
while not (wm.state['buttons'] & cwiid.BTN_HOME):
    #Control Statements
    if wm.state['buttons'] & cwiid.BTN_RIGHT:
        keyboard.press(Key.up)
        pressingup=True
    elif pressingup==True:
        keyboard.release(Key.up)
        pressingup=False

    if wm.state['buttons'] & cwiid.BTN_LEFT:
        keyboard.press(Key.down)
        pressingdown=True
    elif pressingdown==True:
        keyboard.release(Key.down)
        pressingdown=False

    if wm.state['buttons'] & cwiid.BTN_UP:
        keyboard.press(Key.left)
        pressingleft=True
    elif pressingleft==True:
        keyboard.release(Key.left)
        pressingleft=False

    if wm.state['buttons'] & cwiid.BTN_DOWN:
        keyboard.press(Key.right)
        pressingright=True
    elif pressingright==True:
        keyboard.release(Key.right)
        pressingright=False

    if wm.state['buttons'] & cwiid.BTN_A:
        keyboard.press('x')
        pressingx=True
        time.sleep(0.1)
    elif pressingx==True:
        keyboard.release('x')
        pressingx=False

    if wm.state['buttons'] & cwiid.BTN_1:
        keyboard.press(Key.shift)
        pressingshift=True
    elif pressingshift==True:
        keyboard.release(Key.shift)
        pressingshift=False

    if wm.state['buttons'] & cwiid.BTN_2:
        keyboard.press(Key.enter)
        pressingenter=True
    elif pressingenter==True:
        keyboard.release(Key.enter)
        pressingenter=False

    if wm.state['buttons'] & cwiid.BTN_MINUS:
        keyboard.press(Key.ctrl)
        pressingctrl=True
    elif pressingenter==True:
        keyboard.release(Key.ctrl)
        pressingctrl=False

    if wm.state['buttons'] & cwiid.BTN_PLUS:
        keyboard.press(Key.esc)
        pressingesc=True
    elif pressingesc==True:
        keyboard.release(Key.esc)
        pressingesc=False
