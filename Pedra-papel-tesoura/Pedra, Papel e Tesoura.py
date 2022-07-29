from Modulos import *
from Listas import *
                                
root = tk.Tk()                          #Definindo root do sistema 
root.overrideredirect(True)             #Fazendo com que a barra superior desapareça
pc = 0                                  #Variavel para numero de vitórias do computador
vc = 0                                  #Variavel para numero de vitórias do usuário

def center(win):
    win.update_idletasks()

    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    win.deiconify()

#Classe principal para interação das funções 
class Application():
    def __init__(self):         #Função init 
        self.root = root        #Definindo variavel self.root
        self.tela()             #função tela() para proporções e configurações
        self.frame()            #função frame() para definição de repartições da tela 
        self.label()            #função label() para textos dentro dos frames e da tela
        self.widgets()          #função widgets() para atribuição de botões no frame
        self.root.mainloop()    #termino do root //loop para permanência da tela

    def tesoura_command(self):                                          #função comando para opção tesoura
        global pc, vc, placar                                           #definindo variaveis globais
        self.anuncio = Label(self.frame1, bg= cores[0])                 #abrindo Label
        self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7, 
                                    relheight= 0.1, relwidth= 1)        #definindo coordenadas da Label na tela
        self.resultado = Label(self.frame1, bg= cores[0])               #abrindo Label
        self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8, 
                                    relheight= 0.1, relwidth= 1)        #definindo coordenadas da Label na tela
        #Lista de opções 
        op = [                                                          #lista de opções para pedra, papel e tesoura
            1, #Pedra   / op[0]
            2, #Papel   / op[1]    
            3  #Tesoura / op[2]
        ]
        self.random = random.choice(op) #Sistema fazendo escolha aleatória entre as opções
        
        if self.random == 1:
            self.anuncio = Label(self.frame1, text= "Poxa, não foi dessa vez :c", bg= cores[0])     #Abrindo Label
            self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7)                              #definindo coordenadas da Label na tela
            self.anuncio.configure(font= fontes[0])                                                 #Configurando fonte padrão

            self.resultado = Label(self.frame1, text= "DERROTA ;-;", bg= cores[0])                  #Abrindo Label
            self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8)                            #definindo coordenadas da Label na tela
            self.resultado.configure(font= fontes[2])                                               #Configurando fonte padrão

            pc += 1     #Contador de vitorias para o software

        elif self.random == 2:
            self.anuncio = Label(self.frame1, text= "Meu Deus, você é incrível!!!!", bg= cores[0])  #Abrindo Label
            self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7)                              #definindo coordenadas da Label na tela
            self.anuncio.configure(font= fontes[0])                                                 #Configurando fonte padrão

            self.resultado = Label(self.frame1, text= "VITÓRIAAAAA", bg= cores[0])                  #Abrindo Label
            self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8)                            #definindo coordenadas da Label na tela
            self.resultado.configure(font= fontes[2])                                               #Configurando fonte padrão

            vc += 1     #Contador de vitorias para o usuário 

        elif self.random == 3:
            self.anuncio = Label(self.frame1, text= "Hmmmm... Que pena, tente mais uma vez", bg= cores[0])#Abrindo Label
            self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7)                              #definindo coordenadas da Label na tela
            self.anuncio.configure(font= fontes[0])                                                 #Configurando fonte padrão

            self.resultado = Label(self.frame1, text= "EMPATE :/", bg= cores[0])                    #Abrindo Label
            self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8)                            #definindo coordenadas da Label na tela
            self.resultado.configure(font= fontes[2])                                               #Configurando fonte padrão


        self.placar = Label(self.frame1, text= f"Soft. {pc}x{vc} Você", bg= cores[0])               #Abrindo Label
        self.placar.place(anchor= 'center', relx= 0.5, rely= 0.9)                                   #definindo coordenadas da Label na tela
        self.placar.configure(font= fontes[0])                                                      #Configurando fonte padrão

    def pedra_command(self):                                                                        #função comando para opção pedra
        global pc, vc, placar                                                                       #definindo variaveis globais
        self.anuncio = Label(self.frame1, bg= cores[0])                                             #Abrindo Label
        self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7, relheight= 0.1, relwidth= 1)     #definindo coordenadas da Label na tela
        self.resultado = Label(self.frame1, bg= cores[0])                                           #Abrindo Label
        self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8, relheight= 0.1, relwidth= 1)   #definindo coordenadas da Label na tela
        
        #Lista de opções 
        op = [                                                                                      #lista de opções para pedra, papel e tesoura
            1, #Pedra   / op[0]
            2, #Papel   / op[1]    
            3  #Tesoura / op[2]
        ]
        self.random = random.choice(op) #Sistema fazendo escolha aleatória entre as opções
        
        if self.random == 1:
            self.anuncio = Label(self.frame1, text= "Hmmmm... Que pena, tente mais uma vez", bg= cores[0])#Abrindo Label
            self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7)                              #definindo coordenadas da Label na tela
            self.anuncio.configure(font= fontes[0])                                                 #Configurando fonte padrão

            self.resultado = Label(self.frame1, text= "EMPATE :/", bg= cores[0])                    #Abrindo Label
            self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8)                            #definindo coordenadas da Label na tela
            self.resultado.configure(font= fontes[2])                                               #Configurando fonte padrão

        elif self.random == 2:
            self.anuncio = Label(self.frame1, text= "Poxa, não foi dessa vez :c", bg= cores[0])     #Abrindo Label
            self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7)                              #definindo coordenadas da Label na tela
            self.anuncio.configure(font= fontes[0])                                                 #Configurando fonte padrão

            self.resultado = Label(self.frame1, text= "DERROTA ;-;", bg= cores[0])                  #Abrindo Label
            self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8)                            #definindo coordenadas da Label na tela
            self.resultado.configure(font= fontes[2])                                               #Configurando fonte padrão

            pc += 1     #Contador de vitorias para o software

        elif self.random == 3:
            self.anuncio = Label(self.frame1, text= "Meu Deus, você é incrível!!!!", bg= cores[0])  #Abrindo Label
            self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7)                              #definindo coordenadas da Label na tela
            self.anuncio.configure(font= fontes[0])                                                 #Configurando fonte padrão

            self.resultado = Label(self.frame1, text= "VITÓRIAAAAA", bg= cores[0])                  #Abrindo Label
            self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8)                            #definindo coordenadas da Label na tela
            self.resultado.configure(font= fontes[2])                                               #Configurando fonte padrão

            vc += 1     #Contador de vitorias para o usuário


        self.placar = Label(self.frame1, text= f"Soft. {pc}x{vc} Você", bg= cores[0])               #Abrindo Label
        self.placar.place(anchor= 'center', relx= 0.5, rely= 0.9)                                   #definindo coordenadas da Label na tela
        self.placar.configure(font= fontes[0])                                                      #Configurando fonte padrão

    def papel_command(self):                                                                        #função comando para opção tesoura
        global pc, vc, placar                                                                       #definindo variaveis globais
        self.anuncio = Label(self.frame1, bg= cores[0])                                             #Abrindo Label
        self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7, relheight= 0.1, relwidth= 1)     #definindo coordenadas da Label na tela
        self.resultado = Label(self.frame1, bg= cores[0])                                           #Abrindo Label
        self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8, relheight= 0.1, relwidth= 1)   #definindo coordenadas da Label na tela
        
        #Lista de opções 
        op = [                                                                                      #lista de opções para pedra, papel e tesoura
            1, #Pedra   / op[0]
            2, #Papel   / op[1]    
            3  #Tesoura / op[2]
        ]
        self.random = random.choice(op) #Sistema fazendo escolha aleatória entre as opções
        
        if self.random == 1:
            self.anuncio = Label(self.frame1, text= "Meu Deus, você é incrível!!!!", bg= cores[0])  #Abrindo Label
            self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7)                              #definindo coordenadas da Label na tela
            self.anuncio.configure(font= fontes[0])                                                 #Configurando fonte padrão

            self.resultado = Label(self.frame1, text= "VITÓRIAAAAA", bg= cores[0])                  #Abrindo Label
            self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8)                            #definindo coordenadas da Label na tela
            self.resultado.configure(font= fontes[2])                                               #Configurando fonte padrão

            vc += 1     #Contador de vitorias para o usuário

        elif self.random == 2:
            self.anuncio = Label(self.frame1, text= "Hmmmm... Que pena, tente mais uma vez", bg= cores[0])#Abrindo Label
            self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7)                              #definindo coordenadas da Label na tela
            self.anuncio.configure(font= fontes[0])                                                 #Configurando fonte padrão

            self.resultado = Label(self.frame1, text= "EMPATE :/", bg= cores[0])                    #Abrindo Label
            self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8)                            #definindo coordenadas da Label na tela
            self.resultado.configure(font= fontes[2])                                               #Configurando fonte padrão


        elif self.random == 3:
            self.anuncio = Label(self.frame1, text= "Poxa, não foi dessa vez :c", bg= cores[0])     #Abrindo Label
            self.anuncio.place(anchor= 'center', relx= 0.5, rely= 0.7)                              #definindo coordenadas da Label na tela
            self.anuncio.configure(font= fontes[0])                                                 #Configurando fonte padrão

            self.resultado = Label(self.frame1, text= "DERROTA ;-;", bg= cores[0])                  #Abrindo Label
            self.resultado.place(anchor= 'center', relx= 0.5, rely= 0.8)                            #definindo coordenadas da Label na tela
            self.resultado.configure(font= fontes[2])                                               #Configurando fonte padrão

            pc += 1     #Contador de vitorias para o software


        self.placar = Label(self.frame1, text= f"Soft. {pc}x{vc} Você", bg= cores[0])               #Abrindo Label
        self.placar.place(anchor= 'center', relx= 0.5, rely= 0.9)                                   #definindo coordenadas da Label na tela
        self.placar.configure(font= fontes[0])                                                      #Configurando fonte padrão

    #Função para tela principal 
    def tela(self):                                         
        self.root.title("teste")                            #Atribuição de título a janela root
        self.root.geometry("800x600")                       #Dimensões da janela quando aberta
        self.root.configure(background= cores[2])           #Difinição de cores de fundo 
        self.root.resizable(False, False)                   #Restringindo redimencionamento da tela

        center(self.root)                                   #Chamando função para centralizar root no meio da tela 
    
    #Função para os Frames na tela
    def frame(self):
        self.frame1 =  Frame(self.root, bd = 4, bg = cores[0])                                          #Abrindo Frame
        self.frame1.place(relx = 0.5, rely= 0.5, relwidth= 0.95, relheight= 0.95, anchor= "center")     #definindo coordenadas do frame na tela

    #Função para as Labels na tela
    def label(self):
        self.bem_vindo = Label(self.frame1, text= "Bem vindo!!", bg = cores[0])         #Abrindo Label
        self.bem_vindo.place(anchor= 'center', relx= 0.5, rely= 0.13)                   #definindo coordenadas da Label na tela
        self.bem_vindo.configure(font= fontes[1])                                       #Configurando fonte padrão

        self.selecione = Label(self.frame1, text= "Selecione abaixo:", bg = cores[0])   #Abrindo Label
        self.selecione.place(anchor= 'center', relx= 0.5, rely= 0.3)                    #definindo coordenadas da Label na tela
        self.selecione.configure(font= fontes[0])                                       #Configurando fonte padrão

    #Função para os Botões na tela
    def widgets(self):
        self.pedra = Button(self.frame1, relief= FLAT, bd = 0, image= imagem[3], command= self.pedra_command)                   #Abrindo botão
        self.pedra.place(anchor= 'center', relx= 0.25, rely= 0.5, relheight= 0.2, relwidth= 0.2)                                #definindo coordenadas do botão no frame

        self.papel = Button(self.frame1,relief= FLAT, bd= 0, image= imagem[2], command= self.papel_command)                     #Abrindo botão
        self.papel.place(anchor= 'center', relx= 0.50, rely= 0.5, relheight= 0.28, relwidth= 0.18)                              #definindo coordenadas do botão no frame

        self.tesoura = Button(self.frame1, relief=FLAT, bd= 0, bg= cores[0], image= imagem[0], command= self.tesoura_command)   #Abrindo botão
        self.tesoura.place(anchor= "center", relx= 0.75, rely= 0.5, relheight= 0.25, relwidth= 0.16)                            #definindo coordenadas do botão no frame

        self.fechar = Button(self.frame1, relief= FLAT, bd= 0, image= imagem[1], command= self.root.destroy)                    #Abrindo botão
        self.fechar.place(anchor= 'center', relx=0.95, rely= 0.05, relheight= 0.08, relwidth= 0.08)                             #definindo coordenadas do botão no frame

Application()