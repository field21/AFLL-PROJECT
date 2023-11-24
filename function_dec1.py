import ply.yacc as yacc
import ply.lex as lex


# Define the tokens
tokens = (
    'TYPE',
    'POINTER',
    'IDENTIFIER',
    'SEMICOLON',
    'LBRACE',
    'RBRACE',
    'COMMA',
)


# Define token regular expressions
t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_TYPE(t):
    r'int|char|float|double|void'
    return t


t_POINTER = r'\*'
t_SEMICOLON = r';'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACE=r'\('
t_RBRACE=r'\)'

# Error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)


# Parsing rules
def p_declaration(p):
    '''declaration : TYPE IDENTIFIER LBRACE type RBRACE SEMICOLON'''
    p[0] = f"valid declaration of the function: {p[1]}{p[2]} {p[3]};"


def p_type(p):
    '''type: TYPE IDENTIFIER
            | TYPE IDENTIFIER COMMA'''




def p_empty(p):
    'empty :'
    pass


# Error rule for syntax errors
def p_error(p):
    print("Invalid Declaration.")


# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()


# Get user input
input_text = input("Enter a function declaration: ")


lexer.input(input_text)
for token in lexer:
      print(token)
parser.parse(input_text)




result = parser.parse(input_text, lexer=lexer)
if result:
    print("code generated")
    print("valid declaration")
else:
    print("invalid declaration")

