from flask import Flask, send_file
from flask_cors import CORS
import requests

app = Flask( __name__ ) 
CORS(app)

@app.route('/get_glb', methods=['GET'])
def get_glb():
    requests.get('http://192.168.75.10:5000/confirm_glb/1')
    glb_file_path = 'Astronaut.glb'
    return send_file(glb_file_path, as_attachment=True, mimetype='model/gltf-binary')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
