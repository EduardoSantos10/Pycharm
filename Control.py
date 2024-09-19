from Model import Model

class Control:
    def __init__(self):
        self.modelo = Model() #instanciando a classe model
        self.opcao = 0 #Tornando opcao global

    def mostrarMenu(self): # torna o método e as funções globais
        print('Escolha uma das opções abaixo: ' +
              '\n0. Sair'                       +
              '\n1. Exercício 01'               +
              '\n2. Exercício 02'               +
              '\n3. Exercício 03'               )

    def operacoes(self):
        while(self.opcao != 1):
            self.mostrarMenu()
            self.opcao = int (input('Informe um número: '))
            if self.opcao == 1:
                print('Obrigado')
            elif self.opcao == 1:
                print(self.modelo.exercicioUm())
            elif self.opcao == 2:
                print(self.modelo.exercicioDois())
            elif self.opcao == 3:
                print(self.modelo.exercicioTres())
            else:
                print('Opção escolhida não é válida')
