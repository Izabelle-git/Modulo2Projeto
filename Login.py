from tkinter import *
from tkinter import ttk

janela = Tk()

class App():
    def __init__(self):
        self.janela = janela
        self.tela() #Chamando a função tela
        self.widgets_tela() #Chamando Widgets da tela

        janela.mainloop()

    def tela(self):
        self.janela.title('LOGIN')  #Título da tela  
        self.janela.configure(background='#faf9f3')  #Cor de fundo 
        self.janela.geometry('350x250')  #Tamanho inicial da tela

    def widgets_tela(self):
        #Criando labels e Entrys
        self.lb_usuario = Label(self.janela, text='Usuário:', bg='#67aeb4', fg='white', font=('arial', 11, 'bold'))
        self.lb_usuario.place(relx=0.10, rely=0.15)
        self.usuario_entry = Entry(self.janela)
        self.usuario_entry.place(relx=0.30, rely=0.15, relwidth=0.5)

        self.lb_senha = Label(self.janela, text='Senha:', bg='#67aeb4', fg='white', font=('arial', 11, 'bold'))
        self.lb_senha.place(relx=0.10, rely=0.30)
        self.senha_entry = Entry(self.janela, show='*')
        self.senha_entry.place(relx=0.30, rely=0.30, relwidth=0.5)

        #Criando Botões
        self.bt_cadastrar = Button(self.janela, text='Cadastrar', bd=2, bg='#107db2', fg='white', font=('arial', 11, 'bold'))
        self.bt_cadastrar.place(relx=0.12, rely=0.50, relwidth=0.25, relheight=0.15)

        self.bt_entrar = Button(self.janela, text='Entrar', bd=2, bg='#107db2', fg='white', font=('arial', 11, 'bold'))
        self.bt_entrar.place(relx=0.39, rely=0.50, relwidth=0.20, relheight=0.15)

        self.bt_sair = Button(self.janela, text='Sair', bd=2, bg='#107db2', fg='white', font=('arial', 11, 'bold'))
        self.bt_sair.place(relx=0.61, rely=0.50, relwidth=0.20, relheight=0.15)

    def verificarCadastro(self):
        usuario = 'teste'
        senha = 1234

        if self.usuario_entry.get() == 'admin' and self.senha_entry.get() == '1234':
            print('Bem vindo')
        else:
            print('Dados Incorretos')
App()    
