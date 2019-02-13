#!/bin/python
# match parenthesis in given string

def match_paren(in_str):
    paren = list()
    for x in in_str:
        if x == '(' or x == '[':
            paren.append(x)
        elif x == ')':
            y = paren.pop()
            if y != '(':
                return False
        elif x == ']':
            y = paren.pop()
            if y != '[':
                return False
    if len(paren) == 0:
        return True
    else:
        return False
    
def do_match_print(input_string):
    if match_paren(input_string):
        print input_string, 'ok'
    else:
        print input_string, 'failed matching paren'
    

if __name__ == '__main__':
    input_strings = ['( This is [ invalid',
                     'Another ()[] valid (string)',
                     '([1 2 3]]==',
                     '(value)'
                     ]
    for pstring in input_strings:
        do_match_print(pstring)
    
            
                
