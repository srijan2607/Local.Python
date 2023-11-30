num1= int(input("Enter the Number : "))

factorial = 1

if num1 < 0:
    print("Are you stupid factorial is not possiable :-/ ")

elif num1 == 0:
    print("Are you stupid factorial is not possiable :-/")

elif num1 > 0:
    for i in range (1, num1 + 1):
        factorial *= i
print("Factorial = ", factorial)