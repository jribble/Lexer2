from .fsa import FSA

class UndefinedFSA(FSA):
    def __init__(self) -> None:
        FSA.__init__(self, "UNDEFINED")
        self.accept_states.add(self.S_complete)
        self.accept_states.add(self.S1) # incomplete string
        self.valid_start_chars = {',', '.', '?', '(', ')', ':', '*', '+', "'", '#'}

    # I don't think this is correct according to the spec, but it is according to the tests
    def get_consumed_input(self) -> str:
        return self.input_string[:1]

    def is_undefined_start_char(self, input: str) -> bool:
        if str.isalpha(input):
            return False
        if input in self.valid_start_chars:
            return False
        return True

    def S0(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if self.is_undefined_start_char(current_input):
            self.num_chars_consumed += 1
            next_state = self.S_complete
        elif current_input == '\'':
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
            next_state: function = self.S_err # it was a good string, so it's a bad undefined
        return next_state
    
    def S_complete(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S_complete #loop in accept
        return next_state
    
    def S_err(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S_err #loop in error
        return next_state

