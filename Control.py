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
              '\n3. Exercício 03'               +
              '\n4. Exercício 04'               +
              '\n5. Exercício 05'               +
              '\n6. Exercício 06'               +
              '\n7. Exercício 07'               +
              '\n8. Exercício 08'               +
              '\n9. Exercício 09'               +
              '\n10. Exercício 10'              +
              '\n11. Exercício 11'              +
              '\n12. Exercício 12'              +
              '\n13. Exercício 13'              +
              '\n14. Exercício 14'              +
              '\n15. Exercício 15'              +
              '\n16. Exercício 16'              +
              '\n17. Exercício 17'              +
              '\n18. Exercício 18'              +
              '\n19. Exercício 19'              +
              '\n20. Exercício 20'              )

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
            elif self.opcao == 4:
                print(self.modelo.exercicioQuatro())
            elif self.opcao == 5:
                print(self.modelo.exercicioCinco())
            elif self.opcao == 6:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioSeis(num))
            elif self.opcao == 7:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioSete(num))
            elif self.opcao == 8:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioOito(num))
            elif self.opcao == 9:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioNove(num))
            elif self.opcao == 10:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioDez(num))
            elif self.opcao == 11:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioOnze(num))
            elif self.opcao == 12:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioDoze(num))
            elif self.opcao == 13:
                print(self.modelo.exercicioTreze())
            elif self.opcao == 14:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioQuatorze(num))
            elif self.opcao == 15:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioQuinze(num))
            elif self.opcao == 16:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioDezesseis(num))
            elif self.opcao == 17:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioDezessete(num))
            elif self.opcao == 18:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioDezoito(num))
            elif self.opcao == 19:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioDezenove(num))
            elif self.opcao == 20:
                num = int(input('informe um número: '))
                print(self.modelo.exercicioVinte(num))
            else:
                print('Opção escolhida não é válida')
