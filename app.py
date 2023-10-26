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

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            files = os.listdir("./static")
            for file in files:
                file_path = os.path.join("./static", file)
                os.remove(file_path)

            with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
                # ファイルを保存するディレクトリが存在しない場合は作成
                if not os.path.exists("./static"):
                    os.makedirs("./static")

                # ZIPファイル内のファイルを展開して保存
                zip_ref.extractall("./static")

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

    files = os.listdir("./static")
    zip_filename = 'all_files.zip'
    # ZIPファイルを作成
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            # ファイルをZIPに追加
            file_path = os.path.join("./static", file)
            zipf.write(file_path, os.path.basename(file_path))
    # ZIPファイルをクライアントに送信
    return send_file(zip_filename, as_attachment=True)

    # glb_file_path = '1.glb'
    # return send_file(glb_file_path, as_attachment=True, mimetype='model/gltf-binary')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
