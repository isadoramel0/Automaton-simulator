from automata.tm.dtm import DTM

class TuringMachine:
    def __init__(self, states, alphabet, tape_symbols, transitions, initial_state, blank_symbol, final_states):
        self.dtm = DTM(
            states=set(states),
            input_symbols=set(alphabet),
            tape_symbols=set(tape_symbols),
            transitions=transitions,
            initial_state=initial_state,
            blank_symbol=blank_symbol,
            final_states=set(final_states)
        )

    def accepts(self, string: str) -> bool:
        return self.dtm.accepts_input(string)

    def get_info(self):
        return {
            "states": list(self.dtm.states),
            "alphabet": list(self.dtm.input_symbols),
            "tape_symbols": list(self.dtm.tape_symbols),
            "transitions": self.dtm.transitions,
            "initial_state": self.dtm.initial_state,
            "blank_symbol": self.dtm.blank_symbol,
            "final_states": list(self.dtm.final_states)
        }
