"""
Simple Calculator
"""
# Provide your solution here
def calculate (x: int, y: int, i: str):
    if y == 0:
        print("Division by 0 is not allowed")
    elif i == "+":
        return x + y
    elif i == "-":
       return x - y
    elif i == "*":
       return x * y
    elif i == "/":
       return x / y
    else:
        print("Invalid operator")
"""
Reverse Word
"""
# Provide your solution here
def reverse_word(word:str = "hello"):
    index = 1
    while index < len(word) + 1:
        print(word[len(word)-index], end="")
        index += 1

    result = str(reverse_word())
    print(result.capitalize())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(reverse_word("hello")) # "Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

