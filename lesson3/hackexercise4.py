import hashlib
import itertools

def weak_md5(s):
    return hashlib.md5(s).digest()[:5]


def find_collisions():
    arr = itertools.product('wsgj53',repeat=4)
    res = {}
    for i in arr:
        i = "".join(i)
        ans = weak_md5(i)
        if ans in res.keys():
            return res[ans],i
        res[ans]=i
    return '',''# return (s1, s2) such that s1 != s2 and weak_md5(s1) == weak_md5(s2)
