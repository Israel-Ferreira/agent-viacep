from typing_extensions import TypedDict


class AgentState(TypedDict):
    user_query: str
    viacep_tool_result: str
    search_result: str
    final_answer: str
