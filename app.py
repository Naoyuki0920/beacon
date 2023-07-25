from flask import Flask, send_file, render_template, send_from_directory
from flask_cors import CORS

app = Flask( __name__ ) 
CORS(app)

@app.route('/<path:filename>', methods=['GET']) 
# def index():
#     return render_template("index.html")
def send_ARData(filename):
    return send_from_directory("/static", filename, as_attachment=True, mimetype="model/gltf-binary")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
