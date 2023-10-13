from project1_classes.fsa_classes.add_fsa import AddFSA
from project1_classes.fsa_classes.comma_fsa import CommaFSA
from project1_classes.fsa_classes.colon_fsa import ColonFSA
from project1_classes.fsa_classes.comment_fsa import CommentFSA
from project1_classes.fsa_classes.facts_fsa import FactsFSA
from project1_classes.fsa_classes.left_paren_fsa import LeftParenFSA
from project1_classes.fsa_classes.multiply_fsa import MultiplyFSA
from project1_classes.fsa_classes.period_fsa import PeriodFSA
from project1_classes.fsa_classes.q_mark_fsa import QMarkFSA
from project1_classes.fsa_classes.right_paren_fsa import RightParenFSA
from project1_classes.fsa_classes.rules_fsa import RulesFSA
from project1_classes.fsa_classes.schemes_fsa import SchemesFSA
from project1_classes.fsa_classes.string_fsa import StringFSA
from project1_classes.fsa_classes.whitespace_fsa import WhitespaceFSA
from .fsa_classes.fsa import FSA
from .fsa_classes.colon_dash_fsa import ColonDashFSA
from .token import Token
from typing import Callable as function

class LexerFSM:
    def __init__(self):
        self.tokens: list[Token] = []

        #needed FSA's
        self.colon_dash_fsa: ColonDashFSA = ColonDashFSA()
        self.colon_fsa: ColonFSA = ColonFSA()
        self.left_paren_fsa: LeftParenFSA = LeftParenFSA()
        self.right_paren_fsa: RightParenFSA = RightParenFSA()
        self.comma_fsa: CommaFSA = CommaFSA() 
        self.period_fsa: PeriodFSA = PeriodFSA()
        self.q_mark_fsa: QMarkFSA = QMarkFSA()
        self.multiply_fsa: MultiplyFSA = MultiplyFSA()
        self.add_fsa: AddFSA = AddFSA()
        self.comment_fsa: CommentFSA = CommentFSA()
        self.schemes_fsa: SchemesFSA = SchemesFSA()
        self.facts_fsa: FactsFSA = FactsFSA()
        self.rules_fsa: RulesFSA = RulesFSA()
        self.string_fsa: StringFSA = StringFSA()
        self.whitespace_fsa: WhitespaceFSA = WhitespaceFSA()

        #FSA manager dictionary
        self.fsas: list[function] = [self.colon_dash_fsa, self.colon_fsa, self.left_paren_fsa, self.right_paren_fsa, self.comma_fsa, self.period_fsa, 
                                         self.q_mark_fsa, self.multiply_fsa, self.add_fsa, self.comment_fsa, 
                                         self.schemes_fsa, self.facts_fsa, self.rules_fsa, self.string_fsa, self.whitespace_fsa]

    
    def run(self, input: str) -> str:
        line_num: int  = 1
        output_string: str = ""
        EOF: Token = Token("EOF", "", 0)
        tokens: list[Token] = []
        new_strings: list[str] = input.split('\n')
        if len(new_strings) > 0 :
            for index, string in enumerate(new_strings) :
                print(string)
                line_num = index + 1
                        
                token_tuples: list[str] = self.lex(string)
                for token_tuple in token_tuples:
                    # token: Token = Token(token_type, string, line_num)
                    if (string == "") :
                        continue

                    if (token_tuple[0] == "UNDEFINED") :
                        tokens.append(("UNDEFINED", string, line_num))
                        for object in tokens :
                            if isinstance(object, Token): 
                                output_string = output_string + object.to_string() + "\n"
                        print("Total Tokens = Error on line " +  str(line_num))
                        exit()

                    tokens.append(Token(token_tuple[0], token_tuple[1], line_num))
                    # print(token)
        
        EOF.set_line(line_num)
        tokens.append(EOF)
            
        for object in tokens :
            if isinstance(object, Token): 
                output_string = output_string + object.to_string() + "\n"

        output_string = output_string + "Total Tokens = " + str(len(tokens)) + "\n"
        return output_string
    
    def lex(self, input_string: str) -> list[(str,str)]:
        tokens: str = []
        cur_input: str = input_string
        while len(cur_input) > 0:
            best_fsa: FSA = None
            for fsa in self.fsas:
                if fsa.run(cur_input):
                    best_fsa = FSA.better(best_fsa, fsa)
            if best_fsa != None:
                tokens.append((best_fsa.get_name(), best_fsa.get_consumed_input()))
                cur_input = best_fsa.get_remaining_input()
            else:
                tokens.append(("UNDEFINED", cur_input))
                cur_input = ""
            self.reset()
        return tokens

    def reset(self) -> None:
        for FSA in self.fsas : FSA.reset()