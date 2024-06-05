# Prova algoritmos e variáveis - aula1
# O programa deve solicitar ao usuário que forneça a base e a altura do retângulo. 
# Em seguida, o programa deve calcular a área usando a fórmula: Área=Base×Altura

# Pedir ao usuário que insira a base e altura do retângulo
while True:
    try:
        base = float(input("Digite o número da base: ").replace(",", ".")) # Substituindo a vírgula por ponto para garantir que o número seja interpretado corretamente.

        break # Se a conversão for bem-sucedida, sai do loop.

    except ValueError:
        print("Por favor, digite um número válido. Utilize apenas números e um ponto para separar os decimais.") # Entrar com dado válido.

while True:
    try:
        altura = float(input("Digite o número da altura: ").replace(",", ".")) # Substituindo a vírgula por ponto para garantir que o número seja interpretado corretamente.

        break # Se a conversão for bem-sucedida, sai do loop.

    except ValueError:
        print("Por favor, digite um número válido. Utilize apenas números e um ponto para separar os decimais.") # Entrar com dado válido.

area = round(base * altura, 2) # Calculo da área do retângulo com arredondamento em duas casas decimais

print(f"A área do retângulo é igual a {area} m2") # Resultado da formula para o usuário em metros quadrados