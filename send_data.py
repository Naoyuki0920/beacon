import bluetooth

# BluetoothデバイスのMACアドレス
target_address = '3c:01:ef:33:d8:b8'

# Bluetoothデバイスに接続
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, 1))

# テキストを送信
text = 'Hello from Raspberry Pi!'
sock.send(text)

# 接続を閉じる
sock.close()
