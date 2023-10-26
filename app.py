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
    api_url = 'http://192.168.75.10:5000/confirm_glb/1'
    response = requests.get(api_url)

    save_directory = "./static"
    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
        # ファイルを保存するディレクトリが存在しない場合は作成
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # ZIPファイル内のファイルを展開して保存
        zip_ref.extractall(save_directory)

    # glb_file_path = '1.glb'
    # return send_file(glb_file_path, as_attachment=True, mimetype='model/gltf-binary')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
