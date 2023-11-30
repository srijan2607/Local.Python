Num1=int(input("Enter the number you want the table for : "))
Num2=int(input("enter the limit of your table "))

for i in range(1,Num2 + 1):
    Table = i * Num1
    print(i, "x", Num1,"=", Table)