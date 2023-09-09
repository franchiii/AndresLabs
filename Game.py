from Displays import *

class Game:
  def __init__(self, playerName, welcomeMessage, exitMessage, danceLedPin):
    self.playerName = playerName
    self.welcomeM = welcomeMessage
    self.exitM = exitMessage
    self.danceLedPin = danceLedPin
  
  def interestingLedDance(self):
    exled = DimLight(self.danceLedPin,'Blue LED')
    exled.on()
    utime.sleep(1)
    exled.setBrightness(100)
    utime.sleep(1)
    exled.off()
    utime.sleep(1)
    exled.on()
    exled.setBrightness(100)
    exled.off()

  def printWelcomeMessage(self):
    Display=LCDDisplay(sda=0,scl=1,i2cid=0)
    Display.showText(self.welcomeM)
    Buzzer=PassiveBuzzer(16)
    Buzzer.beep()
    print(self.welcomeM)

  def printExitMessage(self):
    print(self.exitMessage)
    Buzzer=PassiveBuzzer(16)
    Buzzer.beep()

  

