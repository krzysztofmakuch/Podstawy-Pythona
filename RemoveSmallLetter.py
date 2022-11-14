import re
def UserEntry():
    user=input("Enter your string: ")
    return user
def RemoveSmallLetter(x):
    result=re.sub("[a-z]","",x)
    return result
print(RemoveSmallLetter(UserEntry()))