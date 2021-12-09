from functools import reduce

bruh = (
    lambda x: (
        lambda l: reduce(
            lambda b, c: (c, b[1]+(c>b[0])),
            l,
            (next(l), 0)
        )
    )(map(int, x.split()))[1]
)

lambda x:(lambda l:reduce(lambda b,c:(c,b[1]+(c>b[0])),l,(next(l),0)))(map(int,x.split()))[1]

bruh2 = (
    lambda x: (
        lambda f, *r: sum(f<(f:=n)for n in r)
    )(*map(int, x.split()))
)

lambda x:(lambda f,*r:sum(f<(f:=n)for n in r))(*map(int,x.split()))
