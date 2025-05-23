# LangGraph Tool Calling POC


The graphs are defined in `src/agent/` folder.

Tavily Search has been used as the tool in this project.

## Key findings

1. **Without LLM tool binding and without LangGraph ToolNode**: The LLM will answer directly, no calls will be made by the tool
2. **Without LLM tool binding and with LangGraph ToolNode**: The LLM will answer directly, no calls will be made by the tool
3. **With LLM tool binding and without LangGraph ToolNode**: The LLM use the tool to answer but the ToolNode by LangGraph will not be used.
4. **With LLM tool binding and with LangGraph ToolNode**: The LLM use the tool to answer and the ToolNode by LangGraph will be used.
