from filaArq import Fila

estacionamento = Fila()


def menuEstacionamento():
    while True:
        entrada = str(
            input("Selecione uma opção:\n[1] Adicionar Carro\n[2] Remover Carro\n[3] Ver Carros\n[4] Sair\n "))
        if entrada == "1":
            placa = str(input("Digite a placa do carro: "))
            estacionamento.inserirPlaca(placa)

        elif entrada == "2":
            placa = str(input("Digite a placa do carro: "))
            estacionamento.mudarOrdem(placa)

        elif entrada == "3":
            estacionamento.mostrarCarros()

        elif entrada != "4":
            print("Digite uma opção válida!\n")

        else:
            print("Obrigado por utilizar o estacionamento!")
            return False


def main():
    print("Bem vindo ao estacionamento!\n")
    menuEstacionamento()


main()
