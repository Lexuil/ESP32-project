from machine import SPI,Pin

sck = Pin(18, Pin.OUT)
mosi = Pin(23, Pin.OUT)
miso = Pin(19)
rst = Pin(22, Pin.OUT)
cs = Pin(21, Pin.OUT)

spi = SPI(baudrate=1000000, polarity=0, phase=0,sck=sck, mosi=mosi, miso=miso)

spi.init()

spi.write(b'0x7e')
spi.write(b'0x7f')
spi.write(b'0x7g')
spi.write(b'0x7h')
