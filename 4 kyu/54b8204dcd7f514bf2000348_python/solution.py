import re
from ast import literal_eval

class Simplexer(object):
    keywords = ["if", "else", "for", "while", "return", "func", "break"]
    pattern_expression = re.compile(fr"(\".+?\"|(?:{'|'.join(keywords)})|\d+|[a-z]\w*|[+/*()=-]|\s+|\d)", 
                                    flags=re.IGNORECASE)
    pattern_isstring = re.compile(r"^\"{1}[^\"]+\"{1}$")
    
    
    def __init__(self, expression):
        print(expression, type(expression))
        self.expression = expression
        self.expression_iter = self.pattern_expression.finditer(expression)
        
        
    def __iter__(self):
        return self
                
    def __next__(self):
        match = next(self.expression_iter)
        chars = match.group()
        
        if chars.isspace():
            token_type = "whitespace"
        
        elif chars.isdigit():
            token_type = "integer"
            
        elif chars in "+-*/%()=":
            token_type = "operator"
            
        elif chars in "truefalse":
            token_type = "boolean"
            
        elif chars in self.keywords:
            token_type = "keyword"
        
        elif self.pattern_isstring.search(chars):
            token_type = "string"
        
        elif chars.isidentifier():
            token_type = "identifier"
            
        else:
            raise ValueError(f"Unknown token value: {repr(chars)}")
        
        return Token(chars, token_type)
        
        