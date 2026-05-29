# Calculator 

Num1 = int(input("Num1:"))

Operand = (input("What is your operand (-,+,*,/):"))

Num2 = int(input("Num2:"))

def Add(Num1,Num2):
    return(Num1 + Num2)

def Sub(Num1,Num2):
    return(Num1 - Num2)

def multi(Num1,Num2):
    return(Num1 * Num2)

def div(Num1,Num2):
    return(Num1 / Num2)

if Operand == "+":
    print(f"Your answer is {Add(Num1,Num2)}")

elif Operand == "-":
    print(f"Your Ans is {Sub(Num1,Num2)}")

elif Operand == "*":
    print(f"Your Ans is {multi(Num1,Num2)}")

elif Operand == "/":
    print(f"Your answer is {div(Num1,Num2)}")

else :
    print("Error")