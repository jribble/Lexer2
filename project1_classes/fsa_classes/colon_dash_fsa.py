from .fsa import FSA
from typing import Callable as function

class ColonDashFSA(FSA):
    def __init__(self) -> None:
        FSA.__init__(self, "COLONDASH")
        """Class constructor"""
        self.accept_states.add(self.S2)

        self.input_string: str = ""
        self.num_chars_read: int = 0
        #don't need a history, but for initial learning purposes
        self.history: list[str] = []

    
    def S0(self) -> function:
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == ':':
            self.num_chars_consumed += 1
            next_state = self.S1
        else:
            next_state = self.S_err
        return next_state
    
    def S1(self) -> function:
        current_input = self._FSA__get_current_input()
        next_state: function = None
        if current_input == '-':
            self.num_chars_consumed += 1
            next_state = self.S2
        else:
            next_state = self.S_err
        return next_state
    
    def S2(self) -> function:
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S2 #loop in accept
        return next_state
    
    def S_err(self) -> function:
        current_input: str = self._FSA__get_current_input()
        next_state: function = self.S_err #loop in error
        return next_state
    
    #Manager functions
    # def run(self, input_string: str) -> bool:
    #     self.input_string = input_string
    #     current_state: function = self.start_state
    #     while self.num_chars_read < len(self.input_string):
    #         current_state = current_state()
    #     outcome: bool = False
    #     if current_state in self.accept_states: outcome = True
    #     return outcome
    
    # def reset(self):
    #     self.num_chars_read = 0
    #     self.history = []

    # #getters and setters
    # def get_name(self) -> str: return self.fsa_name
    # #history probably not needed
    # def get_history(self) -> str:
    #     output_string: str = ""
    #     for message in self.history:
    #         output_string = output_string + message + "\n"
    #     return output_string
    
    # def get_history_string(sefl, current_state: function, input: str, next_state: function) :
    #     history_message: str = "From state " + current_state + " read input " + input + " and transitioned to state " + next_state
    #     return history_message
    
    # #private helper
    # def __get_current_input(self) -> str:
    #     current_input: str = self.input_string[self.num_chars_read]
    #     self.num_chars_read += 1
    #     return current_input