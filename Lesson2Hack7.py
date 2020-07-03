from collections import Counter

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    if not is_ascii(s):
        for i in s:
            if ord(i)>=128:
                s = s.replace(i,'')
    s=s.lower()
    for i in range(97):
        s = s.replace(chr(i),'')
    for i in range(123,129):
        s = s.replace(chr(i),'')
    frequency = {}
    for i in range(26):
        frequency[chr(i+ord('a'))]=0
    for i in s:
        frequency[i]+=1
    frequency = sorted(frequency.items(),key = lambda item:item[1])
    frequency.reverse()
    ans = ['e','t','a','o','i','n']
    return frequency[0][0] in ans and frequency[1][0] in ans and frequency[2][0] in ans
    
    """
    Implement heuristic plaintext detection using frequency analysis:

    Implement a function is_english that:

    Receives a string
    Makes sure it consists of only ASCII characters (using the provided is_ascii() function)
    Counts the 3 most frequent letters in it
    Makes sure they're one of the 6 most frequent letters in English (e, t, a, o, i, n)
    """
