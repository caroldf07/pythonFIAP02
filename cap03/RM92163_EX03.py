numero = int(input("Digite o seu número: "))

ultimo = 1
penultimo = 1
termo = 0

if(numero == 1) or (numero == 2):
    print("Ação bem sucedida!")
else:
    while termo < numero:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo

    if(termo == numero):
        print("Ação bem sucedida!")
    else:
        print("A ação falhou...")
