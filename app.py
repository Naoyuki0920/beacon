from flask import Flask, send_file
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)


@app.route('/get_glb', methods=['GET'])
def get_glb():
    api_url = 'http://192.168.75.10:5000/confirm_glb/1'
    response = requests.get(api_url)

    save_directory = "/"
    os.makedirs(save_directory, exist_ok=True)
    file_path = os.path.join(save_directory, '1.glb')
    with open(file_path, 'wb') as file:
        file.write(response.content)

    glb_file_path = '1.glb'
    return send_file(glb_file_path, as_attachment=True, mimetype='model/gltf-binary')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
