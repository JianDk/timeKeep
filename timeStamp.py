#!/usr/bin/env python
import RPi.GPIO as GPIO
from MFRC522.mfrc522 import SimpleMFRC522
import time

class rfidTimeStamp:
    def readCard(self, **kwargs):
        reader = SimpleMFRC522()
        try:
            id, text = reader.read(**kwargs)
        finally:
            GPIO.cleanup()
        time.sleep(5) #Introduced to avoid unintended card read again after the first read
    
    def writeCard(self, text, **kwargs):
        reader = SimpleMFRC522()

        try:
            idnum, textin = reader.write(text, **kwargs) #The text will only be written after the reader registers card contact
        except:
            GPIO.cleanup()
            idnum, textin = reader.write(text, **kwargs)
        finally:
            GPIO.cleanup()
            return idnum, textin
        
