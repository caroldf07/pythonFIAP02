segunda = int(input("Informe quantos votos o dia de segunda-feira teve: "))
terca = int(input("Informe quantos votos o dia de terça-feira teve: "))
quarta = int(input("Informe quantos votos o dia de quarta-feira teve: "))
quinta = int(input("Informe quantos votos o dia de quinta-feira teve: "))
sexta = int(input("Informe quantos votos o dia de sexta-feira teve: "))

if segunda > terca > quarta > quinta > sexta:
    print("O dia vencedor é: segunda-feira com {} votos".format(segunda))
elif terca > segunda > quarta > quinta > sexta:
    print("O dia vencedor é: terça-feira com {} votos".format(terca))
elif quarta > segunda > terca > quinta > sexta:
    print("O dia vencedor é: quarta-feira com {} votos".format(quarta))
elif quinta > segunda > quarta > terca > sexta:
    print("O dia vencedor é: quinta-feira com {} votos".format(quinta))
else:
    print("O dia vencedor é: sexta-feira com {} votos".format(sexta))
