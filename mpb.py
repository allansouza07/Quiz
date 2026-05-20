def quizmpb():
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