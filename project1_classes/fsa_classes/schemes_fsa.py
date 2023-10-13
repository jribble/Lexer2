from .fsa import FSA

class SchemesFSA(FSA):
    def __init__(self) -> None:
        FSA.__init__(self, "SCHEMES")
        self.accept_states.add(self.S7)

    def S0(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == 's' or current_input == 'S' :
            self.num_chars_consumed += 1
            next_state = self.S1
        else:
            next_state = self.S_err
        return next_state
    
    def S1(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == 'c' or current_input == 'C' :
            self.num_chars_consumed += 1
            next_state = self.S2
        else:
            next_state = self.S_err
        return next_state
    
    def S2(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == 'h' or current_input == 'H' :
            self.num_chars_consumed += 1
            next_state = self.S3
        else:
            next_state = self.S_err
        return next_state
    
    def S3(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == 'e' or current_input == 'E' :
            self.num_chars_consumed += 1
            next_state = self.S4
        else:
            next_state = self.S_err
        return next_state
    
    def S4(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == 'm' or current_input == 'M' :
            self.num_chars_consumed += 1
            next_state = self.S5
        else:
            next_state = self.S_err
        return next_state
    
    def S5(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == 'e' or current_input == 'E' :
            self.num_chars_consumed += 1
            next_state = self.S6
        else:
            next_state = self.S_err
        return next_state
    
    def S6(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == 's' or current_input == 'S' :
            self.num_chars_consumed += 1
            next_state = self.S7
        else:
            next_state = self.S_err
        return next_state
    
    def S7(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S7 #loop in accept
        return next_state
    
    def S_err(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S_err #loop in error
        return next_state

