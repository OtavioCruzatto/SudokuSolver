class Linha:

    def __init__(self, linha: list[int]) -> None:
        self.__linha = linha
        self.__posicao_dos_zeros: list[int] = []
        self.__soma_dos_elementos: int = 0
        self.__quantidade_de_zeros: int = 0

        self.__posicao_dos_zeros = self.get_posicao_dos_zeros()
        self.__soma_dos_elementos = self.get_soma_dos_elementos()
        self.__quantidade_de_zeros = self.get_quantidade_de_zeros()

    def contem(self, numero: int) -> bool:
        return (numero in self.__linha)

    def get_linha(self) -> list[int]:
        return self.__linha

    def get_soma_dos_elementos(self) -> int:
        self.__soma_dos_elementos = 0
        for numero in self.__linha:
            self.__soma_dos_elementos += numero
        return self.__soma_dos_elementos

    def get_posicao_dos_zeros(self) -> list[int]:
        self.__posicao_dos_zeros.clear()
        for posicao, numero in enumerate(self.__linha):
            if (numero == 0):
                self.__posicao_dos_zeros.append(posicao)
        return self.__posicao_dos_zeros

    def get_quantidade_de_zeros(self) -> int:
        self.__quantidade_de_zeros = 0
        for numero in self.__linha:
            if (numero == 0):
                self.__quantidade_de_zeros += 1
        return self.__quantidade_de_zeros