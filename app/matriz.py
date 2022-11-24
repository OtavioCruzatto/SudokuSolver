from linha import Linha
from coluna import Coluna
from conjunto import Conjunto

class Matriz:


    def __init__(self):
        self.__tabela: list[
            list[int], list[int], list[int],
            list[int], list[int], list[int],
            list[int], list[int], list[int]
        ] = [
            # Condicao inicial:
            #[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            #[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            #[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
            # Teste 1:
            #[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 1], [3, 4, 5, 6, 7, 8, 9, 1, 2],
            #[4, 5, 6, 7, 8, 9, 1, 2, 3], [5, 6, 7, 8, 9, 1, 2, 3, 4], [6, 7, 8, 9, 1, 2, 3, 4, 5],
            #[7, 8, 9, 1, 2, 3, 4, 5, 6], [8, 9, 1, 2, 3, 4, 5, 6, 7], [9, 1, 2, 3, 4, 5, 6, 7, 8]
            # Testar linha:
            #[1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3],
            #[4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6],
            #[7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]
            # Testar coluna:
            # [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
            # [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
            # [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # Testar conjunto:
            # [1, 1, 1, 2, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3],
            # [4, 4, 4, 5, 5, 5, 6, 6, 6], [4, 4, 4, 5, 5, 5, 6, 6, 6], [4, 4, 4, 5, 5, 5, 6, 6, 6],
            # [7, 7, 7, 8, 8, 8, 9, 9, 9], [7, 7, 7, 8, 8, 8, 9, 9, 9], [7, 7, 7, 8, 8, 8, 9, 9, 9]
            # Jogo incompleto:
            [0, 0, 0, 9, 1, 0, 6, 0, 0], [3, 0, 4, 7, 8, 0, 1, 5, 2], [8, 1, 6, 4, 2, 0, 0, 9, 3],
            [9, 0, 3, 0, 6, 2, 0, 0, 0], [0, 0, 0, 0, 3, 0, 5, 0, 0], [1, 7, 0, 0, 0, 4, 0, 2, 0],
            [0, 0, 7, 0, 0, 1, 0, 0, 0], [6, 3, 0, 0, 0, 0, 4, 0, 5], [0, 0, 0, 0, 4, 0, 0, 3, 7]
            # Resultado:
            # [7, 5, 2, 9, 1, 3, 6, 8, 4], [3, 9, 4, 7, 8, 6, 1, 5, 2], [8, 1, 6, 4, 2, 5, 7, 9, 3],
            # [9, 4, 3, 5, 6, 2, 8, 7, 1], [2, 6, 8, 1, 3, 7, 5, 4, 9], [1, 7, 5, 8, 9, 4, 3, 2, 6],
            # [4, 2, 7, 3, 5, 1, 9, 6, 8], [6, 3, 9, 2, 7, 8, 4, 1, 5], [5, 8, 1, 6, 4, 9, 2, 3, 7]
            # Testes:
            # [7, 5, 2, 9, 1, 3, 6, 8, 4], [3, 9, 4, 7, 8, 6, 1, 5, 2], [8, 1, 6, 4, 2, 5, 7, 9, 3],
            # [9, 4, 3, 5, 6, 2, 8, 7, 1], [2, 6, 8, 1, 3, 7, 5, 4, 9], [1, 7, 5, 8, 9, 4, 3, 2, 6],
            # [4, 2, 7, 3, 5, 1, 9, 6, 8], [6, 3, 9, 2, 7, 8, 4, 1, 5], [5, 8, 1, 6, 4, 9, 2, 3, 7]
        ]

        self.__linhas: list[Linha] = []
        self.__colunas: list[Coluna] = []
        self.__conjuntos: list[Conjunto] = []
        self.__atualizar_atributos_linhas_colunas_conjuntos()


    def __str__(self):
        return "Matriz de soduku de 9x9."


    def obter_linhas(self) -> list[Linha]:
        linhas = [Linha(self.__tabela[0]), Linha(self.__tabela[1]), Linha(self.__tabela[2]),
                  Linha(self.__tabela[3]), Linha(self.__tabela[4]), Linha(self.__tabela[5]),
                  Linha(self.__tabela[6]), Linha(self.__tabela[7]), Linha(self.__tabela[8])]
        return linhas


    def obter_colunas(self) -> list[Coluna]:
        colunas = []
        colunas_aux = [[], [], [], [], [], [], [], [], []]

        for coluna in range(9):
            for linha in range(9):
                colunas_aux[coluna].append(self.__tabela[linha][coluna])

        for coluna in colunas_aux:
            colunas.append(Coluna(coluna))

        return colunas


    def obter_conjuntos(self) -> list[Conjunto]:
        conjuntos = []
        conjunto_aux = [[], [], [], [], [], [], [], [], []]

        for conjunto in range(9):
            if (conjunto == 0):
                for linha in range(0, 3):
                    for coluna in range(0, 3):
                        conjunto_aux[conjunto].append(self.__tabela[linha][coluna])
            elif (conjunto == 1):
                for linha in range(0, 3):
                    for coluna in range(3, 6):
                        conjunto_aux[conjunto].append(self.__tabela[linha][coluna])
            elif (conjunto == 2):
                for linha in range(0, 3):
                    for coluna in range(6, 9):
                        conjunto_aux[conjunto].append(self.__tabela[linha][coluna])
            elif (conjunto == 3):
                for linha in range(3, 6):
                    for coluna in range(0, 3):
                        conjunto_aux[conjunto].append(self.__tabela[linha][coluna])
            elif (conjunto == 4):
                for linha in range(3, 6):
                    for coluna in range(3, 6):
                        conjunto_aux[conjunto].append(self.__tabela[linha][coluna])
            elif (conjunto == 5):
                for linha in range(3, 6):
                    for coluna in range(6, 9):
                        conjunto_aux[conjunto].append(self.__tabela[linha][coluna])
            elif (conjunto == 6):
                for linha in range(6, 9):
                    for coluna in range(0, 3):
                        conjunto_aux[conjunto].append(self.__tabela[linha][coluna])
            elif (conjunto == 7):
                for linha in range(6, 9):
                    for coluna in range(3, 6):
                        conjunto_aux[conjunto].append(self.__tabela[linha][coluna])
            else:
                for linha in range(6, 9):
                    for coluna in range(6, 9):
                        conjunto_aux[conjunto].append(self.__tabela[linha][coluna])

        for indice_da_lista, lista in enumerate(conjunto_aux):
            conjuntos.append(Conjunto(lista, indice_da_lista))

        return conjuntos


    def __atualizar_atributos_linhas_colunas_conjuntos(self) -> None:
        self.__linhas = self.obter_linhas()
        self.__colunas = self.obter_colunas()
        self.__conjuntos = self.obter_conjuntos()


    @staticmethod
    def __imprimir_linha_de_separacao(indice_da_linha: int) -> None:
        if (indice_da_linha % 3) == 0:
            print()


    @staticmethod
    def __imprimir_espacamento_entre_trios_de_numeros(posicao: int) -> None:
        if ((posicao % 3) == 0):
            print("", end="  ")


    def __imprimir_numeros_da_linha(self, linha: list[int]) -> None:
        for posicao, numero in enumerate(linha):
            self.__imprimir_espacamento_entre_trios_de_numeros(posicao)
            print(numero, end="  ")


    def exibir_matriz(self) -> None:
        for indice_da_linha, linha in enumerate(self.__tabela):
            self.__imprimir_linha_de_separacao(indice_da_linha)
            self.__imprimir_numeros_da_linha(linha)
            print()
        print()


    def inserir_numero_na_matriz_pelo_conjunto(self, conjunto: int, posicao: int, numero: int) -> None:
        if (conjunto == 0):
            if (posicao < 3):
                self.__tabela[0][posicao] = numero
            elif (posicao < 6):
                self.__tabela[1][posicao - 3] = numero
            else:
                self.__tabela[2][posicao - 6] = numero
        elif (conjunto == 1):
            if (posicao < 3):
                self.__tabela[0][posicao + 3] = numero
            elif (posicao < 6):
                self.__tabela[1][posicao] = numero
            else:
                self.__tabela[2][posicao - 3] = numero
        elif (conjunto == 2):
            if (posicao < 3):
                self.__tabela[0][posicao + 6] = numero
            elif (posicao < 6):
                self.__tabela[1][posicao + 3] = numero
            else:
                self.__tabela[2][posicao] = numero
        elif (conjunto == 3):
            if (posicao < 3):
                self.__tabela[3][posicao] = numero
            elif (posicao < 6):
                self.__tabela[4][posicao - 3] = numero
            else:
                self.__tabela[5][posicao - 6] = numero
        elif (conjunto == 4):
            if (posicao < 3):
                self.__tabela[3][posicao + 3] = numero
            elif (posicao < 6):
                self.__tabela[4][posicao] = numero
            else:
                self.__tabela[5][posicao - 3] = numero
        elif (conjunto == 5):
            if (posicao < 3):
                self.__tabela[3][posicao + 6] = numero
            elif (posicao < 6):
                self.__tabela[4][posicao + 3] = numero
            else:
                self.__tabela[5][posicao] = numero
        elif (conjunto == 6):
            if (posicao < 3):
                self.__tabela[6][posicao] = numero
            elif (posicao < 6):
                self.__tabela[7][posicao - 3] = numero
            else:
                self.__tabela[8][posicao - 6] = numero
        elif (conjunto == 7):
            if (posicao < 3):
                self.__tabela[6][posicao + 3] = numero
            elif (posicao < 6):
                self.__tabela[7][posicao] = numero
            else:
                self.__tabela[8][posicao - 3] = numero
        else:
            if (posicao < 3):
                self.__tabela[6][posicao + 6] = numero
            elif (posicao < 6):
                self.__tabela[7][posicao + 3] = numero
            else:
                self.__tabela[8][posicao] = numero


    def inserir_numero_na_matriz_pela_linha(self, linha: int, posicao: int, numero: int) -> None:
        self.__tabela[linha][posicao] = numero


    def inserir_numero_na_matriz_pela_coluna(self, coluna: int, posicao: int, numero: int) -> None:
        self.__tabela[posicao][coluna] = numero


    def atualiza_conjunto_se_faltar_apenas_um_item(self) -> None:
        soma_dos_elementos_de_um_conjunto = 45
        for indice, conjunto in enumerate(self.__conjuntos):
            if (conjunto.get_quantidade_de_zeros() == 1):
                numero_faltante = soma_dos_elementos_de_um_conjunto - conjunto.get_soma_dos_elementos()
                self.inserir_numero_na_matriz_pelo_conjunto(indice, conjunto.get_posicao_dos_zeros()[0], numero_faltante)
        self.__atualizar_atributos_linhas_colunas_conjuntos()


    def atualiza_linha_se_faltar_apenas_um_item(self) -> None:
        soma_dos_elementos_de_uma_linha = 45
        for indice, linha in enumerate(self.__linhas):
            if (linha.get_quantidade_de_zeros() == 1):
                numero_faltante = soma_dos_elementos_de_uma_linha - linha.get_soma_dos_elementos()
                self.inserir_numero_na_matriz_pela_linha(indice, linha.get_posicao_dos_zeros()[0], numero_faltante)
        self.__atualizar_atributos_linhas_colunas_conjuntos()


    def atualiza_coluna_se_faltar_apenas_um_item(self) -> None:
        soma_dos_elementos_de_uma_coluna = 45
        for indice, coluna in enumerate(self.__colunas):
            if (coluna.get_quantidade_de_zeros() == 1):
                numero_faltante = soma_dos_elementos_de_uma_coluna - coluna.get_soma_dos_elementos()
                self.inserir_numero_na_matriz_pela_coluna(indice, coluna.get_posicao_dos_zeros()[0], numero_faltante)
        self.__atualizar_atributos_linhas_colunas_conjuntos()


    def __exibir_atributos_linhas_colunas_conjuntos(self) -> None:
        print("Linhas:")
        for linha in self.__linhas:
            print(linha.get_linha())

        print("Colunas:")
        for coluna in self.__colunas:
            print(coluna.get_coluna())

        print("Conjuntos:")
        for conjunto in self.__conjuntos:
            print(conjunto.get_conjunto())

    @staticmethod
    def __obter_linha_de_uma_posicao_no_conjunto(index_do_conjunto: int, posicao: int) -> int:
        if (posicao < 3):
            linha_da_posicao_no_conjunto = 0
        elif (posicao < 6):
            linha_da_posicao_no_conjunto = 1
        else:
            linha_da_posicao_no_conjunto = 2

        if (index_do_conjunto < 3):
            linha_da_posicao_no_conjunto += 0
        elif (index_do_conjunto < 6):
            linha_da_posicao_no_conjunto += 3
        else:
            linha_da_posicao_no_conjunto += 6

        return linha_da_posicao_no_conjunto

    @staticmethod
    def __obter_coluna_de_uma_posicao_no_conjunto(index_do_conjunto: int, posicao: int) -> int:
        if ((posicao % 3) == 0):
            coluna_da_posicao_no_conjunto = 0
        elif ((posicao % 3) == 1):
            coluna_da_posicao_no_conjunto = 1
        else:
            coluna_da_posicao_no_conjunto = 2

        if ((index_do_conjunto % 3) == 0):
            coluna_da_posicao_no_conjunto += 0
        elif ((index_do_conjunto % 3) == 1):
            coluna_da_posicao_no_conjunto += 3
        else:
            coluna_da_posicao_no_conjunto += 6

        return coluna_da_posicao_no_conjunto


    def verificar_conjuntos(self) -> None:
        self.atualiza_conjunto_se_faltar_apenas_um_item()

        posicoes_com_zero = []
        valores_faltantes = []
        for indice, conjunto in enumerate(self.__conjuntos):
            posicoes_com_zero.append(conjunto.get_posicao_dos_zeros())
            valores_faltantes.append(conjunto.get_valores_faltantes())
            print(f"Conjunto {indice}: Posicoes com zero: {posicoes_com_zero[indice]}")
            print(f"Conjunto {indice}: Valores faltantes: {valores_faltantes[indice]}")
            print()

        linhas_contem_valor_em_teste = [False, False]
        colunas_contem_valor_em_teste = [False, False]
        for indice_do_conjunto, conjunto in enumerate(self.__conjuntos):
            for posicao_com_zero in posicoes_com_zero[indice_do_conjunto]:
                linha = self.__obter_linha_de_uma_posicao_no_conjunto(indice_do_conjunto, posicao_com_zero)
                coluna = self.__obter_coluna_de_uma_posicao_no_conjunto(indice_do_conjunto, posicao_com_zero)

                for valor_em_teste in valores_faltantes[indice_do_conjunto]:
                    linha_contem_valor_em_teste = self.__linhas[linha].contem(valor_em_teste)
                    coluna_contem_valor_em_teste = self.__colunas[coluna].contem(valor_em_teste)

                    linha_analizada = 0
                    for linha_no_conjunto in conjunto.get_linhas_do_conjunto_na_matriz():
                        if (linha_no_conjunto != linha):
                            if conjunto.trecho_da_linha_no_conjunto_esta_completo(linha_no_conjunto):
                                linhas_contem_valor_em_teste[linha_analizada] = True
                            else:
                                linhas_contem_valor_em_teste[linha_analizada] = self.__linhas[linha_no_conjunto].contem(valor_em_teste)
                            linha_analizada += 1

                    coluna_analizada = 0
                    for coluna_no_conjunto in conjunto.get_colunas_do_conjunto_na_matriz():
                        if (coluna_no_conjunto != coluna):
                            if conjunto.trecho_da_coluna_no_conjunto_esta_completo(coluna_no_conjunto):
                                colunas_contem_valor_em_teste[coluna_analizada] = True
                            else:
                                colunas_contem_valor_em_teste[coluna_analizada] = self.__colunas[coluna_no_conjunto].contem(valor_em_teste)
                            coluna_analizada += 1


                    if ((linha_contem_valor_em_teste == False) and (coluna_contem_valor_em_teste == False) and
                        (linhas_contem_valor_em_teste[0] == True) and (linhas_contem_valor_em_teste[1] == True) and
                        (colunas_contem_valor_em_teste[0] == True) and (colunas_contem_valor_em_teste[1] == True)):
                        self.inserir_numero_na_matriz_pelo_conjunto(indice_do_conjunto, posicao_com_zero, valor_em_teste)
                        self.__atualizar_atributos_linhas_colunas_conjuntos()


    def verificar_linhas(self) -> None:
        self.atualiza_linha_se_faltar_apenas_um_item()


    def verificar_colunas(self) -> None:
        self.atualiza_coluna_se_faltar_apenas_um_item()


    def solucionar_matriz(self) -> None:

        for i in range(50):
            self.verificar_conjuntos()
            self.verificar_linhas()
            self.verificar_colunas()
        print("=============================")

