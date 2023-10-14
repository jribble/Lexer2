from .fsa import FSA

class IdFSA(FSA):
    def __init__(self) -> None:
        FSA.__init__(self, "ID")
        self.accept_states.add(self.S1)
        self.accept_states.add(self.S2)
        self.keywords = {'Schemes', 'Facts', 'Rules', 'Queries'}

    def S0(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if str.isalpha(current_input) :
            self.num_chars_consumed += 1
            next_state = self.S1
        else:
            next_state = self.S_err
        return next_state

    def S1(self):
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if str.isalnum(current_input) :
            self.num_chars_consumed += 1
            next_state = self.S1
            # if the consumed input currently matches a keyword
            # swtich to a state that is not an accept state
            if self.get_consumed_input() in self.keywords:
                next_state = self.S_reserved
        else:
            next_state = self.S2
            # if the consumed input currently matches a keyword
            # that won't change, so go to S_err
            if self.get_consumed_input() in self.keywords:
                next_state = self.S_err
        return next_state
    
    def S_reserved(self):
        # this needs to do the exact same thing as S1, it just shouldn't be
        # considered an accept state, so just call S1
        return self.S1()
    
    def S2(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S2 #loop in accept
        return next_state
    
    def S_err(self):
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S_err #loop in error
        return next_state

