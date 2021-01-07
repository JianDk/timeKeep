#!/usr/bin/env python
import RPi.GPIO as GPIO
from MFRC522.mfrc522 import SimpleMFRC522
import time

class rfidTimeStamp:
    def readCard(self, **kwargs):
        reader = SimpleMFRC522()
        try:
            idnum, text = reader.read(**kwargs)
        finally:
            GPIO.cleanup()
            return idnum, text 
    
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
    
    def cardStamp(self):
        '''
        Used when employee stamp the card. It will first read the card status.
        If the card status is registered, the status will be set to 'in'.
        If the card status is in, the card status will be set to 'out'.
        If the card status is out, the card status will be set to 'in'
        
        The registration is then recorded in the data base
        '''
        idnum, text = self.readCard()
        print(idnum)
        print(text)
    
    def splitCardString(self, cardString):
        '''
        splits the cardstring with ; delimeter into employee name, employee number and checkin status
        '''
        cardString = cardString.split(';')
        cardDict = {
            'name' : cardString[0],
            'employeeNumber' : cardString[1],
            'check in status' : cardString[2]
        }
        return cardDict


obj = rfidTimeStamp()
obj.cardStamp()
        
