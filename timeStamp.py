#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

class rfidTimeStamp:
    def readCard(self):
        reader = SimpleMFRC522()

        try:
            id, text = reader.read()
            print(id)
            print(text)
        finally:
            GPIO.cleanup()
        time.sleep(5) #Introduced to avoid unintended card read again after the first read
    
    def writeCard(self, text):
        reader = SimpleMFRC522()

        try:
            reader.write(text) #The text will only be written after the reader registers card contact
            print(f"{text} written to the card!")
        finally:
            GPIO.cleanup()
        time.sleep(5) #Introduced so that the card will not be accidentially read again within short time
        
