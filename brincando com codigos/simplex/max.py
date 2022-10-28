from tabulate import tabulate
from colorama import Fore

class Simplex:

    def __init__(self):
        self.table = []
        self._order_a = {}
        self._order_b = {}
        self._folga = 0
        self._var_folga = 0
        self._chara = 0

    def validate_z(self, list:list):
        if self._chara == len(list):
            return True
        else:
            print(f"{Fore.RED}o numero de variaveis esta diferente do aceitavel{Fore.RESET}")
            return False

    def validate_res(self, list:list):
        if self._chara+1 == len(list):
            if list[-1] != 0:
                return True
            else:
                print(f"{Fore.RED}o Rs não pode ser 0{Fore.RESET}")
                return False
        else:
            print(f"{Fore.RED}o numero de variaveis esta diferente do aceitavel{Fore.RESET}")
            return False

    def edit_ord_a(self,lista: list, folga: int):
        self._chara = len(lista)
        order={}
        leng = 0
        order[0] = "base"
        for char in range(len(lista)):
            order[char+1] = lista[char]
            leng+=1
        for x in range(folga):
            order[leng+1] = f"f{x}"
            leng+=1
        order[leng+1] = "rs"
        self._order_a = order
        self._folga = folga
        self.edit_ord_b()
        
    def edit_ord_b(self):
        order={}
        order[0] = "Z"
        for x in range(self._folga):
            order[x+1] = f"f{x}"
        self._order_b = order
   
    def edit_list(self, li: list):
        last = li[-1]
        li.pop(-1)
        new_list = li
        for x in range(self._folga):
            if(x == self._var_folga):
                new_list.append(1)
            else:
                new_list.append(0)
        new_list.append(last)
        self._var_folga+=1
        return new_list

    def set_max_Z(self, sz: list):
        if(self.validate_z(sz)):
            sz = [value * -1 for value in sz]
            for x in range(self._folga+1):
                sz.append(0)
            self.table.append(sz)
            return True
        else:
            return False

    def set_restricoes(self, sr: list):
        if(self.validate_res(sr)):
            sr_n = self.edit_list(sr)
            self.table.append(sr_n)
            return True
        else:
            return False
    
    def get_coluna_pivo_index(self) -> int:
        coluna_pivo = min(self.table[0])
        index = self.table[0].index(coluna_pivo)

        return index
    
    def get_linha_pivo_index(self, coluna_pivo_index:int)->int:
        resultados = {}
        for linha in range(len(self.table)):
            if linha > 0:
                if self.table[linha][coluna_pivo_index]> 0:
                    divisao = self.table[linha][-1] / self.table[linha][coluna_pivo_index]
                    resultados[linha] = divisao
        index = min(resultados, key=resultados.get)

        return index

    def calcular_nova_linha_pivo(self, coluna_pivo_index: int, linha_pivo_index: int) -> list:
        linha = self.table[linha_pivo_index]
        pivo = linha[coluna_pivo_index]
        nova_linha_pivo = [value / pivo for value in linha]

        return nova_linha_pivo

    def calcular_nova_linha(self, linha: list, coluna_pivo_index: int, linha_pivo: list) -> list:
        pivo = linha[coluna_pivo_index] * -1
        result_linha = [value * pivo for value in linha_pivo]

        nova_linha = []
        for x in range(len(result_linha)):
            
            valor_soma = result_linha[x] + linha[x]
            nova_linha.append(valor_soma)

        return nova_linha

    def negativo(self)-> bool:
        negativo = list(filter(lambda x: x < 0, self.table[0]))

        return True if len(negativo)> 0 else False

    def mostrar_old(self):
        for y in range(len(self._order_a)):
            print(f"|  {self._order_a[y]}  ", end="")
        print()

        for x in range(len(self.table)):
            if x>0:
                print(f"|  {self._order_b[x]}  ",end="")
                for y in range(len(self.table[0])):
                    print(f"|  {round(self.table[x][y],2)}  ",end="")
                print()
        print(f"|  {self._order_b[0]}  ",end="")
        for y in range(len(self.table[0])):
            print(f"|  {round(self.table[0][y],2)}  ",end="")
        print()
        print(f"\n")

    def mostrar(self):
        
        data = []
        data.append(self._order_a.values())

        for x in range(len(self.table)):
            if x>0:
                organizador = {0: self._order_b[x]}
                for y in range(len(self.table[0])):
                    organizador[y+1] = round(self.table[x][y],2)
                data.append(organizador.values())

        organizador = {0: self._order_b[0]}

        for y in range(len(self.table[0])):
            organizador[y+1] = round(self.table[0][y],2)

        data.append(organizador.values())
        print(f"\n")
        print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
        
    def caucular(self):
        coluna_pivo_index = self.get_coluna_pivo_index()
        linha_pivo_index = self.get_linha_pivo_index(coluna_pivo_index)

        linha_pivo = self.calcular_nova_linha_pivo(coluna_pivo_index, linha_pivo_index)

        for x in range(len(self.table)):
            print(f"linha: {self._order_b[x]} valor: {self.table[x][-1]}{Fore.RESET}")
        print(f"{Fore.BLUE}pivo na linha: {self._order_b[linha_pivo_index]} coluna: {self._order_a[coluna_pivo_index+1]} valor: {self.table[linha_pivo_index][coluna_pivo_index]}{Fore.RESET}")


        self.table[linha_pivo_index] = linha_pivo

        table_copy = self.table.copy()

        index = 0
        self._order_b[linha_pivo_index] = self._order_a[coluna_pivo_index+1]
        while index < len(self.table):
            if index != linha_pivo_index:
                linha = table_copy[index]
                nova_linha = self.calcular_nova_linha(linha, coluna_pivo_index, linha_pivo)
                self.table[index] = nova_linha
            index += 1
        self.mostrar()

    def resolver(self):
        self._order = self.edit_ord_a
        self.mostrar()
        self.caucular()
        while self.negativo():
            self.caucular()
        for x in range(len(self.table)):
            print(f"linha: {self._order_b[x]} valor: {self.table[x][-1]}{Fore.RESET}")
        