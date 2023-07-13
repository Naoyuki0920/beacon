from flask import Flask, send_file, render_template
from flask_cors import CORS

app = Flask( __name__ ) 
CORS(app)

@app.route('/', methods=['GET']) 
def index():
    return render_template("index.html")
# def send_ARData():
#     file_path = "NeilArmstrong.glb"
#     return send_file(file_path, as_attachment=True)

if __name__ == '__main__': 
    import ssl
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_context.load_cert_chain(
        'fullchain.pem', 'privkey.pem'
    )
    app.run(host='0.0.0.0', port=5000, ssl_context=ssl_context)
