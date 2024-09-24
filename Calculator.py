NumberOne = int(input("Enter number : "))
Operation = input("Select Operation (+,-,*,/) : ")
NumberTwo = int(input("Enter number : "))

if Operation == "+":
    Add_total = NumberOne + NumberTwo
    print(Add_total)

elif Operation == "-":
    Sub_total = NumberOne - NumberTwo
    print(Sub_total)

elif Operation == "*":
    Mul_total = NumberTwo * NumberOne
    print(Mul_total)

elif Operation == "/":
    Div_total = NumberOne / NumberTwo
    print(Div_total)
    