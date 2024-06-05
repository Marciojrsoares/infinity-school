# Prova algoritmos e variáveis - aula1
# O programa deve solicitar ao usuário que forneça a base e a altura do retângulo. 
# Em seguida, o programa deve calcular a área usando a fórmula: Área=Base×Altura


# Pedir ao usuário que insira a base e altura do retângulo
base = float(input("Por favor, digite a medida (ex 3.11) da base do retângulo: "))
retangulo = float(input("Agora, digite a medida (ex 3.11) da altura do retângulo: "))

# Calculo da área do retângulo
area = round(base * retangulo, 2)

# Se a senha estiver correta, imprimir mensagem de login bem-sucedido
print(f"A área do retângulo é igual a {area} m2")
