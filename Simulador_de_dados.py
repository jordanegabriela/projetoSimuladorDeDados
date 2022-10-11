# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6

# biblioteca que gera valores aleatórios
import random
# biblioteca para importar Interface Gráfica
import PySimpleGUI as sg


class SimuladorDeDado:
    # para DEFINIR o comportamento inicial da classe
    def __init__(self):
        # o que é preciso inicialmente? valor inicial, final e alguma interação
        # primeira função extremamente básica criada
        self.valorMinimo = 1
        self.valorMaximo = 6
        #self.mensagem = 'Você gostaria de gerar um valor para o dado?'

        # INTERFACE
        # Layout
        self.layout = [
            [sg.Text('Jogar dado?')],
            [sg.Button('SIM'), sg.Button('NÃO')]
        ]

    # Segunda função: feita para de fato começar a rodar o 'inicio' do programa

    def Iniciar(self):

        # Criar janela
        self.janela = sg.Window('Simulador de dado', layout = self.layout)
        # Ler valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Usar valores da tela

        # vamos perguntar ao usuário e guardar a resposta dele
        #resposta = input(self.mensagem) - cod 1
        # fazer o tratamento de um possível erro

        while True:
            try:
                    # tomar uma decisão com resposta dele
                if self.eventos == 'sim' or self.eventos == 's':
                    # criar um metodo para que o código fique mais organizado
                    self.GerarValor()

                elif self.eventos == 'NÃO' or self.eventos == 'n' or self.eventos == 'nao':
                    print('Ok!Agradecemos sua participação.')

                else:
                    print('Por favor, digite: SIM ou NÃO')
            except:
                    print('Ocorreu um erro!')

    def GerarValor(self):
        # randint é uma forma de gerar valor inteiro, seja minimo ou max
        print(random.randint(self.valorMinimo, self.valorMaximo))


# para usar uma classe precisamos instanciar
simulador = SimuladorDeDado()
simulador.Iniciar()
