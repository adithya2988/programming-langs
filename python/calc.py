num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
op = input("enter the operation: ")
match op:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
        