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

        #FSA manager dictionary
        # self.fsa_keys: list[function] = [self.colon_dash_fsa, self.colon_fsa, self.left_paren_fsa, self.right_paren_fsa, self.comma_fsa, self.period_fsa, 
        #                                  self.q_mark_fsa, self.multiply_fsa, self.add_fsa, self.comment_fsa, 
        #                                  self.schemes_fsa, self.facts_fsa, self.rules_fsa]
        self.fsa_keys: list[function] = [self.colon_dash_fsa, self.colon_fsa]
        self.colon_or_dash_keys: list[function] = [self.colon_dash_fsa, self.colon_fsa]
        self.fsa_dict: dict[Token, bool] = dict.fromkeys(self.fsa_keys, False)
        self.colon_or_dash_dict: dict[Token, bool] = dict.fromkeys(self.colon_or_dash_keys, False)

    
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
                        tokens.append("UNDEFINED", string, line_num)
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

        output_string = output_string + "\n" + "Total Tokens = " + str(len(tokens))
        return output_string
    
    def lex(self, input_string: str) -> list[(str,str)]:
        tokens: str = []
        cur_input: str = input_string
        while len(cur_input) > 0:
            best_chars_consumed: int = 0
            best_fsa: FSA = None
            for fsa in self.fsa_dict.keys():
                if fsa.run(cur_input):
                    num_chars_consumed: int = fsa.get_num_chars_consumed()
                    if num_chars_consumed > best_chars_consumed:
                        best_chars_consumed = num_chars_consumed
                        best_fsa = fsa
            if best_fsa != None:
                token_input: str = ""
                if best_chars_consumed > 0:
                    token_input = cur_input[:best_chars_consumed]
                tokens.append((best_fsa.get_name(), token_input))
            else:
                best_chars_consumed = 1
            cur_input = cur_input[best_chars_consumed:]
            self.reset()
        return tokens
        # return self.__manager_fsm__()

    def __manager_fsm__(self) -> list[str]:
        output_token: str = "UNDEFINED"
        output_tokens: list[str] = []
        # output_list: list[bool] = [value for value in self.fsa_dict.values()]
        colon_dash_output_list: list[bool] = [value for value in self.colon_or_dash_dict.values()]
        if self.fsa_dict[self.comment_fsa]:
            output_token = "COMMENT"
            output_tokens.append(output_token)

        else:
            # if self.fsa_dict[self.string_fsa]:
            #     output_token = "STRING"
            #     output_tokens.append(output_token)
            if True == False:
                print('idek man')
            
            else:

                if colon_dash_output_list == [True, True]:
                    output_token = "COLON_DASH"
                    output_tokens.append(output_token)
                elif colon_dash_output_list == [False, True]:
                    output_token = "COLON"
                    output_tokens.append(output_token)

                # for fsa in self.fsa_dict.values():
                #     print(fsa)


                if self.fsa_dict[self.left_paren_fsa]: 
                    output_token = "LEFT_PAREN"
                    output_tokens.append(output_token)

                if self.fsa_dict[self.right_paren_fsa]:
                    output_token = "RIGHT_PAREN"
                    output_tokens.append(output_token)

                if self.fsa_dict[self.comma_fsa]:
                    output_token = "COMMA"
                    output_tokens.append(output_token)

                if self.fsa_dict[self.period_fsa]:
                    output_token = "PERIOD"
                    output_tokens.append(output_token)

                if self.fsa_dict[self.q_mark_fsa]:
                    output_token = "Q_MARK"
                    output_tokens.append(output_token)

                if self.fsa_dict[self.multiply_fsa]:
                    output_token = "MULTIPLY"
                    output_tokens.append(output_token)

                if self.fsa_dict[self.add_fsa]:
                    output_token = "ADD"
                    output_tokens.append(output_token)

                # strings get some different considerations
                
                if self.fsa_dict[self.schemes_fsa]:
                    output_token = "SCHEMES"
                    output_tokens.append(output_token)

                # FIXME: why are these always returning true?
                if self.fsa_dict[self.facts_fsa]:
                    print(self.fsa_dict[self.facts_fsa])
                    output_token = "FACTS"
                    output_tokens.append(output_token)

                if self.fsa_dict[self.rules_fsa]:
                    print(self.fsa_dict[self.rules_fsa])
                    output_token = "RULES"
                    output_tokens.append(output_token)
            

        for output in output_tokens: print(output)

        # elif output_list[3] == True: output_token = "PERIOD"
        return output_tokens

    def reset(self) -> None:
        for FSA in self.fsa_dict.keys() : FSA.reset()