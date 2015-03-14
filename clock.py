import lcddriver
import time

lcd = lcddriver.lcd()
while True:

    #lcd.lcd_display_string("16X2 I2C Display", 1)
    #lcd.lcd_display_string("Buy@ Ryanteck.uk", 2)
    lcd.lcd_display_string(time.strftime("%a, %B %d %Y"), 1)
    lcd.lcd_display_string(time.strftime("%I:%M:%S %p"), 2)
    time.sleep(.5)
