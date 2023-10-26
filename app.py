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
    # ディレクトリ内のファイルを取得
    files = os.listdir("./static")
    for file in files:
        file_path = os.path.join("./static", file)
        os.remove(file_path)
    
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
    
    files = os.listdir(save_directory)
    zip_filename = 'all_files.zip'
    # ZIPファイルを作成
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            # ファイルをZIPに追加
            file_path = os.path.join(save_directory, file)
            zipf.write(file_path, os.path.basename(file_path))
    # ZIPファイルをクライアントに送信
    return send_file(zip_filename, as_attachment=True)

    # glb_file_path = '1.glb'
    # return send_file(glb_file_path, as_attachment=True, mimetype='model/gltf-binary')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
