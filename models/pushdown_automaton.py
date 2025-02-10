from automata.pda.dpda import DPDA

class PushdownAutomaton:
    def __init__(self, states, alphabet, stack_symbols, transitions, initial_state, initial_stack_symbol, final_states):
        self.dpda = DPDA(
            states=set(states),
            input_symbols=set(alphabet),
            stack_symbols=set(stack_symbols),
            transitions=transitions,
            initial_state=initial_state,
            initial_stack_symbol=initial_stack_symbol,
            final_states=set(final_states),
            acceptance_mode="final_state"  # Pode ser "final_state" ou "empty_stack"
        )

    def accepts(self, string: str) -> bool:
        return self.dpda.accepts_input(string)

    def get_info(self):
        return {
            "states": list(self.dpda.states),
            "alphabet": list(self.dpda.input_symbols),
            "stack_symbols": list(self.dpda.stack_symbols),
            "transitions": self.dpda.transitions,
            "initial_state": self.dpda.initial_state,
            "initial_stack_symbol": self.dpda.initial_stack_symbol,
            "final_states": list(self.dpda.final_states),
            "acceptance_mode": self.dpda.acceptance_mode
        }
