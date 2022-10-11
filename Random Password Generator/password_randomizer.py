from random import choice
import string
import PySimpleGUI as sg

password_size = 0

class Password_randomizer:
    def __init__(self):
        sg.change_look_and_feel('Topanga')
        layout =[
            [sg.Text('Quantos caracteres a senha deve ter (digite um número inteiro)? ', size = (50, 0)),
            sg.Input(size = (5, 0), key='size')],
            [sg.Output(size=(62, 5))],
            [sg.Button('Gerar senha')]
        ]

        self.screen = sg.Window('Gerador de senhas').layout(layout)

    def Randomizing(self):
        while True:
            self.button, self.values = self.screen.Read()
            password_size = int(self.values['size'])
            password_seed = string.ascii_letters + string.digits + string.punctuation
            password = ''
            for index in range(password_size):
                password += choice(password_seed)
            print(f'Esta foi a senha gerada: {password}')
            print('-' * 105)

program = Password_randomizer()
program.Randomizing()
