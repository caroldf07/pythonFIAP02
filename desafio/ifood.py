# Nome do restaurante, note e distância
dados = input(
    "Deseja colocar restaurantes manualmente(M) ou ver um exemplo (E)? ").lower()


def orderByNota(nota):
    return nota[1]


def orderByDistancia(distancia):
    return distancia[2]


if(dados == "e"):

    restaurantes = [["O Mineiro", 4.2, 1.7], ["Amor aos Pedaços", 4.3, 1.2], ["We Coffe", 4.5, 0.8],
                    ["Lamen Kazu - Liberdade", 4.8, 0.7], ["Mr Pretzel", 4.7, 1.1], ["Brigaderia Shopping Paulista", 4.7, 1.2]]

    restaurantes.sort(key=orderByDistancia)
    restaurantes.sort(key=orderByNota, reverse=True)
    print(restaurantes)
else:
    restaurantes_novos = []
    proximo = "sim"
    while(proximo == "sim"):

        nome = input("Digite o nome do restaurante: ")
        nota = float(input("Digite a nota do restaurante (de 1.0 a 5.0): "))
        while(nota < 1.0 or nota > 5.0):
            nota = float(
                input("Valor de nota inválido, por favor, tente novamente: "))
        distancia = float(input("Digite a distancia do restaurante: "))
        while(distancia < 0):
            distancia = float(
                input("Valor de distancia inválido, por favor, tente novamente: "))
        novo = [nome, nota, distancia]
        restaurantes_novos.append(novo)
        proximo = input(
            "Se deseja incluir mais restaurante digite 'sim' ").lower()

    restaurantes_novos.sort(key=orderByDistancia)
    restaurantes_novos.sort(key=orderByNota, reverse=True)
    print(restaurantes_novos)
