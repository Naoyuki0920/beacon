# -*- coding: utf-8 -*-
import io
import zipfile
from flask import Flask, send_file
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)


@app.route('/get_glb', methods=['GET'])
def get_glb():
    # 子機ごとにURLのさいごの数字を変更
    api_url = 'http://192.168.11.10:5000/confirm_glb/1'
    zip_filename = 'all_files.zip'

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            with open(zip_filename, 'wb') as zip_file:
                zip_file.write(response.content)

        elif response.status_code == 404:
            print('APIが見つかりませんでした。')

        # その他のステータスコードの場合
        else:
            print('error1')

    except requests.exceptions.RequestException as e:
        # リクエストに関連するエラーが発生した場合
        print('error2')

    except Exception as e:
        # その他の例外が発生した場合
        print('error3')

    # ZIPファイルをクライアントに送信
    return send_file(zip_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
