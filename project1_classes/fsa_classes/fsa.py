from typing import Callable as function

class FSA:
    def __init__(self, name: str) -> None:
        self.start_state: function = self.S0
        self.accept_states: set[function] = set()

        self.input_string: str = ''
        self.fsa_name: str = name
        self.num_chars_read: int = 0
    
    def S0(self) -> function:
        raise NotImplementedError()
    
    def run(self, input_string: str) -> bool:
        self.input_string = input_string
        current_state: function = self.start_state

        while self.num_chars_read < len(self.input_string) :
            current_state = current_state()
        outcome: bool = False
        if current_state in self.accept_states:
            outcome = True
        return outcome

    def reset(self) -> None:
        self.num_chars_read = 0

    def get_name(self) -> str: 
        return self.fsa_name

    def set_name(self, FSA_name) -> None:
        self.fsa_name = FSA_name

    def __get_current_input(self) -> str:  # The double underscore makes the method private
        current_input: str = self.input_string[self.num_chars_read]
        self.num_chars_read += 1
        return current_input