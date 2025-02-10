from fastapi import APIRouter, HTTPException
from models.pushdown_automaton import PushdownAutomaton
from schemas.automaton_schema import PushdownAutomatonSchema, TestStringSchema
from fastapi.responses import FileResponse
from models.graph_generator import gerar_grafico_pda

router = APIRouter()

automata_storage = {}

@router.post("/")
def create_automaton(data: PushdownAutomatonSchema):
    """Cria um novo autômato com pilha."""
    try:
        automaton = PushdownAutomaton(
            states=data.states,
            alphabet=data.alphabet,
            stack_symbols=data.stack_symbols,
            transitions=data.transitions,
            initial_state=data.initial_state,
            initial_stack_symbol=data.initial_stack_symbol,
            final_states=data.final_states
        )
        automata_storage["pushdown"] = automaton
        return {"message": "Autômato com pilha criado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def get_automaton():
    """Recupera informações do autômato armazenado."""
    if "pushdown" not in automata_storage:
        raise HTTPException(status_code=404, detail="Nenhum autômato com pilha foi criado ainda.")
    
    automaton = automata_storage["pushdown"]
    return automaton.get_info()

@router.post("/test")
def test_string(data: TestStringSchema):
    """Testa se uma string é aceita pelo autômato."""
    if "pushdown" not in automata_storage:
        raise HTTPException(status_code=404, detail="Nenhum autômato com pilha foi criado ainda.")
    
    automaton = automata_storage["pushdown"]
    result = automaton.accepts(data.string)
    return {"string": data.string, "accepted": result}

@router.get("/graph")
def get_pda_graph():
    """Gera e retorna um gráfico do Autômato com Pilha."""
    if "pushdown" not in automata_storage:
        raise HTTPException(status_code=404, detail="Nenhum autômato com pilha foi criado ainda.")

    arquivo = gerar_grafico_pda(automata_storage["pushdown"])
    return FileResponse(arquivo, media_type="image/png")