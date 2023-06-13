import bluetooth

# ペアリングされたデバイスの検索
print("Searching for devices...")
devices = bluetooth.discover_devices(lookup_names=True)
print("Devices found")

# デバイスの一覧表示
for addr, name in devices:
    print(f"{name} ({addr})")

# 送信先デバイスのBluetoothアドレス。この例では、リストから手動で選択します。
bd_addr = "3c:01:ef:33:d8:b8"

port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

msg = "Hello from Raspberry Pi!"
sock.send(msg)

sock.close()
