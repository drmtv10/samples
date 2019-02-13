#!/usr/bin/python

import sys
import string

def reverse_vowels(word_str):
    """ in-place reverse vowels in a word
    input: word
    output: word where vowels are reversed
    """
    low = 0 # start of word
    vVowels = "aAeEiIoOuU"
    high = len(word_str)-1 # end of word
    while (low < high):
        #print low, high, word_str[low], word_str[high]
        while word_str[low] not in vVowels:
            #print low, high, word_str[low], word_str[high]
            if (low < high):
                low += 1
            else:
                break
        while word_str[high] not in vVowels:
            #print low, high, word_str[low], word_str[high]
            if (low < high):
                high -= 1
            else:
                break
        # swap word_str[low] vowel with word_str[high]
        # what to do if vowels interchanged here are the same?? (TBD)
        #print low, high, word_str[low], word_str[high]
        temp_ch = word_str[high]
        word_str[high] = word_str[low]
        word_str[low] = temp_ch
        low += 1
        high -= 1

def main():
    word_b4 = ['Deepak', 'Khurshid', 'Apple', 'Oracle']
    for i in range(len(word_b4)):
        word_aft = list(word_b4[i])
        reverse_vowels(word_aft)
        rvw = "".join(word_aft)
        #print word_b4[i], word_aft, rvw
        print word_b4[i], rvw

if __name__ == "__main__":
   main()

