import bluetooth

# Bluetoothデバイスの情報
target_name = "Xperia 5"
target_address = None

# Bluetoothデバイスの検索
nearby_devices = bluetooth.discover_devices()
for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name(bdaddr):
        target_address = bdaddr
        break

if target_address is not None:
    print("デバイスが見つかりました:", target_address)
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((target_address, 1))

    # メッセージを送信
    message = "Hello from Raspberry Pi!"
    socket.send(message)

    # ソケットを閉じる
    socket.close()
else:
    print("デバイスが見つかりませんでした.")
