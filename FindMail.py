import re
def UserEntry():
    user=input("Enter your string: ")
    return user
def FindEmail(x):
    result = re.findall("[a-zA-Z0-9]*@[a-zA-Z0-9]*[.][a-zA-Z]{2,3}",x)
    return result
print(FindEmail(UserEntry()))