from bluepy.btle import Peripheral, DefaultDelegate

# ビーコンのUUID

# ビーコンのアドレス
beacon_address = "XX:XX:XX:XX:XX:XX"

# 距離計算のための定数
RSSI_1m = -60  # ビーコンから1m離れた場合のRSSI値

# ビーコンからの距離を計算する関数
def calculate_distance(rssi):
    ratio = rssi / RSSI_1m
    if ratio < 1.0:
        return pow(ratio, 10)
    else:
        return (0.89976) * pow(ratio, 7.7095) + 0.111

# ビーコンとの通信用のデリゲートクラス
class BeaconDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        # ビーコンからの通知を受け取った場合の処理
        rssi = int.from_bytes(data, byteorder='little', signed=True)
        distance = calculate_distance(rssi)
        print("Distance:", distance, "m")

# ビーコンとの接続および通信開始
beacon = Peripheral(beacon_address)
beacon.withDelegate(BeaconDelegate())
beacon.writeCharacteristic(0x12, b"\x01\x00")  # ビーコンの通知を有効化

# 通信ループを開始
while True:
    if beacon.waitForNotifications(1.0):
        continue
