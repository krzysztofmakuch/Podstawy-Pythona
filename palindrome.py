word=input("Check if this word is a palindrome: ")
def Check_Palindrome(a):
    return a==a[::-1]
print(Check_Palindrome(word))
