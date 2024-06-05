num1 = (input ("Informe um número: "))
num2 = (input ("Informe outro número: "))
num3 = (input ("Informe mais um número "))

if num1 < num2:
    num1, num2 = num2, num1

if num1 < num3:
    num1, num3 = num3, num1

if num2 < num3:
    num2, num3 = num3, num2

print (f"Em ordem descrescente, os números são {num1, num2, num3}")