#RAP
print ("Ola")
def rap ():
    rap = [{"Nome:":"Racionais MC's", "Primeiro Album":"Raio-X do Brasil", "integrantes:": "Mano Brown, Edi Rock, Kl Jay e Ice Blue","Música acidente:": "A vítima"}, {"Nome:":"BK", "Nome verdadeiro":"Abebe Bikila", "Último projeto lançado":"Produto do ambiente","C&R":"Castelos e Ruínas"}, {"Nome:":"Djonga", "Nome verdadeiro":"Djonga", "Time:":"Atlético Mineiro", "Inspiração Heresia":"Milton Santos"}]

    pontos = 0
    historico =list()

    escolha_rap = int(input("Escolha um desses artistas de rap: \n [1]:Racionais MC's \n [2]:BK \n [3]Djonga \n Resposta: "))
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
        rodada2 = int(input("Quem são os integrantes dos Racionais MC's? \n [1]Mano Brown, Edi Rock, Ice Blue e Kl Jay \n [2]Mano Brown, Mv Bill, Edi Rock e Ice Cube \n [3]Mauricio Brown, Edi Rap, Ice Blue e Kl Jay \n resposta: "))
        print()
        if rodada2 == 1:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input("Qual a música que retrata um acidente fatal envolvendo o integrante Edi Rock? \n [1]A vítima \n [2]O acidente \n [3]Um homem na estrada\n :resposta: "))
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
            print("Nada como um dia após o outro sendo fã do Racionais! Parabéns!")
        elif pontos >0:
            print("Sou + você! Boa!")
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
        rodada2 = int(input("Qual foi o último projeto lançado de BK? \n [1]Produto do ambiente \n [2] Diamantes, lágrimas e rostos para esquecer \n [3]Meu universo \n resposta: "))
        print()
        if rodada2 == 1:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input("Complete o nome do álbum: Castelos e ________? \n [1]Reis \n [2]Ruínas\n [3]Guerras\n resposta: "))
        print()
        if rodada3 == 2:
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
            print("Você realmente é o líder em movimento! Parabéns!")
        elif pontos >0:
            print("Gigante(s)! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")

        
    elif rap[escolha_rap -1]["Nome:"] == "Djonga":
        rodada1 = int(input("Qual nome verdadeiro do Djonga? \n [1]Gustavo \n [2]Jefferson \n [3]Douglas\n resposta: "))
        print()
        if rodada1 == 1:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input("Qual o time de Djonga? \n [1] Atlético Mineiro \n [2] Flamengo \n [3] Grêmio \n resposta: "))
        print()
        if rodada2 == 1:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input('Em qual obra a capa do álbum "Heresia" foi inspirada? \n [1] "Coisa de acender" de Djavan \n [2] "O descobridor dos sete mares" de Tim Maia \n [3]"Clube da esquina" de Milton Nascimento\n resposta: '))
        print()
        if rodada3 == 3:
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
            print("Dono do quiz! Parabéns por acertar tudo!")
        elif pontos >0:
            print("O raio cai mais de 1 vez no mesmo lugar! Boa!")
        elif pontos==0:
            print("Não desanime! Vamos lá!")   
    


        #"Nome":"BK", "Nome verdadeiro":"Abebe Bikila", "Último projeto lançado":"Produto do ambiente","C&R":"Castelos e Ruínas"
