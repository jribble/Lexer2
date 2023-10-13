from .fsa import FSA

class WhitespaceFSA(FSA):
    def __init__(self) -> None:
        FSA.__init__(self, "WHITESPACE")
        self.accept_states.add(self.S1)
        self.accept_states.add(self.S2)

    def S0(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if str.isspace(current_input) :
            self.num_chars_consumed += 1
            next_state = self.S1
        else:
            next_state = self.S_err
        return next_state
    
    def S1(self):
        current_input: str = self._FSA__get_current_input()
        if str.isspace(current_input) :
            self.num_chars_consumed += 1
            next_state = self.S1
        else:
            next_state: function = self.S2 #loop in s1
        return next_state
    
    def S2(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S2 #loop in accept
        return next_state
    
    def S_err(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S_err #loop in error
        return next_state

