from tkinter import *
from tkinter import messagebox
import banco

def bt_Sair():
    login.destroy()

def criar_Cadastro():
    #Formulario de Registro
    cadastrar.place(x=1000)
    entrar.place(x=1000)
    
    estado.place(x=50, y=175)
    estado_entry.place(x=100, y=200)
    
    usuario.place(x=50, y=75)
    usuario_entry.place(x=50, y=100)
    
    senha.place(x=50, y=125)
    senha_entry.place(x=50, y=150)
    
    nome.place(x=50, y=50)
    nome_entry.place(x=100, y=50)
    
    #Base para o SQLite
    criarcad.place(x=100, y=150)
    retornar.place(x=100, y=180)

def retornar_login():
    #Retorna o necessario
    usuario.place(x=100, y=50)
    usuario_entry.place(x=80, y=75)
    
    senha.place(x=110, y=100)
    senha_entry.place(x=80, y=125)
    
    cadastrar.place(x=148, y=160)
    
    retornar.place(x=500)
    
    entrar.place(x=55, y=160)
    
    #Remover o desnecessario
    nome_entry.place(x=500)
    
    nome.place(x=500)
    
    estado_entry.place(x=500)
    estado.place(x=500)
    
    criarcad.place(x=500)

def registrar_Cadastro():
    #Pegar informações para o Banco
    NomeBanco = nome_entry.get()
    UsuarioBanco = usuario_entry.get()
    SenhaBanco = senha_entry.get()
    EstadoBanco = estado_entry.get()

    if(NomeBanco == "" and UsuarioBanco == "" and SenhaBanco == "" and EstadoBanco == ""):
        messagebox.showerror(title="Erro de Registro", message="Preencha todos os Campos")
    else:
        # Inserir no Banco
        banco.cursor.execute("""
        INSERT INTO Users(Nome, Usuario, Senha, Estado) VALUES(?, ?, ?, ?)
        """,(NomeBanco, UsuarioBanco, SenhaBanco, EstadoBanco))
        banco.conn.commit()
        messagebox.showinfo(title="Register Info", message="Conta criada com sucesso")

def acessando_Login():
    EmailLogin = usuario_entry.get()
    SenhaLogin = senha_entry.get()

    banco.cursor.execute("""
    SELECT * FROM Users
    WHERE Usuario = ? AND Senha = ?
    """,(EmailLogin, SenhaLogin))
    VerificarLogin = banco.cursor.fetchone()
    try:
        if(EmailLogin in VerificarLogin and SenhaLogin in VerificarLogin):
            messagebox.showinfo(title="Login", message="Seja Bem-vindo!")
    except:
        messagebox.showinfo(title="Login", message="Usuario ou senha incorretos! ")


login = Tk()

corDeFundo= '#0d1e24'
login.title('LOGIN')
login["bg"] = corDeFundo
login.geometry("290x300+900+300")
login.resizable(width=False, height=False)
login.iconbitmap(default="Icones_Imagens/icone.ico")

image = PhotoImage(file="Icones_Imagens/imagelogin.png")
img = Label(login, image=image, bg='#0d1e24')
img.place(x=110, y=205)

title = Label(login, text='LOGIN', bg=corDeFundo, foreground='white', font=('arial', 18, 'bold'))
title.pack(side=TOP, fill=X)

usuario = Label(login, text='Usuario', bg=corDeFundo, foreground='white', font=('arial', 14, 'bold'))
usuario.place(x=100, y=50)
usuario_entry = Entry(login)
usuario_entry.place(x=80, y=75)

senha = Label(login, text='Senha', bg=corDeFundo, foreground='white', font=('arial', 14, 'bold'))
senha.place(x=110, y=100)
senha_entry = Entry(login, show="•")
senha_entry.place(x=80, y=125)

entrar = Button(login, width='10', text='ENTRAR', command=acessando_Login)
entrar.place(x=55, y=160)

cadastrar = Button(login, width='10', text='CADASTRAR', command=criar_Cadastro)
cadastrar.place(x=148, y=160)

criarcad = Button(login, width='15', text='Criar Conta', command=registrar_Cadastro)
retornar = Button(login, width='15', text='Voltar', command=retornar_login)
estado = Label(login, text='Estado:', bg='#0d1e24', foreground='white', font=('arial', 14, 'bold'))
nome = Label(login, text='Nome:', bg='#0d1e24', foreground='white', font=('arial', 14, 'bold'))
estado_entry = Entry(login)
nome_entry = Entry(login)

login.mainloop()