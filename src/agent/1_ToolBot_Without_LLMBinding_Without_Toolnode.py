"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from __future__ import annotations

from dataclasses import dataclass

from langchain_core.runnables import RunnableConfig

from typing import TypedDict, Annotated, Any, Dict
from langgraph.graph import add_messages, StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from langgraph.graph import START, END
from IPython.display import Image, display

load_dotenv()


class BasicChatBot(TypedDict):
    messages: Annotated[list, add_messages]


search_tool = TavilySearchResults(max_results=2)
tools = [search_tool]

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

llm_with_tools = llm.bind_tools(tools=tools)


def chatbot(state: BasicChatBot):
    return {
        "messages": [llm.invoke(state["messages"])]
    }

def tools_router(state: BasicChatBot):
    last_message = state["messages"][-1]

    if(hasattr(last_message, "tool_calls") and len(last_message.tool_calls) > 0):
        return "tool_node"
    else: 
        return END

tool_node = ToolNode(tools=tools)

graph = (
    StateGraph(BasicChatBot)
    .add_node("chatbot", chatbot)
    .set_entry_point("chatbot")
    .add_conditional_edges("chatbot", tools_router)
    .compile()
)