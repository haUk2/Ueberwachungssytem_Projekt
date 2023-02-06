import time
import board
import busio as io
import adafruit_mlx90614
import pyrebase
import smbus

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

config = {
  "apiKey": "MiDHkMalq3pwZaMji4NvGn3VNisqiSFVY8WcAXOn",
  "authDomain": "test-b70f3.firebaseapp.com",
  "databaseURL": "https://test-b70f3-default-rtdb.europe-west1.firebasedatabase.app/",
  "storageBucket": "test-b70f3.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")
print("----------------------------------------")
print()

while True:
  i2cbus = smbus.SMBus(1)
  time.sleep(0.5)

  data = i2cbus.read_i2c_block_data(address,0x71,1)
  if (data[0] | 0x08) == 0:
    print('Initialization error')

  i2cbus.write_i2c_block_data(address,0xac,[0x33,0x00])
  time.sleep(0.1)

  data = i2cbus.read_i2c_block_data(address,0x71,7)

  Traw = ((data[3] & 0xf) << 16) + (data[4] << 8) + data[5]
  temperature = 200*float(Traw)/2**20 - 50

  Hraw = ((data[3] & 0xf0) >> 4) + (data[1] << 12) + (data[2] << 4)
  humidity = 100*float(Hraw)/2**20
    
  print(temperature)
  print(humidity)

