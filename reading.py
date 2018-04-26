bus = smbus.SMBus(1)

DEVICE_ADDRESS = 0x1e

data = []
data.append(bus.read_byte_data(DEVICE_ADDRESS, 0x03))
for i in range(1, 6):
    data.append(bus.read_byte_data(DEVICE_ADDRESS, 0x03 + i))

print(data)
