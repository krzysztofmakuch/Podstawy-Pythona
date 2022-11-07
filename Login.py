def UpperCase(nbname):
    b=0
    fname=""
    for let in nbname:
        if let!=' ':
            b=b+1
        if let.isupper():
            fname=fname+let
    fname=fname+str(b)
    return fname

def NoUpperCase(bname):
    a=0
    b=0
    fname=""
    if bname[a]!=' ':
        fname=fname+bname[a]
        b=b+1
    a=a+1
    c=len(bname)-1
    while a<=c:
        if bname[a]==' ' and bname[a+1]!=' ':
            fname=fname+bname[a+1]
        elif(bname[a]!=' '):
            b=b+1
        a=a+1
    fname=fname+str(b)
    fname=fname.upper()
    return fname

def Create_Login():
    rname=str(input("first and last name: "))
    if any(let.isupper() for let in rname):
        print(UpperCase(rname))
    else:
        print(NoUpperCase(rname))

Create_Login()
