#!/bin/python

# remove !"#$%&'()*+,-./:;?@[\]^_`{|}~ puctuation marks from a string, where
# puctuation marks are characters listed above, as defined in C locale.

def remove_punctuation(s):
    punctuation_marks = "!\"#$%&\'()*+,-./:;?@[\]^_`{|}~ \\"

    rs = ""
    for c in s:
        if c not in punctuation_marks:
            rs +=c

    return rs

if __name__ == "__main__":
    test_str = "%welcome\' to @geeksforgeek<s"
    ans_str = remove_punctuation(test_str)
    print ans_str
