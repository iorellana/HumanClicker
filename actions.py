import time
import pydirectinput as pdi
from random import randint, randrange, choice, choices
from time import sleep, time
import math
from pyclick import HumanClicker
from constants import *

# Create a class for mouse and keyboard actions that uses time.sleep to wait between actions so it get some realism on the movement, using the library pdi
class Actions:
    hc = HumanClicker()

    def __init__(self):
        pass

    # Move actions
    def moveDuration(self, x, y):
        mx, my = pdi.position() # get mouse position
        d = math.sqrt((x - mx)**2 + (y - my)**2) # calculate the distance between the mouse and the destination 
        t = d / MOUSE_SPEED_PIXELS_PER_SECOND # calculate the duration of the movement
        return t # return the duration of the movement plus the distance duration
    
    def move(self, x, y, fixedDuration=0):
        moveDuration = self.moveDuration(x, y) if fixedDuration == 0 else (fixedDuration*0.85)
        # print("moveDuration: ", moveDuration)
        self.hc.move((x, y), moveDuration) # move the mouse to the destination

    # Move to a random location with a random duration, with a chance of success
    def moveRandom(self):
        cx, cy = pdi.position()
        if (randint(1, 3) < 3):
            self.clickPoc(cx + (choice([-1, 1]) * randrange(60, 90)), 
                          cy + (choice([-1, 1]) * randrange(60, 90)))

    # Click actions
    def _click(self, button = pdi.PRIMARY):
        pdi.mouseDown(button=button)
        sleep(WAIT_BETWEEN_CLICKUP_AND_CLICKDOWN * (randint(83, 117) / 100)) # +- 17% variance
        pdi.mouseUp(button=button)

    def _real_click(self):
        '''This function clicks the mouse with realistic errors:
        occasional accidental right click
        occasional double click
        occasional no click'''
        if self.chance(REAL_CLICK_CHANCE):
            sleep(randint(7, 10) / 1000)
            self._click()
        else:
            tmp_rand = randint(1, 3)
            if tmp_rand == 1:
                #double click
                self._click()
                sleep(randint(43, 113) / 1000)
                self._click()
            elif tmp_rand == 2:
                self._click(button=pdi.SECONDARY)

    def click(self):
        self._real_click()

    def clickPoc(self, x, y, fixedDuration=0):
        self.working = True
        self.move(x, y, fixedDuration)
        self.click()
        self.working = False

    # Keyboard actions
    def keyDown(self, key):
        pdi.keyDown(key)

    def keyUp(self, key):
        pdi.keyUp(key)

    def keyPress(self, key):
        self.keyDown(key)
        sleep(randint(9,14)/100)
        self.keyUp(key)

    # Extra actions
    def wait(self, t):
        #randomize the wait time
        sleep(t * randint(83, 117) / 100)

    def chance(self, percentage):
        return choices([True, False], weights=[percentage, 100-percentage], k=1)[0]
