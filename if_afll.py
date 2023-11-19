import ply.yacc as yacc
import ply.lex as lex


# Define the tokens
tokens = (
    'LBRACE',
    'RBRACE',
    'IDENTIFIER',
    'SEMICOLON',
    'IF',
    'RPARA',
    'LPARA',
    'GREATER',
    'LESSER',
    'EQUAL',
    'NUMERIC',
    'PRINT',
    'QUOTE',
    'STRING',
)


# Define token regular expressions
t_ignore = ' \t'

def t_IF(t):
    r'if'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_PRINT(t):
    r'printf'
    return t

def t_QUOTE(t):
    r'\"'
    return t


t_SEMICOLON = r'\;'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACE=r'\{'
t_RBRACE=r'\}'
t_LPARA=r'\('
t_RPARA=r'\)'
t_GREATER=r'\>'
t_LESSER=r'\<'
t_EQUAL=r'\='
t_NUMERIC=r'[0-9_]'
# Error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)


# Parsing rules
def p_declaration(p):
    '''declaration : IF LPARA condition RPARA LBRACE RBRACE '''
    p[0] = f'if {p[3]}:\n{p[6]}'


def p_condition(p):
    '''condition : IDENTIFIER GREATER IDENTIFIER
                 | IDENTIFIER LESSER IDENTIFIER
                 | IDENTIFIER EQUAL EQUAL IDENTIFIER
                 '''
    p[0] = f'if {p[1]} {p[2]} {p[3]}:'

def p_condition_NUM(p):
    '''condition : IDENTIFIER GREATER NUMERIC
                 | NUMERIC GREATER NUMERIC
                 | IDENTIFIER LESSER NUMERIC
                 | NUMERIC LESSER NUMERIC'''
    p[0] = f'if {p[1]} {p[2]} {p[3]}:'



def p_empty(p):
    'empty :'
    pass


# Error rule for syntax errors
def p_error(p):
    print("Invalid statement.")


# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()


# Get user input
input_text = input("Enter an if statement: ")
# input_text ="if(x>y){}"

lexer.input(input_text)
for token in lexer:
      print(token)
parser.parse(input_text)




result = parser.parse(input_text, lexer=lexer)
if result:
    print("code generated")
    print("valid statement")
else:
    print("invalid statement")
