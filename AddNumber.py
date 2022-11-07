def UserAdd():
    result=[]
    while True:
        x=input("Add your number: ")
        if x=='0':
            break
        try:
            int(x)
            result.append(x)
        except ValueError:
            print("%s is not a number"%(x))
    return(result)
print(UserAdd())