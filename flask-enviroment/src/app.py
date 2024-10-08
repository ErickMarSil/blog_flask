from flask import Flask
from src.config_app import setConfigs
from src.jwt_initialize.JwtObj import setJWT

app:Flask = setConfigs(Flask(__name__))
setJWT(app)

@app.route("/", methods=["GET"])
def main():
    return "main"

if __name__ == "__main__":
    app.run(debug=True)