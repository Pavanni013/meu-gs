
from flask import Flask, jsonify
from gerar_pix_bot import gerar_pix_bot

app = Flask(__name__)

@app.route("/gerar-pix", methods=["GET"])
def gerar_pix():
    chave = gerar_pix_bot()
    return jsonify({"chave": chave})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
