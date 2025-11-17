from flask import Flask, request
from dotenv import load_dotenv

import config.load_config  # Carrega as variáveis de ambiente

import os

from routes.agent_blueprint import agent_blueprint




app = Flask(__name__)
app.register_blueprint(agent_blueprint)
app.logger.setLevel("INFO")

  



if __name__ == "__main__":
    

    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

    app.logger.debug("API Iniciada...")
    app.run(host="0.0.0.0", port=5000)