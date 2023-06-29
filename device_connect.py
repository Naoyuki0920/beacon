import bluepy

scanner = bluepy.btle.Scanner(0)
device = scanner.scan(5)  #5秒間スキャン

for device in device:
    if device.addr == "3c:01:ef:33:d8:b8":
        distance = 10 ** ((-59 - device.rssi)/(10 * 2))
        print('address : %s' % device.addr)
        print('addrType: %s' % device.addrType)
        print('RSSI    : %s' % device.rssi)
        print('range   : %s' % distance)
        print('Adv data:')
        for (adtype, desc, value) in device.getScanData():
            print(' (%3s) %s : %s ' % (adtype, desc, value))