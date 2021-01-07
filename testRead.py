from MFRC522.mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

obj = SimpleMFRC522()
try:
    idnum, text = obj.read(timeout = 10)
except:
    print('error')
    GPIO.cleanup()
    idnum, text = obj.read(timeout = 10)
finally:
    GPIO.cleanup()

print(idnum)
print(text)