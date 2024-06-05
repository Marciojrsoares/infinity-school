L1 = (input ("Informe o preço da laranja: R$ "))
M1 = (input ("Informe o preço da maça: R$ "))
G1 = (input ("Informe o preço da goiaba: R$ "))

L2 = "Laranja"
M2 = "Maça"
G2 = "Goiaba"

menor = L1
produto = L2

if M1 < G1 and M1 < L1:
    menor = M1
    produto = M2

if G1 < L1 and G1 < M1:
    menor = G1
    produto = G2

print (f"O produto escolhido é a {produto} pois o valor é R$ {menor}")