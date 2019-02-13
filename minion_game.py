
def minion_game(string):
    # your code goes here
    Vowels = 'AEIOU'
    Consonants = 'BCDFGHJKLMNPQRSTVWXYZ'

    vo = 0
    co = 0
    known_substr = []
    for w in range(1, len(string)+1):
        for p in range(len(string)+1-w):
            substr = string[p:p+w]
            print 'w=', w, substr
            if substr in known_substr:
                continue
            if substr[0] in Vowels:
                vo += string.count(substr)
                print 'sub=', substr, 'vo=', vo
            if substr[0] in Consonants:
                co += string.count(substr)
                print 'sub=', substr, 'co=', co
            known_substr.append(substr)
            
    if vo == co:
        print 'Draw'
    elif co > vo:
        print 'Stuart', co
    else :
        print 'Kevin', vo

def minion_game_answer(s):
"""The logic is simple - take all possible substrings, split them into two sets according to starting letter, then sum elements in sets. 

All possible substrings are string of lenght 1, then strings of length 2 etc. i above is an iterator for that lenght. 

And then comes a little optimization - if you know the starting letter, you can add all substrings of different length that start with this letter. It will be len(s) - i
"""
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print "Kevin", kevsc
    elif kevsc < stusc:
        print "Stuart", stusc
    else:
        print "Draw"    

def minion_game_tryagain(game_s):
    vowels = 'aeiou'.uppercase()

    set s=[][]
    for w in range(1, len(game_s)+1):
        s[w] = game_s.split(w0

if __name__ == '__main__':
    s = raw_input()
    #minion_game(s)
    minion_game_solution(s)
    
