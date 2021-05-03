class Fila:
    def __init__(self):
        self.dados = []

    def inserirPlaca(self, novoValor):
        self.dados.append(novoValor)
        print()

    def mudarOrdem(self, valor):
        pos = self.dados.index(valor)
        for i in range(0, pos + 1):
            self.inserirPlaca(self.dados[0])
            self.dados.pop(0)
        self.dados.pop()
        print(f"O carro de placas '{valor}' foi removido.")

    def mostrarCarros(self):
        print("\nOs carros se encontram nessa ordem:")
        for i in self.dados:
            print(f"{self.dados.index(i) + 1} - Placas {[i]}")
        print()
