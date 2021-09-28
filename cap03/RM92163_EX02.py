opcao = -1
transacoes = []
gastos = []

while opcao != 3:
    print("======= FinançaKids =======\n")
    print("1 - Incluir gasto")
    print("2 - Total gasto hoje")
    print("3- Sair")
    opcao = int(input("\nInforme a sua opção: "))
    print("======= FinançaKids =======\n")

    if opcao == 1:
        transacoes.append(input("Digite o nome da transação: "))
        gastos.append(
            int(input("Digite o valor das transação informada: ")))
    elif opcao == 2:
        total_transacao = len(transacoes)
        total_gasto = sum(gastos)
        print(f"As transações de hoje foram: ")
        for transacao in transacoes:
            print(transacao)
        print(f"Você realizou {total_transacao} transações hoje.")
        print(f"O total gasto foi: {total_gasto}\n")

print("========================")
print("\nFinançaKids\n")
print("========================")
