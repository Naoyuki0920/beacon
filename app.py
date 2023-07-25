from flask import Flask, send_file, render_template
from flask_cors import CORS

app = Flask( __name__ ) 
CORS(app)

@app.route('/get_glb', methods=['GET'])
def get_glb():
    # glbファイルのパスを指定してバイナリデータとして読み込む
    glb_file_path = 'NeilArmstrong.glb'
    return send_file(glb_file_path, as_attachment=True, mimetype='model/gltf-binary')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
