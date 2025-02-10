from graphviz import Digraph

def gerar_grafico_afd(automato):
    """Gera um gráfico para um Autômato Finito Determinístico (DFA)."""
    dot = Digraph(comment='Autômato Finito')

    # Adiciona os estados
    for estado in automato.dfa.states:
        shape = 'doublecircle' if estado in automato.dfa.final_states else 'circle'
        dot.node(estado, estado, shape=shape)

    # Adiciona as transições
    for estado, transicoes in automato.dfa.transitions.items():
        for simbolo, destino in transicoes.items():
            dot.edge(estado, destino, label=simbolo)

    # Gera o arquivo em PNG
    arquivo = "dfa_automaton"
    dot.render(arquivo, format='png', cleanup=True)
    return f"{arquivo}.png"

def gerar_grafico_pda(automato):
    """Gera um gráfico para um Autômato com Pilha (PDA)."""
    dot = Digraph(comment='Autômato com Pilha')

    # Adiciona os estados
    for estado in automato.dpda.states:
        shape = 'doublecircle' if estado in automato.dpda.final_states else 'circle'
        dot.node(estado, estado, shape=shape)

    # Adiciona as transições
    for estado, transicoes in automato.dpda.transitions.items():
        for simbolo, regras in transicoes.items():
            for pilha_topo, (destino, push) in regras.items():
                label = f"{simbolo}, {pilha_topo} → {', '.join(push) if push else 'ε'}"
                dot.edge(estado, destino, label=label)

    # Gera o arquivo em PNG
    arquivo = "pda_automaton"
    dot.render(arquivo, format='png', cleanup=True)
    return f"{arquivo}.png"

def gerar_grafico_turing(automato):
    """Gera um gráfico para uma Máquina de Turing."""
    dot = Digraph(comment='Máquina de Turing')

    # Adiciona os estados
    for estado in automato.dtm.states:
        shape = 'doublecircle' if estado in automato.dtm.final_states else 'circle'
        dot.node(estado, estado, shape=shape)

    # Adiciona as transições
    for estado, transicoes in automato.dtm.transitions.items():
        for simbolo, (destino, escreve, move) in transicoes.items():
            label = f"{simbolo} → {escreve}, {move}"
            dot.edge(estado, destino, label=label)

    # Gera o arquivo em PNG
    arquivo = "turing_machine"
    dot.render(arquivo, format='png', cleanup=True)
    return f"{arquivo}.png"
