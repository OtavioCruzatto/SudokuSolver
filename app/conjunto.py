class Conjunto:

    def __init__(self, conjunto: list[int]) -> None:
        self.__conjunto = conjunto
        self.__posicao_dos_zeros: list[int] = []
        self.__soma_dos_elementos: int = 0
        self.__quantidade_de_zeros: int = 0
        self.__valores_faltantes: list[int] = []

        self.__posicao_dos_zeros = self.get_posicao_dos_zeros()
        self.__soma_dos_elementos = self.get_soma_dos_elementos()
        self.__quantidade_de_zeros = self.get_quantidade_de_zeros()
        self.__valores_faltantes = self.get_valores_faltantes()

    def contem(self, numero: int) -> bool:
        return (numero in self.__conjunto)

    def get_conjunto(self) -> list[int]:
        return self.__conjunto

    def get_soma_dos_elementos(self) -> int:
        self.__soma_dos_elementos = 0
        for numero in self.__conjunto:
            self.__soma_dos_elementos += numero
        return self.__soma_dos_elementos

    def get_posicao_dos_zeros(self) -> list[int]:
        self.__posicao_dos_zeros.clear()
        for posicao, numero in enumerate(self.__conjunto):
            if (numero == 0):
                self.__posicao_dos_zeros.append(posicao)
        return self.__posicao_dos_zeros

    def get_quantidade_de_zeros(self) -> int:
        self.__quantidade_de_zeros = 0
        for numero in self.__conjunto:
            if (numero == 0):
                self.__quantidade_de_zeros += 1
        return self.__quantidade_de_zeros

    def get_valores_faltantes(self) -> list[int]:
        self.__valores_faltantes.clear()
        for numero in range(1, 10):
            if (numero not in self.__conjunto):
                self.__valores_faltantes.append(numero)
        return self.__valores_faltantes


