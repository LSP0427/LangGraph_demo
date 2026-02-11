from langgraph.graph import StateGraph, START, END
import random
from typing import List, TypedDict
from IPython.display import Image, display

class AgentState(TypedDict):
    number: List[int]
    counter: int

def random_node(state: AgentState) -> AgentState:
    """Generates a random number from 0 to 10"""
    state["number"].append(random.randint(0, 10))
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

graph.add_node("random", random_node)

graph.add_edge(START, "random")
graph.add_conditional_edges(
    "random",     # Source node
    should_continue, # Action
    {
        "loop": "random",  
        "exit": END          
    }
)

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

app.invoke({"number":[], "counter":5})