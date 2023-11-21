import os
import io
import zipfile
import requests
from flask import Flask, send_file

app = Flask(__name__)

def get_glb():
    # 子機ごとにURLのさいごの数字を変更
    api_url = 'http://192.168.75.10:5000/confirm_glb/1'

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            zip_filename = 'all_files.zip'
            with open(zip_filename, 'wb') as zip_file:
                zip_file.write(response.content)

        elif response.status_code == 404:
            print('APIが見つかりませんでした。')

        # その他のステータスコードの場合
        else:
            print(f'APIにアクセスできませんでした。ステータスコード: {response.status_code}')

    except requests.exceptions.RequestException as e:
        # リクエストに関連するエラーが発生した場合
        print(f'リクエストエラーが発生しました: {e}')

    except Exception as e:
        # その他の例外が発生した場合
        print(f'エラーが発生しました: {e}')

    # ZIPファイルをクライアントに送信
    return send_file(zip_filename, as_attachment=True)

if __name__ == "__main__":
    app.run()
