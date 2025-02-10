from fastapi import APIRouter, HTTPException
from models.finite_automaton import FiniteAutomaton
from schemas.automaton_schema import FiniteAutomatonSchema, TestStringSchema
from fastapi.responses import FileResponse
from models.graph_generator import gerar_grafico_afd

router = APIRouter()

automata_storage = {}

@router.get("/graph")
def get_automaton_graph():
    """Gera e retorna um gráfico do Autômato Finito."""
    if "finite" not in automata_storage:
        raise HTTPException(status_code=404, detail="Nenhum autômato foi criado ainda.")

    arquivo = gerar_grafico_afd(automata_storage["finite"])
    return FileResponse(arquivo, media_type="image/png")

@router.post("/")
def create_automaton(data: FiniteAutomatonSchema):
    """Cria um novo autômato finito."""
    try:
        automaton = FiniteAutomaton(
            states=data.states,
            alphabet=data.alphabet,
            transitions=data.transitions,
            initial_state=data.initial_state,
            final_states=data.final_states
        )
        automata_storage["finite"] = automaton
        return {"message": "Autômato criado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def get_automaton():
    """Recupera informações do autômato armazenado."""
    if "finite" not in automata_storage:
        raise HTTPException(status_code=404, detail="Nenhum autômato foi criado ainda.")
    
    automaton = automata_storage["finite"]
    return automaton.get_info()

@router.post("/test")
def test_string(data: TestStringSchema):
    """Testa se uma string é aceita pelo autômato."""
    if "finite" not in automata_storage:
        raise HTTPException(status_code=404, detail="Nenhum autômato foi criado ainda.")
    
    automaton = automata_storage["finite"]
    result = automaton.accepts(data.string)
    return {"string": data.string, "accepted": result}
