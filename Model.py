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

    def exercicioCinco(self):
        num = float(input('digite um número: '))
        if num % 2 == 0:
            print('par')
        else:
            print('impar')


    def exercicioSeis(self, num):
        if num > 0:
            print('positivo')
        elif num < 0:
            print('negativo')
        elif num == 0:
            print('numero igual a zero!')

    def exercicioSete(self, num):
        resultado = " "
        for i in range(0, 11, 1):  # passa parâmetros
            resultado += f'{num} * {i} = {num * i}\n'
        return resultado

    def exercicioOito(self, num):
        resultado = ''
        for i in range(0, num, 1):
            resultado += f'{i}\n'
        return resultado

    def exercicioNove(self, num):
        resultado = 0
        for i in range(0,(num + 1), 1):
            resultado += i
        return resultado

    def exercicioDez(self, num):
        resultado = '2\n3\n5'
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0: resultado += f'\n{i}'
        return resultado

    def exercicioOnze(self, num):
        if num >= 2:
            for i in range(2, num):
                if num % i != 0:
                    print(num, 'é primo')
                else:
                    print(num, 'não é primo')
                    break


    def exercicioDoze(self, num):
        resultado = 1
        for i in range(1 ,num , 1):
            resultado *= i
        return resultado

    def exercicioTreze(self):

        resultado = "0\n1\n"
        fib1 = 0
        fib2 = 1
        fib3 = 0

        for i in range(1, 9, 1):
            fib3 = fib1 + fib2
            resultado += f'{fib3}\n'
            fib1 = fib2
            fib2 = fib3
        return resultado

    def exercicioQuatorze(self, num):

        resultado = "0\n1\n"
        fib1 = 0
        fib2 = 1
        fib3 = 0

        for i in range(0, 50, 1):
            fib3 = fib1 + fib2
            resultado += f'{fib3}\n'
            fib1 = fib2
            fib2 = fib3
            if num == fib3:
                return f'{num}' "Esse número aparece na tabela de fibonacci"

                return f'{num}' "Esse número não é fibonacci"

        return resultado

    def exercicioQuinze(self,num):
        resto = 0
        num % 10
        while num / 10 != 0:
            resto += num % 10
            num += int(num / 10)
        return resto

    def exercicioDezesseis(self, num):
        par = ""
        impar = ""
        resultado = 0
        for i in range(0, (num + 1), 1):
            resultado += i
        num = float(input('digite um número: '))
        if num % 2 == 0:
            print('par')
        else:
            print('impar')
        return resultado

    def exercicioDezessete:
        







