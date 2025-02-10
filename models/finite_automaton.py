from automata.fa.dfa import DFA

class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.dfa = DFA(
            states=set(states),
            input_symbols=set(alphabet),
            transitions=transitions,
            initial_state=initial_state,
            final_states=set(final_states)
        )

    def accepts(self, string: str) -> bool:
        return self.dfa.accepts_input(string)

    def get_info(self):
        return {
            "states": list(self.dfa.states),
            "alphabet": list(self.dfa.input_symbols),
            "transitions": self.dfa.transitions,
            "initial_state": self.dfa.initial_state,
            "final_states": list(self.dfa.final_states)
        }
