n = []
for i in range(5):
    n.append(int(input(f"Informe o {i+1}º numero: ")))

maior_valor = n[0]
menor_valor = n[0]
for valor in n:
    if valor > maior_valor:
        maior_valor = valor 
    if valor < menor_valor:
        menor_valor = valor

print("O maior valor é: ", maior_valor)
print("O menor valor é: ", menor_valor)