#RAP

def rap ():
    rap = [{"Nome:":"Racionais MC's", "Primeiro Album":"Raio-X do Brasil", "integrantes:": "Mano Brown, Edi Rock, Kl Jay e Ice Blue","Música acidente:": "A vítima"}]
    pontos = 0

    escolha_rap = int(input("Escolha um desses artistas nacionais: \n [1]:Racionais MC's \n [2]:BK \n [3]Djonga \n Resposta:"))
    print(f"Você selecionou {rap[escolha_rap -1]["Nome:"]}")
    print("Vamos começar as perguntas!")
    print()
    #RACIONAIS
    if rap[escolha_rap -1]["Nome:"] == "Racionais MC's":
        rodada1 = int(input("Qual foi o primeiro álnum dos racionais?\n [1]Sobrevivendo no Inferno \n [2]Raio-x do Brasil \n [3]Nada como um dia após o outro \n resposta: "))
        if rodada1 == 2:
            pontos +=1
            print("voce ganhou um ponto!")
        else:
            print("Não foi dessa vez!")
        rodada2 =


#Escolha
def programa ():
    escolha1= int(input("Escolha um gênero musical: \n [1] Rap Brasileiro \n [2] MPB \n [3] Pagode \n [4] Pop internacional \n [5] Rock \n Resposta: "))
    if escolha1 == 1 :
        rap()

programa()
