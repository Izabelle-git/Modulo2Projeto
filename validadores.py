#Adicionando validadores nas entrys
class Validadores():

    def validar_entry2(self, text): 
        if text == '':
            return True #Para poder trabalhar na entry
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 10000 #Os 0 do são o número de caracteres

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
        



    ####### Aqui são nas Entrys Pra validar os comandos  ########

self.entry_codigo = Entry(self.frame_1, validate='key', validatecommand=self.val_entry2)
        
self.entry_nome = Entry(self.frame_1, validate='key', validatecommand=self.val_entryLet)

self.entry_telefone = Entry(self.frame_1, validate='key', validatecommand=self.val_entryNum)





         #######   Função pro número do telefone já sair bonitinho, mas não deu certo tenho que ver ainda #####
def validaTel(self, padrao, tel, validarNum):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'

        tel = re.search(padrao, validarNum())
        return '+{}({}){}-{}'.format(tel.group(1),  tel.group(2), tel.group(3), tel.group(4))



               ######## A gente pode pensar em algo pra botar no menu ################

#Função para criar menus
    def menus(self):
        menu_bar = Menu(self.janela)
        self.janela.config(menu=menu_bar)
        file_menu = Menu(menu_bar) #Primeiro menu
        file_menu2 = Menu(menu_bar) #Segundo menu
        ##Função dentro dos menus (só pode ser usada aqui) pra Sair
        def Quit(): 
            self.janela.destroy()
        #Menu em Cascata
        menu_bar.add_cascade(label= 'Opções', menu= file_menu)
        menu_bar.add_cascade(label= 'Sobre', menu= file_menu2)
        #Adicionar opções dentro do menu
        file_menu.add_command(label= 'Sair', command= Quit) #Comado Quit pra fechar a janela
        file_menu2.add_command(label= 'Limpar', command= self.limpa_tela) #Limpa a tela