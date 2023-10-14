from project1_classes.fsa_classes.add_fsa import AddFSA
from project1_classes.fsa_classes.colon_dash_fsa import ColonDashFSA
from project1_classes.fsa_classes.colon_fsa import ColonFSA
from project1_classes.fsa_classes.comma_fsa import CommaFSA
from project1_classes.fsa_classes.comment_fsa import CommentFSA
from project1_classes.fsa_classes.facts_fsa import FactsFSA
from project1_classes.fsa_classes.id_fsa import IdFSA
from project1_classes.fsa_classes.left_paren_fsa import LeftParenFSA
from project1_classes.fsa_classes.multiply_fsa import MultiplyFSA
from project1_classes.fsa_classes.period_fsa import PeriodFSA
from project1_classes.fsa_classes.q_mark_fsa import QMarkFSA
from project1_classes.fsa_classes.queries_fsa import QueriesFSA
from project1_classes.fsa_classes.right_paren_fsa import RightParenFSA
from project1_classes.fsa_classes.rules_fsa import RulesFSA
from project1_classes.fsa_classes.schemes_fsa import SchemesFSA
from project1_classes.fsa_classes.string_fsa import StringFSA
from project1_classes.fsa_classes.undefined_fsa import UndefinedFSA
from project1_classes.fsa_classes.whitespace_fsa import WhitespaceFSA
from .fsa_classes.fsa import FSA
from .token import Token
from typing import Callable as function

class LexerFSM:
    def __init__(self):
        self.tokens: list[Token] = []

        #needed FSA's
        self.add_fsa: AddFSA = AddFSA()
        self.colon_dash_fsa: ColonDashFSA = ColonDashFSA()
        self.colon_fsa: ColonFSA = ColonFSA()
        self.comma_fsa: CommaFSA = CommaFSA()
        self.comment_fsa: CommentFSA = CommentFSA()
        self.facts_fsa: FactsFSA = FactsFSA()
        self.id_fsa: IdFSA = IdFSA()
        self.left_paren_fsa: LeftParenFSA = LeftParenFSA()
        self.multiply_fsa: MultiplyFSA = MultiplyFSA()
        self.period_fsa: PeriodFSA = PeriodFSA()
        self.q_mark_fsa: QMarkFSA = QMarkFSA()
        self.queries_fsa: QueriesFSA = QueriesFSA()
        self.right_paren_fsa: RightParenFSA = RightParenFSA()
        self.rules_fsa: RulesFSA = RulesFSA()
        self.schemes_fsa: SchemesFSA = SchemesFSA()
        self.string_fsa: StringFSA = StringFSA()
        self.undefined_fsa: UndefinedFSA = UndefinedFSA()
        self.whitespace_fsa: WhitespaceFSA = WhitespaceFSA()

        #FSA manager dictionary
        self.fsas: list[function] = [
            self.add_fsa,
            self.colon_dash_fsa,
            self.colon_fsa,
            self.comma_fsa,
            self.comment_fsa,
            self.facts_fsa,
            self.id_fsa,
            self.left_paren_fsa,
            self.multiply_fsa,
            self.period_fsa,
            self.q_mark_fsa,
            self.queries_fsa,
            self.right_paren_fsa,
            self.rules_fsa,
            self.schemes_fsa,
            self.string_fsa,
            self.whitespace_fsa,
            self.undefined_fsa
        ]

    
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
                    if token_tuple[0] != 'WHITESPACE':
                        tokens.append(Token(token_tuple[0], token_tuple[1], line_num))
        
        EOF.set_line(line_num)
        tokens.append(EOF)
            
        error_line: int = -1
        token: Token
        for token in tokens :
            output_string = output_string + token.to_string() + "\n"
            if token.get_type() == 'UNDEFINED':
                error_line = token.get_line()
                break

        if error_line >= 0:
            output_string = output_string + "\nTotal Tokens = Error on line " + str(error_line) + "\n"
        else:
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