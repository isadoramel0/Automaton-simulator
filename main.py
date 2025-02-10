from fastapi import FastAPI
from routes import finite_routes, pushdown_routes, turing_routes

app = FastAPI()


app.include_router(finite_routes.router, prefix="/finite-automaton", tags=["Finite Automaton"])
app.include_router(pushdown_routes.router, prefix="/pushdown-automaton", tags=["Pushdown Automaton"])
app.include_router(turing_routes.router, prefix="/turing-machine", tags=["Turing Machine"])
