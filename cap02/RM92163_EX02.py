assinatura = input("Informe qual o tipo de assinatura do cliente: ")

faturamento = float(
    input("Informe o faturamento anual do cliente em formato monetário (0.00): "))

assinaturaTratada = assinatura.lower()

bonus = 0.0

if assinaturaTratada == "basic":
    bonus = faturamento * 0.3
    print("O bônus a ser recebido é: R$ {}".format(round(bonus, 2)))
elif assinaturaTratada == "silver":
    bonus = faturamento * 0.2
    print("O bônus a ser recebido é: R$ {}".format(round(bonus, 2)))
elif assinaturaTratada == "gold":
    bonus = faturamento * 0.1
    print("O bônus a ser recebido é: R$ {}".format(round(bonus, 2)))
elif assinaturaTratada == "platinum":
    bonus = faturamento * 0.05
    print("O bônus a ser recebido é: R$ {}".format(round(bonus, 2)))
else:
    print("O plano informado não existe ou foi digitado errado")
