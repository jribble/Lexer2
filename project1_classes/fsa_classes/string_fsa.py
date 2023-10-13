from .fsa import FSA

class StringFSA(FSA):
    def __init__(self) -> None:
        FSA.__init__(self, "StringFSA")
        self.accept_states.add(self.S2)

    def S0(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == '\'' :
            next_state = self.S1
        else:
            next_state = self.S_err
        return next_state
    
    def S1(self):
        current_input: str = self._FSA__get_current_input()
        print(current_input)
        if current_input == '\'' :
            print('\' seen')
            next_state = self.S2
            print('should be going to s2 now')
        else:
            next_state: function = self.S1 #loop in s1
        return next_state
    
    def S2(self):
        current_input: str = self._FSA__get_current_input()
        print ('in s2')
        if current_input == '\'' :
            next_state = self.S1
        else:
            next_state: function = self.S2 #loop in accept
        return next_state
    
    def S_err(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S_err #loop in error
        return next_state

