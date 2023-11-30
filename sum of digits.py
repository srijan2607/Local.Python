while True :
    num =  int(input("Enter the Number : "))

    digits = 0

    while num > 0:
        sum = num % 10 
        digits += sum
        num //= 10

    print("Answer = ", digits)