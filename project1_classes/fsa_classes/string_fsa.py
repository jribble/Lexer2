from .fsa import FSA

class StringFSA(FSA):
    def __init__(self) -> None:
        FSA.__init__(self, "STRING")
        self.accept_states.add(self.S2)
        self.accept_states.add(self.S3)

    def S0(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == '\'' :
            self.num_chars_consumed += 1
            next_state = self.S1
        else:
            next_state = self.S_err
        return next_state
    
    def S1(self):
        current_input: str = self._FSA__get_current_input()
        print(current_input)
        if current_input == '\'' :
            self.num_chars_consumed += 1
            next_state = self.S2
        else:
            self.num_chars_consumed += 1
            next_state: function = self.S1 #loop in s1
        return next_state
    
    def S2(self):
        current_input: str = self._FSA__get_current_input()
        if current_input == '\'' :
            # it's a double ', so we are still in the string
            self.num_chars_consumed += 1
            next_state = self.S1
        else:
            # it's not a double ', so string was over last state
            next_state: function = self.S3 #loop in accept
        return next_state
    
    def S3(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S3 #loop in accept
        return next_state
    
    def S_err(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S_err #loop in error
        return next_state

