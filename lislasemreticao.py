lista1 = input("Digite os numeros da lista 1, separados por espaço: ").split()
lista2 = input("Digite os numeros da lista 2, separados por espaço: ").split()

lista1 = [int(x) for x in lista1]
lista2 = [int(x) for x in lista2]

lista_uni = list(set(lista1 + lista2))

print("Lista unificada: ", *lista_uni)