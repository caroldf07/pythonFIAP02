peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / altura**2

if float(imc) < 16.00:
    print("Seu IMC é {} e está: Baixo peso Grau III".format(round(imc, 2)))
elif float(imc) >= 16.00 and float(imc) < 16.99:
    print("Seu IMC é {} e está: Baixo peso Grau II".format(round(imc, 2)))
elif float(imc) >= 17.00 and float(imc) < 18.49:
    print("Seu IMC é {} e está: Baixo peso Grau I".format(round(imc, 2)))
elif float(imc) >= 18.50 and float(imc) < 24.99:
    print("Seu IMC é {} e está: Peso ideal".format(round(imc, 2)))
elif float(imc) >= 25.00 and float(imc) < 29.99:
    print("Seu IMC é {} e está: Sobrepeso".format(round(imc, 2)))
elif float(imc) >= 30.00 and float(imc) < 34.99:
    print("Seu IMC é {} e está: Obesidade Grau I".format(round(imc, 2)))
elif float(imc) >= 35.00 and float(imc) < 39.99:
    print("Seu IMC é {} e está: Obesidade Grau II".format(round(imc, 2)))
else:
    print("Seu IMC é {} e está: Obesidade Grau III".format(round(imc, 2)))
