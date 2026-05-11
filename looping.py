from langgraph.graph import StateGraph, START, END
from typing import List, TypedDict
from IPython.display import Image, display

class AgentState(TypedDict):
    counter: int

def decrement_node(state: AgentState) -> AgentState:
    """Function to decrement the counter by 1"""
    state["counter"] -= 1

    return state

def should_continue(state: AgentState) -> AgentState:
    """Function to decide what to do next"""
    if state["counter"] > 0:
        print("ENTERING LOOP", state["counter"])
        return "loop"  # Continue looping
    else:
        return "exit"  # Exit the loop
    
graph = StateGraph(AgentState)

graph.add_node("decrement", decrement_node)

graph.add_edge(START, "decrement")
graph.add_conditional_edges(
    "decrement",
    should_continue,
    {
        "loop": "decrement",  
        "exit": END          
    }
)

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

input = AgentState(number=[], counter=5)
app.invoke(input)