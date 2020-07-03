def simple_hash(s):
    r = 7
    for i in s:
        r = ((r*31)+ord(i))%(1<<16)
    return r
