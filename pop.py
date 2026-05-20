def quizpop():
    print()
    pagode=[{"Nome:": "Ferrugem", "cidade": "Rio de Janeiro", "Origem do apelido": "Ser ruivo","time":"Fluminense"}, {"Nome:": "Thiaguinho", "Grupo famoso":"Exaltasamba","Primeiro álbum":"Ousadia & Alegria","Turne":"Tardezinha"}, {"Nome:": "Péricles", "Saida": 2012,"time":"Corinthians", "tentei fazer valer a pena":"Até que durou"}]
    pontos = 0

    escolha_pagode = int(input("Escolha um desses artistas de pop: \n [1]: Michael Jackson \n [2]: Justin Bieber \n [3] Bruno Mars  \n Resposta: "))
    print()
    print(f"Você selecionou {pagode[escolha_pagode -1]["Nome:"]}")
    print("Vamos começar as perguntas!")
    print()

    if pagode[escolha_pagode -1]["Nome:"] == "Ferrugem":
        rodada1 = int(input("Qual o estado que Ferrugem nasceu?\n [1] São Paulo \n [2] Rio Grande do Sul \n [3] Rio de Janeiro \n resposta: "))
        print()
        if rodada1 == 3:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input("Por que o apelido Ferrugem? \n [1] Por ele ser ruivo \n [2] Por ter trabalhado de mecânico \n [3] Por ter pouca mobilidade nas pernas \n resposta: "))
        print()
        if rodada2 == 1:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input("Qual o time de Ferrugem? \n [1] Fluminense \n [2] Vasco \n [3] Botafogo \n :resposta: "))
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
            print("LARAIA LARAIAAAAA!Jogou muito, parabéns!")
        elif pontos >0:
            print("Pra matar o tempo você devora conhecimento! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")
    
    elif pagode[escolha_pagode -1]["Nome:"] == "Thiaguinho":
        rodada1 = int(input("Qual o grupo musical que Thiaguinho fazia parte entre 2003 e 2012?\n [1] Exaltasamba \n [2] Exaltapagode \n [3] Menos é Mais \n resposta: "))
        print()
        if rodada1 == 1:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input("Qual o primeiro álbum solo de Thiaguinho? \n [1] Ousadia & Alegria \n [2] Caraca,muleque! \n [3] Pagodeira \n resposta: "))
        print()
        if rodada2 == 1:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input("Qual o nome do festival famoso que Thiaguinho realiza desde 2015? \n [1] Pagode na praia \n [2] Thiaguinho e seus amigos \n [3] Tardezinha \n :resposta: "))
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
            print("CARACA, MULEQUE!Jogou muito, parabéns!")
        elif pontos >0:
            print("Foi ousado e alegre! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")


    elif pagode[escolha_pagode -1]["Nome:"] == "Péricles":
        rodada1 = int(input("Em que ano Péricles saiu do grupo Exaltasamba??\n [1] 2010 \n [2] 2012 \n [3] 2018  \n resposta: "))
        print()
        if rodada1 == 2:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input("Qual o time de Péricles? \n [1] Corinthians \n [2] Santos \n [3] São Paulo \n resposta: "))
        print()
        if rodada2 == 1:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input('"Até que durou, me diz o porquê", essa frase faz parte da música: \n [1] Final de tarde \n [2] Diz o porquê \n [3] Até que durou \n :resposta: '))
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
            print("Você fez valer a pena!Jogou muito, parabéns!")
        elif pontos >0:
            print("Isso é um sinal de boa jogada! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")