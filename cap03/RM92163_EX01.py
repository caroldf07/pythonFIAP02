opcao = -1
alimentos = []
calorias = []

while opcao != 3:
    print("======= HealthTrack =======\n")
    print("1 - Incluir alimento")
    print("2 - Total de calorias ingeridas hoje")
    print("3- Sair")
    opcao = int(input("\nInforme a sua opção: "))
    print("======= HealthTrack =======\n")

    if opcao == 1:
        alimentos.append(input("Digite o nome do alimento: "))
        calorias.append(
            int(input("Digite o valor das calorias do alimento informado: ")))
    elif opcao == 2:
        total_alimentos = len(alimentos)
        total_ingerido = sum(calorias)
        print(f"Os alimentos ingeridos de hoje foram: ")
        for alimento in alimentos:
            print(alimento)
        print(f"Você ingeriu {total_alimentos} alimentos.")
        print(f"O total de calorias ingerido é: {total_ingerido}\n")

print("========================")
print("\nEncerrando o HealthTrack\n")
print("========================")
