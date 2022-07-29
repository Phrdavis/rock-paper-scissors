from Modulos import *

get_dir = os.path.dirname(__file__)     #Pegando diretorio do arquivo
#Lista de cores
cores = [
    "white",    #cores[0]
    "black",    #cores[1]
    "#A9A9A9"   #cores[2]
]

#Lista de Imagens
tesoura = PhotoImage(file= fr"{get_dir}\botões\Tesoura.png")    #Diretorio da imagem
fechar = PhotoImage(file= fr"{get_dir}\botões\Fechar.png")      #Diretorio da imagem
papel = PhotoImage(file= fr"{get_dir}\botões\Papel.png")        #Diretorio da imagem
pedra = PhotoImage(file= fr"{get_dir}\botões\Pedra.png")        #Diretorio da imagem
imagem = [
    tesoura,    #imagem[0]
    fechar,     #imagem[1]
    papel,      #imagem[2]
    pedra       #imagem[3]
]

#Lista de Fontes
fonte1 = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")    #Definindo padrão de fonte
fonte1_1 = tkFont.Font(family="Arial", size=35, weight="bold")                  #Definindo padrão de fonte
fonte1_2 = tkFont.Font(family="Arial", size=20, weight="bold")                  #Definindo padrão de fonte

fontes = [
    fonte1,     #fontes[0]
    fonte1_1,   #fontes[1]
    fonte1_2    #fontes[2]
]