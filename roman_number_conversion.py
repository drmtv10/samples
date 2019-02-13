#!/bin/python

from collections import OrderedDict

# convert integers to roman numerals
class roman_number0:
    '''
    This is very brute force draft of
    conversion implementation.  Needs further
    modulerization / break up
    '''
    def __init__(self, x=int(0)):
        self.value = ''
        while x >= 1000:
            self.value += 'M'
            x -= 1000
        if x >= 900:
            self.value += 'CM'
            x -= 900
        if x >= 500:
            self.value += 'D'
            x -= 500
        if x >= 400:
            self.value += 'CD'
            x -= 400
        while x >= 100:
            self.value += 'C'
            x -= 100
        if x >= 90:
            self.value += 'XC'
            x -= 90
        if x >= 50:
            self.value += 'L'
            x -= 50
        if x >= 40:
            self.value += 'XL'
            x -= 40
        while x >= 10:
            self.value += 'X'
            x -= 10
        if x >= 9:
            self.value += 'IX'
            x -= 9
        if x >= 5:
            self.value += 'V'
            x -= 5
        if x >= 4:
            self.value += 'IV'
            x -= 4
        while x >= 1:
            self.value += 'I'
            x -= 1
            
class roman_number:
    """
    Using OrderedDict from collections class is *NECESSARY* here.
    Otherwise, iterator returns items in an order that is un-expected and
    conersion fails.  Using another data structure, such as two separate
    lists, may work, too.
    """
    conv_roman_map = OrderedDict( [(1000,'M'), (900,'CM'), (500,'D'), (400,'CD'),
                                   (100,'C'), (90,'XC'), (50,'L'), (40,'XL'),
                                   (10,'X'), (9,'IX'), (5,'V'), (4,'IV'),
                                   (1,'I') ] )
    
    def __init__(self, x=int(0)):
        self.value = ''
        for k, v in self.conv_roman_map.items():
            while x >= int(k):
                self.value += v
                x -= int(k)

        
def print_roman_value(num):
    rv = roman_number(num)
    print num, '=', rv.value

if __name__ == '__main__':
    for i in [1, 44, 2018, 575, 2001]:
        print_roman_value(i)
