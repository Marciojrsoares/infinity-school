# verificar se um número é positivo, negativo ou zero
# solicitar ao usuário que insira um número e, em seguida, imprimir uma mensagem indicando a natureza do número.
# Se o número for maior que zero, exiba a mensagem "O número é positivo.
# " Se for menor que zero, exiba "O número é negativo." Caso seja zero, a mensagem deve ser "O número é zero."
# estruturas condicionais e formatação com F-string

num1 = (int(input ("Informe um número: "))) # coleta o número

if num1 > 0:
    print (f"O número é positivo.") # indica a natureza positiva do número

elif num1 < 0:
    print (f"O númeor é negativo.") # indica a natureza negativa do número

else:
    print (f"O número é zero.") # indica a natureza neutra do número