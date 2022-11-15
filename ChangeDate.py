import re
def UserEntry():
    user=input("Enter your string: ")
    return user
def ChangeDate(x):
    res=re.sub(r'([0-9]{4})-([0-9]{2})-([0-9]{2})',r'\3-\2-\1',x)
    return res
print(ChangeDate(UserEntry()))