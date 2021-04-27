from math import*


def calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Error. Cannot divide by zero."
            return result
    elif operator == "*":
        result = num1 * num2
    else:
        result = "An error has occurred, closing program."
    if result - floor(result) == 0:
        result = int(result)
        return result
    else:
        return result


is_valid = False
operators = "+-/*"

while not is_valid:
    num1 = (input("Enter first number: "))
    operator = input("Enter operator: ")
    num2 = (input("Enter second number: "))

    num1_digit_test = num1.replace(".", "0")
    num2_digit_test = num2.replace(".", "0")

    if num1_digit_test.isdigit() and num2_digit_test.isdigit() and (operator in operators) and len(operator) == 1:

        is_valid = True

        num1 = float(num1)
        num2 = float(num2)

        final_result = (calculator(num1, num2, operator))

        if final_result == "Error. Cannot divide by zero.":
            print(final_result)
            is_valid = False
        else:
            print(final_result)

    else:
        print("Invalid Number or Operator has been chosen please try again")