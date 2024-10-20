def calc1(num1, num2):
    sum1 = num1 + num2
    diff1 = num1 - num2
    prd1 = num1 * num2
    div1 = num1 / num2
    div2 = num1 // num2
    rem1 = num1 % num2
    exp1 = num1 ** num2
    
    print(f"Sum: {sum1}")
    print(f"Difference: {diff1}")
    print(f"Product: {prd1}")
    print(f"Division (float): {div1}")
    print(f"Division (int): {div2}")
    print(f"Remainder: {rem1}")
    print(f"Exponentiation: {exp1}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
calc1(num1, num2)

