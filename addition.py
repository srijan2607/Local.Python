total_sum=0
print("welcome to the programing world")
num1 = int(input("Enter your starting range for adition  " ))
num2 = int(input("Enter your ending range for adition  " ))
Type = input("You want addition of even or Odd or Natural Number  ")

if Type == "odd":
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            total_sum += i
elif Type == "even":
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            total_sum += i
elif Type == "natural":
    total_sum = sum(range(num1, num2 + 1))
else:
    print("Invalid input")

if Type in ["odd", "even", "natural"]:
    print("Total sum =", total_sum)
