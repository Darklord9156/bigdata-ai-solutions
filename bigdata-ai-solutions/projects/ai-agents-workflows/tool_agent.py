import json, os, math
from typing import Dict, Any
from langchain.tools import tool
from langchain_openai import ChatOpenAI

@tool
def calc_square_root(x: float) -> float:
    """Return the square root of x."""
    return math.sqrt(x)

def main():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    # Simple ReAct-style prompt demonstrating tool use
    user_query = "What is the square root of 256? Use tools if needed."
    # For brevity, we'll just call the tool directly here:
    result = calc_square_root.run(256.0)
    print(f"Agent tool result: {result}")

if __name__ == "__main__":
    main()