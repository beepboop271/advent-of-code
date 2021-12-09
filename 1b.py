bruh = (
    lambda x: (
        lambda a,b,c,*r: sum(0+(a+b+c<(a:=b)+(b:=c)+(c:=n)) for n in r)
    )(*map(int, x.split()))
)

lambda x:(lambda a,b,c,*r:sum(0+(a+b+c<(a:=b)+(b:=c)+(c:=n))for n in r))(*map(int,x.split()))

from itertools import tee

def g(x):
    l = map(int, x.split())
    a, b, c = tee(l, 3)
    next(b); next(c); next(c)
    s = map(sum, zip(a, b, c))
    return (lambda f,*r:sum(0+(f<(f:=n))for n in r))(next(s), *s)

def f(x):
    l = list(map(int, x.split()))
    s = map(sum, zip(l, l[1:], l[2:]))
    return (lambda f,*r:sum(0+(f<(f:=n))for n in r))(next(s), *s)
