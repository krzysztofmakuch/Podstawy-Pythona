import re
def UserEntry():
    user=input("Enter your string: ")
    user1=re.split(", ",user)
    return user1
def SameLetter(x):
    result=[]
    for a in x:
        r=re.split("\s",a)
        r1=re.findall("^.",r[0])
        r2=re.findall("^.",r[1])
        if r1==r2:
            result.append(a)
    return result
print(SameLetter(UserEntry()))