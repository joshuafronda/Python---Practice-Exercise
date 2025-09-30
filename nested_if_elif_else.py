num = int(input("Enter value for num: "))
if num > 0:
    if num % 2 == 0:
        print("It is positive and even.")
    else:
        print("It is positive and odd.")
elif num < 0:
    print("It is negative.")
else:
    print("It is zero.")



