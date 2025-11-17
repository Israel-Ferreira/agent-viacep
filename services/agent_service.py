from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import tool


from langchain.agents import create_agent

from langchain_google_genai.chat_models import ChatGoogleGenerativeAI


import requests




@tool
def consultar_cep(query):
    """
    Ferramenta que consulta um cep informado pelo usuário no prompt
    e retorna as informações como bairro, coordenadas geograficas, cidade

    Entrada:
        Input Format: Gostaria de buscar o cep 01001-000  (str)
    Saida:
        Output: str

    """

    print(f"Informações: {query} ")
    cep_viacep = "".join(query.split("-"))
    

    url =  f"https://viacep.com.br/ws/{cep_viacep}/json/"
    print(f"Consultando o CEP na URL: {url}")


    response = requests.get(url)

    if response.status_code >= 400:
        return "erro ao consultar o cep"

    content = response.json()


    return  f"Bairro: {content.get('bairro')}, Cidade: {content.get('localidade')}, Estado: {content.get('uf')}"





system_prompt = """
Você é um assistente especializado na busca de informações sobre bairros e endereços, qualquer pergunta 
fora desse contexto, você deve responder 'não sei'.

Use a seguinte ferramentas:
- consultar_cep: ferramenta que permite consultar códigos postais (CEPs) e retorna as informações sobre o bairro, cidade, estado relacionado a aquele.
- duck_duck_go_tool: Buscar informações sobre uma determinada localização no duck-duck-go. Responda sobre informações e curiosidades do local.

No final, forneça uma resposta completa ao usuário com base nas informações obtidas pelas ferramentas. A Resposta deve ser clara e objetiva.
"""



duck_duck_go_tool = DuckDuckGoSearchResults()




tools =  [consultar_cep, duck_duck_go_tool]

llm =  ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
).bind_tools(tools)


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)



def execute_agent(payload: dict):
    user_prompt = payload["user_prompt"]

    resposta_agente = agent.invoke({"messages": [{"role": "user", "content": user_prompt}]})
    print(f"Resposta do agente: {resposta_agente}")


    return ""



