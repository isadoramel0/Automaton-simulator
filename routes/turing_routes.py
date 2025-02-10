from fastapi import APIRouter, HTTPException
from models.turing_machine import TuringMachine
from schemas.automaton_schema import TuringMachineSchema, TestStringSchema
from fastapi.responses import FileResponse
from models.graph_generator import gerar_grafico_turing

router = APIRouter()

automata_storage = {}

@router.post("/")
def create_turing_machine(data: TuringMachineSchema):
    """Cria uma nova Máquina de Turing."""
    try:
        machine = TuringMachine(
            states=data.states,
            alphabet=data.alphabet,
            tape_symbols=data.tape_symbols,
            transitions=data.transitions,
            initial_state=data.initial_state,
            blank_symbol=data.blank_symbol,
            final_states=data.final_states
        )
        automata_storage["turing"] = machine
        return {"message": "Máquina de Turing criada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def get_turing_machine():
    """Recupera informações da Máquina de Turing armazenada."""
    if "turing" not in automata_storage:
        raise HTTPException(status_code=404, detail="Nenhuma Máquina de Turing foi criada ainda.")
    
    machine = automata_storage["turing"]
    return machine.get_info()

@router.post("/test")
def test_string(data: TestStringSchema):
    """Testa se uma string é aceita pela Máquina de Turing."""
    if "turing" not in automata_storage:
        raise HTTPException(status_code=404, detail="Nenhuma Máquina de Turing foi criada ainda.")
    
    machine = automata_storage["turing"]
    result = machine.accepts(data.string)
    return {"string": data.string, "accepted": result}

@router.get("/graph")
def get_turing_graph():
    """Gera e retorna um gráfico da Máquina de Turing."""
    if "turing" not in automata_storage:
        raise HTTPException(status_code=404, detail="Nenhuma Máquina de Turing foi criada ainda.")

    arquivo = gerar_grafico_turing(automata_storage["turing"])
    return FileResponse(arquivo, media_type="image/png")
