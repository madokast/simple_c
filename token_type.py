"""
定义 Token 类型
IDENTIFIER[ID]
EOF[EOF]
KeyWords:
  ELSE[else], FOR[for], FUNC[func], IF[if], RETURN[return], VAR[var]
Punctuations:
  BRACE_L[{], BRACE_R[}], COMMA[,], PAREN_L[(], PAREN_R[)], SEMICOLON[;]
Operators:
  ADD[+], ASSIGN[=], ASTER[*], DIV[/], EQ[==], GT[>], GTE[>=], LT[<], LTE[<=], NEQ[!=], NOT[!], SUB[-]
Literals:
  CHAR[char-literal], FLOAT[float-literal], INT[int-literal], STRING[str-literal]
"""

class TokenType:
    def __init__(self, name:str) -> None:
        self.name = name
    def __str__(self) -> str:
        return self.name
    def __repr__(self) -> str:
        return self.name

IDENTIFIER = TokenType('ID')
EOF = TokenType('EOF')

class KeyWords:
    VAR = TokenType('var')
    FUNC = TokenType('func')
    IF = TokenType('if')
    ELSE = TokenType('else')
    FOR = TokenType('for')
    RETURN = TokenType('return')

class Punctuations:
    COMMA = TokenType(',')
    SEMICOLON = TokenType(';')
    PAREN_L = TokenType('(')
    PAREN_R = TokenType(')')
    BRACE_L = TokenType('{')
    BRACE_R = TokenType('}')

class Operators:
    ASSIGN = TokenType('=')
    ADD = TokenType('+')
    SUB = TokenType('-')
    ASTER = TokenType('*')
    DIV = TokenType('/')
    NOT = TokenType('!')
    EQ = TokenType('==')
    NEQ = TokenType('!=')
    LT = TokenType('<') # less than
    LTE = TokenType('<=')
    GT = TokenType('>')
    GTE = TokenType('>=')

class Literals:
    INT = TokenType('int-literal')
    FLOAT = TokenType('float-literal')
    STRING = TokenType('str-literal')
    CHAR = TokenType('char-literal')

if __name__ == '__main__':
    def member_visit(cls):
        print(cls.__name__, ':\n', '  ', end='', sep='')
        print(*[f"{member}[{getattr(cls, member)}]" for member in sorted(dir(cls)) if member[0] != '_'], sep=', ')

    print('定义 Token 类型')
    print(f"IDENTIFIER[{IDENTIFIER.name}]")
    print(f"EOF[{EOF.name}]")
    member_visit(KeyWords)
    member_visit(Punctuations)
    member_visit(Operators)
    member_visit(Literals)
