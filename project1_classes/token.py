class Token():
    def __init__(self, token_type: str, value: str, line_num: int):
        self.token_type = token_type
        self.value = value
        self.line = line_num

    def to_string(self) -> str:
        string = "(" + self.token_type + ",\"" + self.value +  "\"," + str(self.line) + ")"
        return string
    
    def set_type(self, type: str):
        self.token_type = type

    def get_type(self) -> str:
        return self.token_type

    def set_value(self, value: str):
        self.value = value

    def get_value(self) -> str:
        return self.value

    def set_line(self, line_num: int):
        self.line = line_num

    def get_line(self) -> int:
        return self.line