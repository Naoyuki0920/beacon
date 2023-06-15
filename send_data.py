import bluetooth
import time

# BluetoothデバイスのMACアドレス
target_address = '3c:01:ef:33:d8:b8'

# Bluetoothデバイスに接続
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("1")
sock.connect((target_address, 1))
time.sleep(5)
print("2")
# テキストを送信
text = 'Hello from Raspberry Pi!'
sock.send(text)
print("3")
# 接続を閉じる
sock.close()
