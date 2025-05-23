n = int(input("Digite um numero inteiro positivo: "))

if n <= 0:
    print("Digite um numero inteiro positivo.")

else:
    fibonacci = [0, 1]
    for i in range(2, n):
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)
    
    print(f"Os {n} primeiros numeros da sequência de Fibonacci são: {fibonacci[:n]}")