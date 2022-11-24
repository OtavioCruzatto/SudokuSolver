class Conjunto:

    def __init__(self, conjunto: list[int], indice_na_matriz) -> None:
        self.__conjunto = conjunto
        self.__posicao_dos_zeros: list[int] = []
        self.__soma_dos_elementos: int = 0
        self.__quantidade_de_zeros: int = 0
        self.__valores_faltantes: list[int] = []
        self.__indice_na_matriz: int = indice_na_matriz

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

    def trecho_da_linha_no_conjunto_esta_completo(self, linha_da_matriz: int) -> bool:
        if (self.__indice_na_matriz < 3):
            linha_no_conjunto = linha_da_matriz
        elif (self.__indice_na_matriz < 6):
            linha_no_conjunto = linha_da_matriz - 3
        else:
            linha_no_conjunto = linha_da_matriz - 6

        if (linha_no_conjunto == 0):
            if (0 not in self.__conjunto[0:3]):
                return True
        elif (linha_no_conjunto == 1):
            if (0 not in self.__conjunto[3:6]):
                return True
        elif (linha_no_conjunto == 2):
            if (0 not in self.__conjunto[6:9]):
                return True
        else:
            return False

        return False

    def trecho_da_coluna_no_conjunto_esta_completo(self, coluna_da_matriz: int) -> bool:
        if ((self.__indice_na_matriz % 3) == 0):
            coluna_no_conjunto = coluna_da_matriz
        elif ((self.__indice_na_matriz % 3) == 1):
            coluna_no_conjunto = coluna_da_matriz - 3
        else:
            coluna_no_conjunto = coluna_da_matriz - 6

        if (coluna_no_conjunto == 0):
            if (self.__conjunto[0] != 0 and self.__conjunto[3] != 0 and self.__conjunto[6] != 0):
                return True
        elif (coluna_no_conjunto == 1):
            if (self.__conjunto[1] != 0 and self.__conjunto[4] != 0 and self.__conjunto[7] != 0):
                return True
        elif (coluna_no_conjunto == 2):
            if (self.__conjunto[2] != 0 and self.__conjunto[5] != 0 and self.__conjunto[8] != 0):
                return True
        else:
            return False

        return False

    def get_linhas_do_conjunto_na_matriz(self) -> tuple[int, int, int]:
        if (self.__indice_na_matriz < 3):
            return (0, 1, 2)
        elif (self.__indice_na_matriz < 6):
            return (3, 4, 5)
        else:
            return (6, 7, 8)

    def get_colunas_do_conjunto_na_matriz(self) -> tuple[int, int, int]:
        if ((self.__indice_na_matriz % 3) == 0):
            return (0, 1, 2)
        elif ((self.__indice_na_matriz % 3) == 1):
            return (3, 4, 5)
        else:
            return (6, 7, 8)


