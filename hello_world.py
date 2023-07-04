from flask import Flask, send_file

app = Flask( __name__ ) 

@app.route('/', methods=['GET']) 
def send_ARData():
    file_path = "NeilArmstrong.glb"
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