def mpb():
    print()
    mpb=[{"Nome:": "Djavan", "Idade": 77, "Eu te": "Devoro","Ultimo album":"improviso"}, {"Nome:": "Chico Buarque", "Época":"Ditadura militar","Time":"Fluminense","Agora eu era héroi":"João e Maria"}, {"Nome:": "Belchior", "Línguas":"Inglês, francês, espanhol, italiano e latim","morte":"aneurisma de aorta", "cidade-natal":"Sobral, Ceara"}]
    pontos = 0

    escolha_mpb = int(input("Escolha um desses artistas de MPB: \n [1]: Djavan \n [2]: Chico Buarque \n [3] Belchior \n Resposta: "))
    print()
    print(f"Você selecionou {mpb[escolha_mpb -1]["Nome:"]}")
    print("Vamos começar as perguntas!")
    print()

    if mpb[escolha_mpb -1]["Nome:"] == "Djavan":
        rodada1 = int(input("Qual a idade de Djavan?\n [1] 70 anos de idade \n [2] 77 anos de idade \n [3] 83 anos de idade \n resposta: "))
        print()
        if rodada1 == 2:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input("Complete o nome da música: Eu te ________ ? \n [1] Adoro \n [2] Controlo \n [3] Devoro \n resposta: "))
        print()
        if rodada2 == 3:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input("Qual foi o último álbum de Djavan? \n [1] Improviso \n [2] Imprevistos \n [3] Esquinas \n :resposta: "))
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
            print("Seus sinais não me confundem da cabeça aos pés pois eu sei que você mandou muito bem! Parabéns!")
        elif pontos >0:
            print("Um conhecimento puro! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")
    
    elif mpb[escolha_mpb -1]["Nome:"]== "Chico Buarque":
        rodada1 = int(input("Em qual época do Brasil Chico Buarque foi amplamente perseguido, tendo que sair do Brasil? \n [1]Chegada da família real no Brasil \n [2]Era Vargas \n [3]Ditadura militar \n resposta: "))
        if rodada1 == 3:
            pontos += 1
            print()
            print("Correto! Um ponto!")
            print()
        else:
            print()
            print("Não foi dessa vez!")
            print()
        rodada2= int(input("Qual time Chico Buarque torce? \n [1]Fluminense \n [2]Corinthians \n [3]Internacional\n resposta: "))
        if rodada2 == 1:
            pontos += 1
            print()
            print("Parabéns! Ponto!")
            print()
        else:
            print()
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input('"Agora eu era héroi, e meu cavalo só falava inglês...", esse trecho faz parte da música: \n [1]Meu cavalinho \n [2]João e Maria \n [3]Cotidiano \n Resposta: '))
        if rodada3 == 2:
            pontos += 1
            print()
            print("Muito bem! Ponto!")
            print()
        else:
            print()
            print("Não foi dessa vez!")
        print("FIM DO QUIZ!")
        print()
        print(f"Sua pontuação: {pontos} pontos de 3")
        if pontos == 3 :
            print("Vencer faz parte do seu cotidiano. Parabés pelo desempenho!")
        elif pontos >0:
            print("Meu cavalo só falava inglês, já você fala a língua do conhecimento! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")
    
    elif mpb[escolha_mpb -1]["Nome:"]=="Belchior":
        rodada1=int(input("Além do português, quais línguas Belchior falava? \n [1]Inglês, francês, espanhol, italiano e latim \n [2]Inglês e japonês \n [3]Inglês, Francês, Japonês, espanhol e italiano\n Resposta: "))
        if rodada1 == 1:
            pontos += 1
            print()
            print("Parabéns. Ganhou um ponto!")
            print()
        else:
            print()
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input("Qual foi a causa da morte de Belchior? \n [1]aneurisma de aorta \n [2]Envelhecimento \n [3]Cancêr de pâncreas \n Resposta: "))
        if rodada2 == 1:
            pontos +=1
            print()
            print("Boa, ganhou um ponto!")
            print()
        else:
            print()
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input("Qual cidade Belchior nasceu? \n [1]Macaé, Rio de Janeiro \n [2]Sobral, Ceará \n [3]Feira de Santana, Bahia \n Resposta: "))
        if rodada3 ==2:
            pontos+=1
            print()
            print("Boa, um ponto garantido")
            print()
        else:
            print()
            print("Não foi dessa vez")
            print()
        print("FIM DO QUIZ!")
        print()
        print(f"Sua pontuação: {pontos} pontos de 3")
        if pontos == 3 :
            print("Não é sujeito de sorte, e sim um sujeito muito inteligente! Mandou bem demais!")
        elif pontos >0:
            print("Belchior ficaria orgulhoso! Parabéns!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")
        
#Escolha

def programa ():
    print()
    escolha1= int(input("Escolha um gênero musical: \n [1] Rap Brasileiro \n [2] MPB \n [3] Pagode \n [4] Pop internacional \n [5] Rock \n Resposta: "))
    historico1 = list()

    if escolha1 == 1 :
        rap()
        
    elif escolha1 ==2:
        mpb()
    

programa()
while True:    
    condicao= str(input("Quer continuar?"))
    if condicao in " s S SIM sim ":
        programa()  
    else:
        break



