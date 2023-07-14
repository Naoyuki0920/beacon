from flask import Flask, send_file, render_template
from flask_cors import CORS

app = Flask( __name__ ) 
CORS(app)

@app.route('/', methods=['GET']) 
# def index():
#     return render_template("index.html")
def send_ARData():
    file_path = "CardboardBoxes.gltf"
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
