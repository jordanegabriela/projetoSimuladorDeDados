# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6

# biblioteca que gera valores aleatórios
import random


class SimuladorDeDado:
    # para DEFINIR o comportamento inicial da classe
    def __init__(self):
        # o que é preciso inicialmente? valor inicial, final e alguma interação
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = 'Você gostaria de gerar um valor para o dado?'
    # primeira função extremamente básica criada

    # Segunda função: feita para de fato começar a rodar o 'inicio' do programa
    def Iniciar(self):
        # vamos perguntar ao usuário e guardar a resposta dele
        resposta = input(self.mensagem)
        # fazer o tratamento de um possível erro
        try:
            # tomar uma decisão com resposta dele
            if resposta == 'sim' or resposta == 's':
                # criar um metodo para que o código fique mais organizado
                self.GerarValor()

            elif resposta == 'não' or resposta == 'n' or resposta == 'nao':
                print('Ok!Agradecemos sua participação.')

            else:
                print('Por favor, digite: sim ou não')
        except:
            print('Ocorreu um erro!')

    def GerarValor(self):
        # randint é uma forma de gerar valor inteiro, seja minimo ou max
        print(random.randint(self.valorMinimo, self.valorMaximo))


# para usar uma classe precisamos instanciar
simulador = SimuladorDeDado()
simulador.Iniciar()
