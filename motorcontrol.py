import board
import digitalio
import serial
import time
print("serial conect")
#ser = serial.Serial('/dev/ttyUSB0', 115200)
led1 = digitalio.DigitalInOut(board.P8_3)
led2 = digitalio.DigitalInOut(board.P8_4) 
led3 = digitalio.DigitalInOut(board.P8_5) 
led4 = digitalio.DigitalInOut(board.P8_6) 
led5 = digitalio.DigitalInOut(board.P8_7) 
led6 = digitalio.DigitalInOut(board.P8_8) 
led7 = digitalio.DigitalInOut(board.P8_9) 
led8 = digitalio.DigitalInOut(board.P8_10) 
led9 = digitalio.DigitalInOut(board.P8_11) 
led10 = digitalio.DigitalInOut(board.P8_12) 
led11 = digitalio.DigitalInOut(board.P8_13) 
led12 = digitalio.DigitalInOut(board.P8_14) 
led13 = digitalio.DigitalInOut(board.P8_15) 
led14 = digitalio.DigitalInOut(board.P8_16) 
led15 = digitalio.DigitalInOut(board.P8_17) 
led16 = digitalio.DigitalInOut(board.P8_18) 

led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
led3.direction = digitalio.Direction.OUTPUT
led4.direction = digitalio.Direction.OUTPUT
led5.direction = digitalio.Direction.OUTPUT
led6.direction = digitalio.Direction.OUTPUT
led7.direction = digitalio.Direction.OUTPUT
led8.direction = digitalio.Direction.OUTPUT
led9.direction = digitalio.Direction.OUTPUT
led10.direction = digitalio.Direction.OUTPUT
led11.direction = digitalio.Direction.OUTPUT
led12.direction = digitalio.Direction.OUTPUT
led13.direction = digitalio.Direction.OUTPUT
led14.direction = digitalio.Direction.OUTPUT
led15.direction = digitalio.Direction.OUTPUT
led16.direction = digitalio.Direction.OUTPUT

def led_on(num):
  
    if(num == 1):
        print("works")
        led1.value = True
    
    if(num == 2):
        led2.value = True
        
    if(num == 3):
        led3.value = True
        
    if(num == 4):
        led4.value = True
        
    if(num == 5):
        led5.value = True
        
    if(num == 6):
        led6.value = True
        
    if(num == 7):
        led7.value = True
        
    if(num == 8):
        led8.value = True
        
    if(num == 9):
        led9.value = True
        
    if(num == 10):
        led10.value = True
        
    if(num == 11):
        led11.value = True
        
    if(num == 12):
        led12.value = True
        
    if(num == 13):
        led13.value = True
        
    if(num == 14):
        led4.value = True
        
    if(num == 15):
        led15.value = True
        
    if(num == 16):
        led16.value = True
        
def led_off(num):
    if(num == 1):
        print("works")
        led1.value = False
    
    if(num == 2):
        led2.value = False
        
    if(num == 3):
        led3.value = False
        
    if(num == 4):
        led4.value = False
        
    if(num == 5):
        led5.value = False
        
    if(num == 6):
        led6.value = False
        
    if(num == 7):
        led7.value = False
        
    if(num == 8):
        led8.value = False
        
    if(num == 9):
        led9.value = False
        
    if(num == 10):
        led10.value = False
        
    if(num == 11):
        led11.value = False
        
    if(num == 12):
        led12.value = False
        
    if(num == 13):
        led13.value = False
        
    if(num == 14):
        led4.value = False
        
    if(num == 15):
        led15.value = False
        
    if(num == 16):
        led16.value = False


# def motor_control(position):
    
#     if(position == 1):
#         time.sleep(2)
#         print("rotating")
#         ser.write(str.encode("G1 X0 F3000\r\n"))
#         print("done")
#         time.sleep(1)
        
#     if(position == 2):
#         time.sleep(2)
#         print("rotating")
#         ser.write(str.encode("G1 X10 F3000\r\n"))
#         print("done")
#         time.sleep(1)
        
#     if(position == 3):
#         time.sleep(2)
#         print("rotating")
#         ser.write(str.encode("G1 X20 F3000\r\n"))
#         print("done")
#         time.sleep(1)
        
#     if(position == 4):
#         time.sleep(2)
#         print("rotating")
#         ser.write(str.encode("G1 X30 F3000\r\n"))
#         print("done")
#         time.sleep(1)
        

# ser.close()
