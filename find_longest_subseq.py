"""
The Challenge 
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.
Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.
Note: D can appear in any format (list, hash table, prefix tree, etc.
For example,
given the input of S = "abppplee" and
D ={"able", "ale", "apple", "bale", "kangaroo"}
the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter
than "apple".

The word "bale" is not a subsequence of S because even though S has all
the right letters, they are not in the right order.

The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
"""
def get_nextW(index, D):
    return D[index]

def lookup_ch_pos(start_pos, ch, S):
    pos = start_pos
    while pos < len(S):
        if ch == S[pos]:
            print pos, ch, S
            return pos
        else:
            pos += 1
    return None
    
def find_longest_subseq(S, D):
    matched_W_len_max = matched_W_len = 0
    i_len_max = None
    for i in range(len(D)):
        W = get_nextW(i,D)
        nextpos = 0
        matched_W_len = 0
        print W
        for j in range(len(W)):
            pos = lookup_ch_pos(nextpos, W[j], S)
            if pos >= 0:
                nextpos = pos
                matched_W_len += 1
            else:
                break
            print j, nextpos, matched_W_len, W[j], S
        if j == matched_W_len -1:
            if matched_W_len > matched_W_len_max:
                matched_W_len_max = matched_W_len
                i_len_max = i                
    return i_len_max

if __name__ == '__main__':
    longS = "abppplee"
    mD = ["able", "ale", "apple", "bale", "kangaroo"]

    longest_subseq = find_longest_subseq(longS, mD)
    print mD[longest_subseq]
    
