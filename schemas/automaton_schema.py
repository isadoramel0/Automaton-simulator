from pydantic import BaseModel
from typing import Dict, List

class FiniteAutomatonSchema(BaseModel):
    states: List[str]
    alphabet: List[str]
    transitions: Dict[str, Dict[str, str]]
    initial_state: str
    final_states: List[str]

class PushdownAutomatonSchema(BaseModel):
    states: List[str]
    alphabet: List[str]
    stack_symbols: List[str]
    transitions: Dict[str, Dict]
    initial_state: str
    initial_stack_symbol: str
    final_states: List[str] 
    acceptance_mode: str

class TuringMachineSchema(BaseModel):
    states: List[str]
    alphabet: List[str]
    tape_symbols: List[str]
    transitions: Dict[str, Dict[str, tuple]]
    initial_state: str
    blank_symbol: str
    final_states: List[str]

class TestStringSchema(BaseModel):
    string: str
