import pyautogui as pag
from pynput import mouse, keyboard
import time
pag.PAUSE = 0
pag.FAILSAFE = True 
width,height = pag.size()

failSafe = True 

class Autoclick:
    auto = False 
    saveX = 0
    saveY = 0
    @staticmethod
    def on_press(key):
        try:
            # print('alphanumeric key {0} pressed'.format(
            #     key.char))
            if(key.char == "`"):
                if(Autoclick.auto):
                    print("Autoclick deactivated")
                    Autoclick.auto = False
                    Autoclick.save = ()
                else:
                    print("Autoclick activated")
                    Autoclick.auto = True
                    Autoclick.saveX, Autoclick.saveY = pag.position()
            # else:
            #     print("Key "+key.char+" added")
            #     if(key.char not in Autoclick.keyList):
            #         Autoclick.keyList.append(key.char)
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
    @staticmethod
    def on_release(key):
        global failSafe
        if key == keyboard.Key.esc:
            print("escape key pressed, exiting keyboard listener")
            failSafe = False
            return False
    # @staticmethod 
    # def on_click(x,y,button,pressed):
    #     if Autoclick.auto:
    #         if(button == mouse.Button.left):
    #             if pressed:
    #                 if Autoclick.save != ():
    #                     Autoclick.save = (x,y)
    @staticmethod
    def update():
        if(Autoclick.auto):
            mx, my = pag.position()
            pag.click(Autoclick.saveX,Autoclick.saveY,interval=0)
            print("clicked")
            pag.moveTo(mx, my)

listenerk = keyboard.Listener(
        on_press=Autoclick.on_press,
        on_release=Autoclick.on_release)
listenerk.start()

# listenerm = mouse.Listener(
#         on_click=Autoclick.on_click)
# listenerm.start()

print("listening to keyboard and mouse!")
while failSafe:
    Autoclick.update()
    time.sleep(1)