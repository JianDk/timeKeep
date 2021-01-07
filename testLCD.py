from RPLCD.i2c import CharLCD
import time
lcd = CharLCD('PCF8574', 0x27, backlight_enabled = True)
lcd.cursor_pos = (0,0)
lcd.write_string('hello world')
lcd.cursor_pos = (1,0)
lcd.write_string('This is Jian')
time.sleep(5)
lcd.clear()