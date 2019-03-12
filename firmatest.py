import pyfirmata 
import time 
#from pyfirmata.util import Iterator
try:
  board = pyfirmata.Arduino("/dev/ttyACM0")
  print("Hardware STM32 connect successfully !")
except: 
    print("Hardware connection fail to connect :(")
board.digital[13].write(1)
it = pyfirmata.util.Iterator(board)
it.start()
board.analog[0].enable_reporting() 
while True:
    print(board.analog[0].read()) 

