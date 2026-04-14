#RAP
print("Ola")
def rap ():
    rap = [{"Nome:":"Racionais MC's", "Primeiro Album":"Raio-X do Brasil", "integrantes:": "Mano Brown, Edi Rock, Kl Jay e Ice Blue","Música acidente:": "A vítima"}, {"Nome:":"BK", "Nome verdadeiro":"Abebe Bikila", "Último projeto lançado":"Produto do ambiente","C&R":"Castelos e Ruínas"}]
    pontos = 0

    escolha_rap = int(input("Escolha um desses artistas nacionais: \n [1]:Racionais MC's \n [2]:BK \n [3]Djonga \n Resposta: "))
    print()
    print(f"Você selecionou {rap[escolha_rap -1]["Nome:"]}")
    print("Vamos começar as perguntas!")
    print()
    #RACIONAIS
    if rap[escolha_rap -1]["Nome:"] == "Racionais MC's":
        rodada1 = int(input("Qual foi o primeiro álnum dos racionais?\n [1]Sobrevivendo no Inferno \n [2]Raio-x do Brasil \n [3]Nada como um dia após o outro \n resposta: "))
        print()
        if rodada1 == 2:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input("Quem são os integrantes dos Racionais MC's? \n [1]Mano Brown, Edi Rock, Ice Blue e Kl Jay \n [2]Mano Brown, Mv Bill, Edi Rock e Ice Cube \n [3]Mauricio Brown, Edi Rap, Ice Blue e Kl Jay \n resposta"))
        print()
        if rodada2 == 1:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input("Qual a música que retrata um acidente fatal envolvendo o integrante Edi Rock? \n [1]A vítima \n [2]O acidente \n [3]Um homem na estrada\n :resposta"))
        print()
        if rodada3 == 1:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        print("FIM DO QUIZ!")
        print()
        print(f"Sua pontuação: {pontos} pontos de 3")
        if pontos == 3 :
            print("Você é um verdadeiro fã! Parabéns!")
        elif pontos >0:
            print("Dá pra ver que você possuí um conhecimento! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")
    
    elif rap[escolha_rap -1]["Nome:"] == "BK":
        rodada1 = int(input("Qual nome verdadeiro do BK? \n [1]Bruno Kennedy \n [2]Luccas Carlos \n [3]Abebe Bikila\n resposta: "))
        print()
        if rodada1 == 3:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input("Qual foi o último projeto lançado de BK? \n [1]Produto do ambiente \n [2] Diamantes, lágrimas e rostos para esquecer \n [3]Meu universo \n resposta:"))
        print()
        if rodada2 == 1:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input("Complete o nome do álbum: Castelos e ________? \n [1]Reis \n [2]Ruínas\n [3]Guerras\n resposta:"))
        print()
        if rodada3 == 1:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        print("FIM DO QUIZ!")
        print()
        print(f"Sua pontuação: {pontos} pontos de 3")
        if pontos == 3 :
            print("Você é um verdadeiro fã! Parabéns!")
        elif pontos >0:
            print("Dá pra ver que você possuí um conhecimento! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")
        




        #"Nome":"BK", "Nome verdadeiro":"Abebe Bikila", "Último projeto lançado":"Produto do ambiente","C&R":"Castelos e Ruínas"


#Escolha

def programa ():
    print()
    escolha1= int(input("Escolha um gênero musical: \n [1] Rap Brasileiro \n [2] MPB \n [3] Pagode \n [4] Pop internacional \n [5] Rock \n Resposta: "))
    if escolha1 == 1 :
        rap()

while True:    
    condicao= str(input("Quer continuar?"))
    if condicao in " s S SIM sim ":
        programa()  
    else:
        break
     

