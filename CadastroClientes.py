from tkinter import *
from tkinter import ttk
import sqlite3
import re
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

janela = Tk()

#Adicionando uma classe para geração de relatorios
class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    
    def gerarRelatorio(self):
        self.c = canvas.Canvas("cliente.pdf")  
        self.codigoRel = self.entry_codigo.get()
        self.nomeRel = self.entry_nome.get()
        self.cpfRel = self.entry_cpf.get()
        self.cepRel = self.entry_cep.get()
        self.cidadeRel = self.entry_cidade.get()
        self.nibge = self.entry_nibge.get()
        self.uf = self.entry_uf.get()
        self.logradouro = self.entry_logradouro.get()
        self.numero = self.entry_numero.get()
        self.telefoneRel = self.entry_telefone.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        #Criando os campos na ficha
        self.c.setFont("Helvetica-Bold", 14)
        self.c.drawString(50, 700, 'Codigo ')
        self.c.drawString(50, 680, 'Nome: ')
        self.c.drawString(50, 660, 'CPF: ')
        self.c.drawString(50, 640, 'CEP: ')
        self.c.drawString(50, 620, 'Cidade: ')
        self.c.drawString(50, 600, 'Nº IBGE: ')
        self.c.drawString(50, 580, 'UF: ')
        self.c.drawString(50, 560, 'Logradouro: ')
        self.c.drawString(50, 540, 'Número: ')
        self.c.drawString(50, 520, 'Telefone: ')

        #Chamando os dados de acordo com a entry do banco
        self.c.setFont("Helvetica-Bold", 14)
        self.c.drawString(105, 700, self.codigoRel)
        self.c.drawString(100, 680, self.nomeRel)
        self.c.drawString(110, 640, self.cidadeRel)
        self.c.drawString(120, 660, self.telefoneRel)
        ###LEMBRAR DE ADICIONAR MAIS COISA AQUI

        #Um detalhe a mais para deixa a ficha bonita
        self.c.rect(185, 780, 215, 35, fill=False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.printCliente()

#Adicionando validadores nas entrys
class Validadores():

    def validar_entry2(self, text): 
        if text == '':
            return True #Para poder trabalhar na entry
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100000 #Os 0 do são o número de caracteres

    def validarNum(self, text): #Limite de 9 caracteres
        if text == '':
            return True #Para poder trabalhar na entry
        if ' ' in text:
            texto = text.replace(' ','')
            if texto.isnumeric():
                return True
            else:
                return False
        else:
            if text.isnumeric():
                return True
            else:
                return False
        


    def validaLetra(self, text):
        if text == '':
            return True
        if ' ' in text:
            texto = text.replace(' ','')
            if texto.isalpha():
                return True
            else:
                return False
        else:
            if text.isalpha():
                return True
            else:
                return False
        
        
###### Função pra validar as entradas ######### 

def valida_entrada(self):
    self.val_entry2 = (self.janela.register(self.validar_entry2),'%P')
    self.val_entryNum = (self.janela.register(self.validarNum),'%P')
    self.val_entryLet = (self.janela.register(self.validaLetra),'%P')
        
#######   Função pro número do telefone já sair bonitinho, mas não deu certo tenho que ver ainda #####
def validaTel(self, padrao, tel, validarNum):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'

        tel = re.search(padrao, validarNum())
        return '+{}({}){}-{}'.format(tel.group(1),  tel.group(2), tel.group(3), tel.group(4))



               ######## A gente pode pensar em algo pra botar no menu ################

#Adicionando função aos Botões[]
class Funcs():
#Função para o botão Limpar
    def limpa_tela(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_cep.delete(0, END)
        self.entry_cidade.delete(0, END)
        self.entry_nibge.delete(0, END)
        self.entry_uf.delete(0, END)
        self.entry_logradouro.delete(0, END)
        self.entry_numero.delete(0, END)
        self.entry_telefone.delete(0, END)
        
#Função para conectar o banco de dados
    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor() 
        print('Conectando ao Banco de Dados')

#Função para desconectar o banco de dados
    def desconecta_bd(self):
        self.conn.close()
        print('Desconectando o Banco de Dados')

#Função para criar o banco de dados
    def montaTabelas(self):
        self.conecta_bd()
        ###Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
             cod INTEGER PRIMARY KEY,
             nome_cliente CHAR(40) NOT NULL,
             cpf INTEGER(11) NOT NULL,
             cep INTEGER(9),
             ibge INTEGER(7),
             uf CHAR(2) NOT NULL,
             logradouro CHAR(40),
             numero INTEGER(5),
             telefone INTEGER(20),
             cidade CHAR(40)
            );
        """)
        #Validar a informação no banco de dados
        self.conn.commit(); print('Banco de Dados criado')
        #Desconectar o banco de dados
        self.desconecta_bd(); print('Banco de Dados Desconectado')

#Função que possui todas as variaveis
    def dados(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.cpf = self.entry_cpf.get()
        self.cep = self.entry_cep.get()
        self.cidade = self.entry_cidade.get()
        self.nibge = self.entry_nibge.get()
        self.uf = self.entry_uf.get()
        self.logradouro = self.entry_logradouro.get()
        self.numero = self.entry_numero.get()
        self.telefone = self.entry_telefone.get()   

#Função para adiconar dados do cliente    
    def add_cliente(self):
        self.dados()
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO clientes(nome_cliente, cpf, cep, ibge, uf, logradouro, numero, telefone, cidade)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.nome, self.cpf, self.cep, self.nibge, self.uf, self.logradouro, self.numero, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()       

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, cpf, cep, ibge, uf, logradouro, numero, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i) 
        self.desconecta_bd()   
#Função para Duplo Click
    def OnDoubleClick(self, event):  
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.listaCli.item(n, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_cpf.insert(END, col3)
            self.entry_cep.insert(END, col4)
            self.entry_cidade.insert(END, col5)
            self.entry_nibge.insert(END, col6)
            self.entry_uf.insert(END, col7)
            self.entry_logradouro.insert(END, col8)
            self.entry_numero.insert(END, col9)
            self.entry_telefone.insert(END, col10)

    def deleta_cliente(self):
        self.dados()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()

    def altera_cliente(self):
        self.dados()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, cpf = ?, cep = ?, ibge = ?, uf = ?, logradouro = ?, numero = ?, telefone = ?, cidade = ? WHERE cod = ? """, (self.nome, self.cpf, self.cep, self.nibge, self.uf, self.logradouro, self.numero, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
        
    def busca_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children()) #limpa a lista

        self.entry_nome.insert(END, '%') #Busca (% é coringa por isso coloquei aqui, pra ñ ficar digitando)
        nome = self.entry_nome.get() #Variável pra identificar o nome digitado
        self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" %nome) 
        #LIKE vai fazer a pesquisa de algo que tenha o que foi digitado, ñ somente o que foi digitado
        #Order By vai fazer a pesquisa em ordem ASC de ascendente
        busca_cliente = self.cursor.fetchall() #fecha a busca
        for i in busca_cliente:
            self.listaCli.insert('', END, values=i) #Vai inserir a pesquisa na lista
        self.limpa_tela() #Limpar as entrys
        self.desconecta_bd()   
        

class App(Funcs, Relatorios):
    def __init__(self):
        self.janela = janela
        self.tela() #chamando a funçao tela
        self.frames_tela() #chamando a funçao frames tela
        self.widgets_frame1() #chamando a funçao widgets tela
        self.lista_frame2() #chamando a tabela Clientes
        self.montaTabelas() #chamando a função monta tabelas
        self.select_lista() #chamando para atualizar a lista com o clientes cadastrados
        self.menus() #chamando a função mostrar Menu
        janela.mainloop()

    def tela(self):
        self.janela.title('Cadastro de Clientes') #titulo
        self.janela.configure(background='#1e3743') #Cor de fundo
        self.janela.geometry('1000x800') #tamanho da tela
        self.janela.resizable(True, True) #tamanho ajustável
        self.janela.maxsize(width=1100, height=900) #tamanho máximo
        self.janela.minsize(width=500, height=400) #tamanho mínimo

    def frames_tela(self):
        #Criando o Frame 1
        self.frame_1 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        
        #Criando o frame 2
        self.frame_2 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)    
      
    def widgets_frame1(self):
    ##Criando Botões##  
        #Criando o Botão Limpar
        self.btn_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'), command = self.limpa_tela)
        self.btn_limpar.place(relx=0.8, rely=0.25, relwidth=0.1, relheight=0.15)

        #Criando o Botão Buscar
        self.btn_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'))
        self.btn_buscar.place(relx=0.7, rely=0.25, relwidth=0.1, relheight=0.15)

        #Criando o Botão Salvar
        self.btn_salvar = Button(self.frame_1, text='SALVAR', bd=2, bg='#00FF7F', fg='white',
                                font=('verdana', 8, 'bold'), command = self.add_cliente)
                                
        self.btn_salvar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        #Criando o Botão Alterar
        self.btn_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#107db2', fg='white',
                                 font=('verdana', 8, 'bold'), command = self.altera_cliente)
        self.btn_alterar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        #Criando o Botão Deletar
        self.btn_deletar = Button(self.frame_1, text='DELETAR', bd=2, bg='#DC143C', fg='white',
                                font=('verdana', 8, 'bold'), command = self.deleta_cliente)
        self.btn_deletar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

    ##Criando Labels e Entrys##       
        #Criando Label e Entry Código
        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.0455, rely=0.13)

        self.entry_codigo = Entry(self.frame_1)
        self.entry_codigo.place(relx=0.05, rely=0.20, relwidth=0.08)

        #Criando Label e Entry Nome
        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.27)

        self.entry_nome = Entry(self.frame_1)
        self.entry_nome.place(relx=0.05, rely=0.34, relwidth=0.3)

        #Criando Label e Entry Nome
        self.lb_cpf = Label(self.frame_1, text='CPF', bg='#dfe3ee', fg='#107db2')
        self.lb_cpf.place(relx=0.38, rely=0.27)

        self.entry_cpf = Entry(self.frame_1)
        self.entry_cpf.place(relx=0.38, rely=0.34, relwidth=0.2)

        #Criando Label e Entry CEP
        self.lb_cep = Label(self.frame_1, text='CEP', bg='#dfe3ee', fg='#107db2')
        self.lb_cep.place(relx=0.05, rely=0.41)

        self.entry_cep = Entry(self.frame_1)
        self.entry_cep.place(relx=0.05, rely=0.47, relwidth=0.1)

        #Criando Label e Entry Cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.18, rely=0.41)

        self.entry_cidade = Entry(self.frame_1)
        self.entry_cidade.place(relx=0.18, rely=0.47, relwidth=0.25)
       
        #Criando Label e Entry N° IBGE
        self.lb_nibge = Label(self.frame_1, text='IBGE', bg='#dfe3ee', fg='#107db2')
        self.lb_nibge.place(relx=0.46, rely=0.41)

        self.entry_nibge = Entry(self.frame_1)
        self.entry_nibge.place(relx=0.46, rely=0.47, relwidth=0.08)

        #Criando Label e Entry Unidade Federativa
        self.lb_uf = Label(self.frame_1, text='UF', bg='#dfe3ee', fg='#107db2')
        self.lb_uf.place(relx=0.57, rely=0.41)

        self.entry_uf = Entry(self.frame_1)
        self.entry_uf.place(relx=0.57, rely=0.47, relwidth=0.04)
        
        #Criando Label e Entry Logradouro
        self.lb_logradouro = Label(self.frame_1, text='Logradouro', bg='#dfe3ee', fg='#107db2')
        self.lb_logradouro.place(relx=0.05, rely=0.56)

        self.entry_logradouro = Entry(self.frame_1)
        self.entry_logradouro.place(relx=0.05, rely=0.63, relwidth=0.3)

        #Criando Label e Entry Número
        self.lb_numero = Label(self.frame_1, text='Número', bg='#dfe3ee', fg='#107db2')
        self.lb_numero.place(relx=0.38, rely=0.56)

        self.entry_numero = Entry(self.frame_1)
        self.entry_numero.place(relx=0.38, rely=0.63, relwidth=0.1)        

        #Criando Label e Entry Telefone
        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.51, rely=0.56)

        self.entry_telefone = Entry(self.frame_1)
        self.entry_telefone.place(relx=0.51, rely=0.63, relwidth=0.2)

    def lista_frame2(self):
    ##Criando a tabela Clientes    
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Código')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='CPF')
        self.listaCli.heading('#4', text='CEP')
        self.listaCli.heading('#5', text='Cidade')
        self.listaCli.heading('#6', text='IBGE')
        self.listaCli.heading('#7', text='UF')
        self.listaCli.heading('#8', text='Logradouro')
        self.listaCli.heading('#9', text='Número')
        self.listaCli.heading('#10', text='Telefone')

        self.listaCli.column('#0', width=0)
        self.listaCli.column('#1', width=45)
        self.listaCli.column('#2', width=150)
        self.listaCli.column('#3', width=90)
        self.listaCli.column('#4', width=90)
        self.listaCli.column('#5', width=80)
        self.listaCli.column('#6', width=70)
        self.listaCli.column('#7', width=50)
        self.listaCli.column('#8', width=125)
        self.listaCli.column('#9', width=50)
        self.listaCli.column('#10', width=100)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        #criando Barra de rolagem
        self.scrolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrolLista.set)
        self.scrolLista.place(relx=0.96, rely=0.1, relwidth=0.025, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
        style=ttk.Style(janela)
        style.theme_use('clam')
        
    #Criando a barra com menu de opções
    def menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        menu1 = Menu(menubar)
        menu2 = Menu(menubar)

        def Quit(): self.janela.destroy()

        menubar.add_cascade(label= "Opções", menu = menu1)
        menubar.add_cascade(label= "Relatorios", menu = menu2)

        menu1.add_command(label= "Sair", command = Quit)
        menu1.add_command(label= "Limpa Cliente", command = self.limpa_tela)
        
        menu2.add_command(label= "Clientes", command = self.gerarRelatorio)
App()