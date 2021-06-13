import board
import busio
#import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import adafruit_character_lcd.character_lcd_i2c as Character_LCD_I2C

lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = Character_LCD_I2C.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)
lcd.clear()
