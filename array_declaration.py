import ply.yacc as yacc
import ply.lex as lex


# Define the tokens
tokens = (
    'TYPE',
    'IDENTIFIER',
    'SEMICOLON',
    'LSQUARE',
    'RSQUARE',
    'NUM',
)


# Define token regular expressions
t_ignore = ' \t'


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)  # Convert the matched value to an integer
    return t


def t_TYPE(t):
    r'int|char'
    return t


t_LSQUARE=r'\['
t_RSQUARE=r'\]'
t_SEMICOLON = r';'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'


# Error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)


# Parsing rules
def p_declaration(p):
    '''declaration : TYPE IDENTIFIER LSQUARE NUM RSQUARE SEMICOLON '''
    p[0] = f"valid declaration: {p[1]}{p[2]} {p[3]};"





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
input_text = input("Enter an array declaration: ")
#input_text =f"int arr[{2}];"

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
