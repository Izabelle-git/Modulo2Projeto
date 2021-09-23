from tkinter import *
from tkinter import messagebox
import banco

def bt_Sair():
    login.destroy()
def criar_Cadastro():
    # Formulario de Registro
    cadastrar.place(x=1000)
    entrar.place(x=1000)
    estado.place(x=50, y=125)
    estado_entry.place(x=100, y=125)
    usuario.place(x=50, y=75)
    usuario_entry.place(x=100, y=75)
    senha.place(x=50, y=100)
    senha_entry.place(x=100, y=100)
    nome.place(x=50, y=50)
    nome_entry.place(x=100, y=50)
    # Base para o SQLite
    criarcad.place(x=100, y=150)
    retornar.place(x=100, y=180)
def retornar_login():
    # Retorna o necessario
    usuario.place(x=50, y=50)
    usuario_entry.place(x=100, y=50)
    senha.place(x=50, y=75)
    senha_entry.place(x=100, y=75)
    cadastrar.place(x=143, y=150)
    cadastrar.place(x=143, y=150)
    retornar.place(x=500)
    entrar.place(x=50, y=150)
    # Remover o desnecessario
    nome_entry.place(x=500)
    nome.place(x=500)
    estado_entry.place(x=500)
    estado.place(x=500)
    criarcad.place(x=500)
def registrar_Cadastro():
    # Pegar informações para o Banco
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
        messagebox.showinfo(title="Login", message="Não te encontramos: Certifique se está cadastrado no nosso sistema. ")
login = Tk()

corDeFundo= '#0d1e24'
login.title('LOGIN')
login["bg"] = corDeFundo
login.geometry("300x300+100+100")
login.resizable(width=False, height=False)
login.iconbitmap(default="Icones_Imagens/icone.ico")

image = PhotoImage(file="Icones_Imagens/imagelogin.png")
img = Label(login, image=image, bg='#0d1e24')
img.place(x=110, y=205)

title = Label(login, text='LOGIN', bg=corDeFundo, foreground='white')
title.pack(side=TOP, fill=X)

usuario = Label(login, text='Usuario:', bg=corDeFundo, foreground='white')
usuario.place(x=50, y=50)
usuario_entry = Entry(login)
usuario_entry.place(x=100, y=50)
senha = Label(login, text='Senha:', bg=corDeFundo, foreground='white')
senha.place(x=50, y=75)
senha_entry = Entry(login, show="•")
senha_entry.place(x=100, y=75)

entrar = Button(login, width='10', text='ENTRAR', command=acessando_Login)
entrar.place(x=50, y=150)
cadastrar = Button(login, width='10', text='CADASTRAR', command=criar_Cadastro)
cadastrar.place(x=143, y=150)

criarcad = Button(login, width='15', text='CRIAR CADASTRO', command=registrar_Cadastro)
retornar = Button(login, width='15', text='RETORNAR', command=retornar_login)
estado = Label(login, text='Estado:', bg='#0d1e24', foreground='white')
nome = Label(login, text='Nome:', bg='#0d1e24', foreground='white')
estado_entry = Entry(login)
nome_entry = Entry(login)

login.mainloop()