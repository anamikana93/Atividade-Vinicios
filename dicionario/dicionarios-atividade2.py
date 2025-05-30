estoque = {} 
qtnd_de_prod = int(input("Informe a quantidade de produtos que deseja cadastrar: "))  
for i in range(qtnd_de_prod):
    nome_prod = input("Informe o nome do produto: ")
    qtd_prod = int(input(f"Informe a quantidade do produto {nome_prod}: "))    
    estoque[nome_prod] = qtd_prod
print(estoque)

for produto, quantidade in estoque.items():
    print("Produto: ", produto, "|| Quantidade: ", quantidade)

busca = input("Informe o nome do produto que deseja pesquisar: ")
if busca in estoque:
    print(f"A quantidade do produto {busca} é {estoque[busca]} ")
else:
    print("O produto não está no estoque!")

estoque = {"Camiseta": 50, "Calça": 30}
while True:
    print("\nEstoque Atual:", estoque)
    op = input("Digite 'adicionar' para adicionar, 'remover' para remover, ou 'sair' para sair: ").lower()
    if op == 'sair':
        break
    produto = input("Qual produto você quer atualizar? ").capitalize()
    if produto in estoque:
        try:
            quantidade = int(input("Quantas unidades? "))
            if op == 'adicionar':
                estoque[produto] += quantidade  
                print(f"Você adicionou {quantidade} unidades de {produto}.")
            elif op == 'remover':
                if estoque[produto] >= quantidade:
                    estoque[produto] -= quantidade  
                    print(f"Você removeu {quantidade} unidades de {produto}.")
                else:
                    print(f"Não há unidades suficientes de {produto} para remover.")
            else:
                print("Operação inválida. Escolha 'adicionar' ou 'remover'.")
        except ValueError:
            print("Por favor, digite um número válido para a quantidade.")
    else:
        print(f"O produto '{produto}' não está no estoque.")
