from network import Sigfox
import socket
import time
import pycom
from L76GNSS import L76GNSS 
from pytrack import Pytrack 

py = Pytrack() 
l76 = L76GNSS(py, timeout=60)

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(False)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

while(True):
	print("init")
 
	# send some bytes	
	coord = l76.coordinates() 
	print(coord)
	s.send(str(coord[0]))
	
	print("Sent 1")
	
	time.sleep(5)
	s.send(str(coord[1]))

	print("sent 2")
	pycom.rgbled(0xff00)
	time.sleep(1)
	pycom.rgbled(0x0000)
	time.sleep(23)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	