import pyautogui

class ctrlHandle:

    def __init__(self) -> None:
        self.m1Click = False
        pass

    def relativeMoveCustom(self, relativeX, relativeY, duration=0.01):
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.moveTo(currentMouseX+relativeX, currentMouseY+relativeY, duration, _pause=False)
    
    def relativeMove(self, relativeX, relativeY):
        pyautogui.move(relativeX, relativeY)

    def m1Down(self):
        pyautogui.mouseDown(_pause=False)

    def m1Up(self):
        pyautogui.mouseUp(_pause=False)

    def m2Click(self):
        pyautogui.rightClick(_pause=False)

    def setFailSafe(self, value):
        pyautogui.FAILSAFE = value
        