from flask.blueprints import Blueprint
from flask import request

from services.agent_service import execute_agent

agent_blueprint = Blueprint("agent_blueprint", __name__)

@agent_blueprint.route("/agent-via-cep", methods=["POST"])
def consultar_cep_via_ia():
    payload = request.get_json()
    resposta = execute_agent(payload)
    return {"resposta": resposta}