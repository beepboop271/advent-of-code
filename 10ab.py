from functools import reduce
p = {"(": ")", "[": "]", "{": "}", "<": ">"}
sc = {")": 3, "]": 57, "}": 1197, ">": 25137}
sc2 = {")": 1, "]": 2, "}": 3, ">": 4}
def score(x):
    st = []
    for c in x:
        if c in p:
            st.append(p[c])
        elif st.pop() != c:
            return sc[c]
    return 0
def score2(x):
    st = []
    for c in x:
        if c in p:
            st.append(p[c])
        elif st.pop() != c:
            return -1
    return reduce(lambda b, c: b*5+sc2[c], reversed(st), 0)
def p1(x):
    return sum(map(score, x.split()))
def p2(x):
    l = sorted(filter(lambda x: x > -1, map(score2, x.split())))
    return l[len(l)//2]
