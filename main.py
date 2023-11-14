#ask for a number
x=int(input("Please tell me a number:"))
#discuss the range of the number
if x>=1000:
    if x<=9999:
        if x%2==0:
            if x%10==0:
                print("It is bad because it ends with a 0.")
            else:
                print("Thank you, it is good.")
        else:
            print("It is bad because it is an odd.")
    else:
        print("it is bad because it is too big.")
else:
    print("it is bad because it is too small.")

quit()
