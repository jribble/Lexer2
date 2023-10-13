from project1_classes import token
from project1_classes.fsa_classes    import colon_dash_fsa, colon_fsa, left_paren_fsa, right_paren_fsa
from project1_classes.fsa_classes.comma_fsa import CommaFSA
from project1_classes.fsa_classes.fsa import FSA
from project1_classes.lexer_fsm import LexerFSM


my_lexer: LexerFSM = LexerFSM()
fsaTest: FSA = CommaFSA()
input_string: str = """
'hi''s' .
rules
facts
"""
my_lexer.reset()
points = my_lexer.run(input_string)#fsaTest.run(',')

print(points)

# for point in points :
#     if isinstance(point, token.Token):
#         print(point.to_string())

# input_string = ":-"
# my_lexer.reset()
# print("On input",input_string, "The lexer output ",my_lexer.lex(input_string))

# input_string = "("
# my_lexer.reset()
# print("On input",input_string, "The lexer output ",my_lexer.lex(input_string))

# input_string = ")"
# my_lexer.reset()
# print("On input",input_string, "The lexer output ",my_lexer.lex(input_string))

# input_string = "(:-:)"
# my_lexer.reset()
# print("On input",input_string, "The lexer output ",my_lexer.lex(input_string))