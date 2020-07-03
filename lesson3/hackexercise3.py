import itertools
def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r


def crack(s):
    ans = simple_hash(s)
    s2 = itertools.product([i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'],repeat=8)
    for i in s2:
        if simple_hash(i)==ans and i!=s:
            return i
    return ""# return s2 such that s != s2 and simple_hash(s) == simple_hash(s2)
    
  """
  Brute-force the hash function you've just written!

Implement a function crack that given a string s, loops until it finds a different string that collides with it, and returns the different string."""
