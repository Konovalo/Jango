def my_var():
    nt = int(42)
    tr = str(42)
    st2 = "quarante-deux"
    at = float(42)
    ol = True
    st = [42]
    ct = {42: 42}
    le = (42,)
    et = set()
    print(nt, "has a type", type(nt))
    print(tr, "has a type", type(tr))
    print(st2, "has a type", type(st2))
    print(at, "has a type", type(at))
    print(ol, "has a type", type(ol))
    print(st, "has a type", type(st))
    print(ct, "has a type", type(ct))
    print(le, "has a type", type(le))
    print(et, "has a type", type(et))

if __name__ == '__main__':
    my_var()
    
