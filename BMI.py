we = float(input("Input your weight (in kg): "))
hi = float(input("Input your height ( in cm): "))

def BMI_count(we,hi):
    BMI=float(0)
    hi=hi/100
    hi=hi*hi
    BMI=we/hi
    print( "Your BMI is ", BMI)
    if BMI<=18.49:
        print("You are underweight")
    elif BMI>=18.5 and BMI<=24.99:
        print("Your weight is within normal")
    else:
        print("You are overweight")

BMI_count(we, hi)