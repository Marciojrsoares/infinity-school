n1 = input ("Digite um numero: ")
n2 = input ("Digite outro numero: ")
n3 = input ("Digite mais um numero: ")

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

menor = n1

if n2 < n1 and n2 < n3:
    maior = n2

if n3 < n1 and n3 < n2:
    menor = n3

print(f"O maior número digitado foi {maior}")
print(f"O menor número digitado foi {menor}")