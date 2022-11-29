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
            # Jogo incompleto:
            [0, 0, 8, 2, 0, 5, 6, 0, 0], [0, 0, 0, 3, 0, 9, 0, 0, 0], [3, 0, 0, 7, 0, 4, 0, 0, 8],
            [9, 6, 5, 0, 0, 0, 4, 2, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 8, 7, 0, 0, 0, 1, 5, 6],
            [6, 0, 0, 8, 0, 3, 0, 0, 9], [0, 0, 0, 4, 0, 1, 0, 0, 0], [0, 0, 1, 6, 0, 7, 8, 0, 0]
        ]

        self.__linhas: list[Linha] = []
        self.__colunas: list[Coluna] = []
        self.__conjuntos: list[Conjunto] = []
        self.__atualizar_atributos_linhas_colunas_conjuntos()


    def __str__(self):
        return "Matriz de soduku de 9x9."


    def __get_linhas(self) -> list[Linha]:
        linhas = [Linha(self.__tabela[0]), Linha(self.__tabela[1]), Linha(self.__tabela[2]),
                  Linha(self.__tabela[3]), Linha(self.__tabela[4]), Linha(self.__tabela[5]),
                  Linha(self.__tabela[6]), Linha(self.__tabela[7]), Linha(self.__tabela[8])]
        return linhas


    def __get_colunas(self) -> list[Coluna]:
        colunas = []
        colunas_aux = [[], [], [], [], [], [], [], [], []]

        for coluna in range(9):
            for linha in range(9):
                colunas_aux[coluna].append(self.__tabela[linha][coluna])

        for coluna in colunas_aux:
            colunas.append(Coluna(coluna))

        return colunas


    def __get_conjuntos(self) -> list[Conjunto]:
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
        self.__linhas = self.__get_linhas()
        self.__colunas = self.__get_colunas()
        self.__conjuntos = self.__get_conjuntos()


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


    def __inserir_numero_na_matriz_pelo_conjunto(self, conjunto: int, posicao: int, numero: int) -> None:
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


    def __inserir_numero_na_matriz_pela_linha(self, linha: int, posicao: int, numero: int) -> None:
        self.__tabela[linha][posicao] = numero


    def __inserir_numero_na_matriz_pela_coluna(self, coluna: int, posicao: int, numero: int) -> None:
        self.__tabela[posicao][coluna] = numero


    def __atualiza_conjunto_se_faltar_apenas_um_item(self) -> None:
        soma_dos_elementos_de_um_conjunto = 45
        for indice, conjunto in enumerate(self.__conjuntos):
            if (conjunto.get_quantidade_de_zeros() == 1):
                numero_faltante = soma_dos_elementos_de_um_conjunto - conjunto.get_soma_dos_elementos()
                self.__inserir_numero_na_matriz_pelo_conjunto(indice, conjunto.get_posicao_dos_zeros()[0], numero_faltante)
        self.__atualizar_atributos_linhas_colunas_conjuntos()


    def __atualiza_linha_se_faltar_apenas_um_item(self) -> None:
        soma_dos_elementos_de_uma_linha = 45
        for indice, linha in enumerate(self.__linhas):
            if (linha.get_quantidade_de_zeros() == 1):
                numero_faltante = soma_dos_elementos_de_uma_linha - linha.get_soma_dos_elementos()
                self.__inserir_numero_na_matriz_pela_linha(indice, linha.get_posicao_dos_zeros()[0], numero_faltante)
        self.__atualizar_atributos_linhas_colunas_conjuntos()


    def __atualiza_coluna_se_faltar_apenas_um_item(self) -> None:
        soma_dos_elementos_de_uma_coluna = 45
        for indice, coluna in enumerate(self.__colunas):
            if (coluna.get_quantidade_de_zeros() == 1):
                numero_faltante = soma_dos_elementos_de_uma_coluna - coluna.get_soma_dos_elementos()
                self.__inserir_numero_na_matriz_pela_coluna(indice, coluna.get_posicao_dos_zeros()[0], numero_faltante)
        self.__atualizar_atributos_linhas_colunas_conjuntos()


    @staticmethod
    def __get_linha_de_uma_posicao_no_conjunto(index_do_conjunto: int, posicao: int) -> int:
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
    def __get_coluna_de_uma_posicao_no_conjunto(index_do_conjunto: int, posicao: int) -> int:
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


    def __atualiza_conjunto_avaliando_linhas_e_colunas(self, posicoes_com_zero: list[list[int]], valores_faltantes: list[list[int]]) -> None:
        linhas_contem_valor_em_teste = [False, False]
        colunas_contem_valor_em_teste = [False, False]
        for indice_do_conjunto, conjunto in enumerate(self.__conjuntos):
            for posicao_com_zero in posicoes_com_zero[indice_do_conjunto]:
                linha = self.__get_linha_de_uma_posicao_no_conjunto(indice_do_conjunto, posicao_com_zero)
                coluna = self.__get_coluna_de_uma_posicao_no_conjunto(indice_do_conjunto, posicao_com_zero)

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

                    """
                    Se a linha e a coluna de uma posicao em teste não conter o valor em teste e
                    as outras duas linhas e duas colunas do conjunto tiverem o valor,
                    insere o valor em teste na posicao em teste.
                    """
                    if ((linha_contem_valor_em_teste == False) and (coluna_contem_valor_em_teste == False) and
                        (linhas_contem_valor_em_teste[0] == True) and (linhas_contem_valor_em_teste[1] == True) and
                        (colunas_contem_valor_em_teste[0] == True) and (colunas_contem_valor_em_teste[1] == True)):
                        self.__inserir_numero_na_matriz_pelo_conjunto(indice_do_conjunto, posicao_com_zero, valor_em_teste)
                        self.__atualizar_atributos_linhas_colunas_conjuntos()


    def __atualiza_conjunto_avaliando_posicoes_vazias_cobertas_por_linhas_e_colunas(self, posicoes_com_zero: list[list[int]], valores_faltantes: list[list[int]]) -> None:
        for indice_do_conjunto, conjunto in enumerate(self.__conjuntos):
            for posicao in posicoes_com_zero[indice_do_conjunto]:
                for valor in valores_faltantes[indice_do_conjunto]:
                    posicoes_com_zero_aux = posicoes_com_zero[indice_do_conjunto].copy()

                    """
                    Se na linha da posicao testada contiver o valor testado, 
                    desconsidera todas as posicoes vazias na linha para aquele valor.
                    """
                    linhas_do_conjunto = conjunto.get_linhas_do_conjunto_na_matriz()
                    for linha in linhas_do_conjunto:
                        if (self.__linhas[linha].contem(valor)):
                            if (linha == 0 or linha == 3 or linha == 6):
                                for posicao_avaliada in [0, 1, 2]:
                                    if (posicao_avaliada in posicoes_com_zero_aux):
                                        posicoes_com_zero_aux.remove(posicao_avaliada)
                            elif (linha == 1 or linha == 4 or linha == 7):
                                for posicao_avaliada in [3, 4, 5]:
                                    if (posicao_avaliada in posicoes_com_zero_aux):
                                        posicoes_com_zero_aux.remove(posicao_avaliada)
                            elif (linha == 2 or linha == 5 or linha == 8):
                                for posicao_avaliada in [6, 7, 8]:
                                    if (posicao_avaliada in posicoes_com_zero_aux):
                                        posicoes_com_zero_aux.remove(posicao_avaliada)

                    """
                    Se na coluna da posicao testada contiver o valor testado, 
                    desconsidera todas as posicoes vazias na coluna para aquele valor.
                    """
                    colunas_do_conjunto = conjunto.get_colunas_do_conjunto_na_matriz()
                    for coluna in colunas_do_conjunto:
                        if (self.__colunas[coluna].contem(valor)):
                            if (coluna == 0 or coluna == 3 or coluna == 6):
                                for posicao_avaliada in [0, 3, 6]:
                                    if (posicao_avaliada in posicoes_com_zero_aux):
                                        posicoes_com_zero_aux.remove(posicao_avaliada)
                            elif (coluna == 1 or coluna == 4 or coluna == 7):
                                for posicao_avaliada in [1, 4, 7]:
                                    if (posicao_avaliada in posicoes_com_zero_aux):
                                        posicoes_com_zero_aux.remove(posicao_avaliada)
                            elif (coluna == 2 or coluna == 5 or coluna == 8):
                                for posicao_avaliada in [2, 5, 8]:
                                    if (posicao_avaliada in posicoes_com_zero_aux):
                                        posicoes_com_zero_aux.remove(posicao_avaliada)

                    """
                    Se na linha e coluna testadas não haver o valor em teste e 
                    a quantidade de posicoes vazias no conjunto para aquele valor for 1,
                    insere o valor testado na posicao vazia restante do conjunto.
                    """
                    linha_da_posicao_testada_contem_valor_testado = self.__linhas[self.__get_linha_de_uma_posicao_no_conjunto(indice_do_conjunto, posicao)].contem(valor)
                    coluna_da_posicao_testada_contem_valor_testado = self.__colunas[self.__get_coluna_de_uma_posicao_no_conjunto(indice_do_conjunto, posicao)].contem(valor)
                    quantidade_de_posicoes_nao_cobertas_no_conjunto = len(posicoes_com_zero_aux)
                    if (quantidade_de_posicoes_nao_cobertas_no_conjunto == 1 and linha_da_posicao_testada_contem_valor_testado == False and coluna_da_posicao_testada_contem_valor_testado == False):
                        self.__inserir_numero_na_matriz_pelo_conjunto(indice_do_conjunto, posicoes_com_zero_aux[0], valor)
                        self.__atualizar_atributos_linhas_colunas_conjuntos()


    def __get_posicao_dos_zeros_nos_conjuntos_da_matriz(self) -> list[list[int]]:
        posicoes_com_zero = []
        for indice, conjunto in enumerate(self.__conjuntos):
            posicoes_com_zero.append(conjunto.get_posicao_dos_zeros())
        return posicoes_com_zero


    def __get_valores_faltantes_nos_conjuntos_da_matriz(self) -> list[list[int]]:
        valores_faltantes = []
        for indice, conjunto in enumerate(self.__conjuntos):
            valores_faltantes.append(conjunto.get_valores_faltantes())
        return valores_faltantes


    def __verificar_conjuntos(self) -> None:
        self.__atualiza_conjunto_se_faltar_apenas_um_item()
        posicoes_com_zero = self.__get_posicao_dos_zeros_nos_conjuntos_da_matriz()
        valores_faltantes = self.__get_valores_faltantes_nos_conjuntos_da_matriz()
        self.__atualiza_conjunto_avaliando_linhas_e_colunas(posicoes_com_zero, valores_faltantes)
        self.__atualiza_conjunto_avaliando_posicoes_vazias_cobertas_por_linhas_e_colunas(posicoes_com_zero, valores_faltantes)


    def __verificar_linhas(self) -> None:
        self.__atualiza_linha_se_faltar_apenas_um_item()


    def __verificar_colunas(self) -> None:
        self.__atualiza_coluna_se_faltar_apenas_um_item()


    def solucionar_matriz(self) -> None:
        soma_de_todos_elementos_de_uma_matriz_completa = 405
        contador_de_iteracoes = 0
        soma_atual_da_matriz = 0

        while soma_atual_da_matriz != soma_de_todos_elementos_de_uma_matriz_completa:
            self.__verificar_conjuntos()
            self.__verificar_linhas()
            self.__verificar_colunas()

            soma_atual_da_matriz = 0
            for linha in self.__tabela:
                for numero in linha:
                    soma_atual_da_matriz += numero

            contador_de_iteracoes += 1
            if (contador_de_iteracoes == 50):
                print("Nao foi possivel resolver a matriz!")
                return

        print(f"Matriz resolvida em {contador_de_iteracoes} iteracoes!")
