import re
def UserEntry():
    user=input("Enter your string: ")
    return user
def BigLetter(x):
    result=[]
    res=re.findall(r'([a-zA-Z0-9 ]{1,}\.)',x)
    for a in res:
        a=a.lower()
        if a[0]==" ":
            a=a[1].upper()+a[2:]
        else:
            a=a.capitalize()
        result.append(a)
    result=' '.join(result)
    return result
print(BigLetter(UserEntry()))