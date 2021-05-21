import re
from typing import NamedTuple, Iterable

class Token(NamedTuple):
    kind: str
    value: str

def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """

    code = code.split(";;", 1)[0]
    
    for token in re.finditer(createRegex(), code):
        kind = token.lastgroup
        value = token.group()
        if kind != "MISMATCH":
            yield Token(kind, value)

def createRegex():
    token_specification = [
        ("STRING", r"\".*\""),
        ("CHAR", r"#\\[\w]+"),
        ('NUMBER', r'[-+]?\d+(\.\d*)?'),
        ("NAME", r"[-+_\w\d\<\>\?\!\%\=\*\/\.]+"),  
        ("BOOL", r"#([fF]|[tT])"),
        ('COMMA', r','),               
        ("QUOTE", r"[\'\"]"),
        ("LPAR", r"\("), 
        ("RPAR", r"\)"), 
        ('MISMATCH', r'.'),            
    ]
    regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    return regex