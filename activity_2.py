a=int((input("enter a number to find its cube: ")))
def cube():
    print(a*a*a)
def div_3():
    if (a%3==0):
       return cube()
    else:
        print("it is not divisible by 3")

div_3()