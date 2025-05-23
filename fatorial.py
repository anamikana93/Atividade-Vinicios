def calcular_fatorial(numero):
    if numero < 0:
        return None
    return 1 if numero == 0 else numero * calcular_fatorial(numero - 1)

while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("Digite um número positivo.")
        else:
            break
    except ValueError:
        print("Entrada inválida, digite um número inteiro.")

fatorial = calcular_fatorial(numero)
if fatorial is not None:
    print(f"O fatorial de {numero} é {fatorial}")
else:
    print("Não é possível calcular o fatorial de números negativos.")