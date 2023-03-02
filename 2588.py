firstNumber = int(input())
secondNumber = int(input())

print(firstNumber * (secondNumber % 10))
print(firstNumber*(int(secondNumber % 100 / 10)))
print(firstNumber*(int(secondNumber / 100)))
print(firstNumber*secondNumber)
