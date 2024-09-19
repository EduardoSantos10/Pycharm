class Model:
    def __init__(self):
        #self.num1 = 0
        #self.num2 = 0


     """def trocar(self, valorA, valorB):
        valorC = valorA
        valorA = valorB
        valorB = valorC
        return f'Valor A {valorA} \nValor B: {valorB}'

    def tabuada(self, num):
        resultado = " " #Variavél String
        for i in range(0, 11, 1): #passa parâmetros
            resultado += f'{num} * {i} = {num * i}\n' # += resultado = resultado + resultado
        return resultado

    def mediaTres(self, nota1, nota2, nota3):
        return (nota1 + nota2 + nota3)/3"""

    def exercicioUm(self):
        resultado = ""
        for i in range(1,11,1):
            resultado += f'{i} \n'
        return resultado

    def exercicioDois(self):
        resultado = ""
        for i in range(2,21,2):
            resultado += f'{i} \n'
        return resultado

    def exercicioTres(self):
        resultado = 0
        for i in range(1,101,1):
            resultado += i
        return resultado

    def exercicioQuatro(self):
        resultado = 0
        for i in range(0,50,5):
            resultado += i
        return resultado

    def exercicioSeis(self):
        resultado = 0
        num = 0
        if( num > 10)
