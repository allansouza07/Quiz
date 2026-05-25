def quizrap ():
    rap = [{"Nome:":"Racionais MC's", "Primeiro Album":"Raio-X do Brasil", "integrantes:": "Mano Brown, Edi Rock, Kl Jay e Ice Blue","Música acidente:": "A vítima"}, {"Nome:":"BK", "Nome verdadeiro":"Abebe Bikila", "Último projeto lançado":"Produto do ambiente","C&R":"Castelos e Ruínas"}, {"Nome:":"Djonga", "Nome verdadeiro":"Djonga", "Time:":"Atlético Mineiro", "Inspiração Heresia":"Milton Santos"}]

    pontos = 0
    

    while True:
        try:
            print()
            escolha_rap = int(input("\033[33mEscolha um desses artistas de rap: \033[m \n [1]:Racionais MC's \n [2]:BK \n [3]Djonga \n Resposta: "))
        except:
            print("\033[31mdigite um número entre 1 e 3!\033[m")
            continue
        else:
            print()
            print(f"\033[33mVocê selecionou {rap[escolha_rap -1]["Nome:"]}\033[m")
            print("Vamos começar as perguntas!")
            print()
            break
    #RACIONAIS
    if rap[escolha_rap -1]["Nome:"] == "Racionais MC's":
        rodada1 = int(input("Qual foi o primeiro álnum dos racionais?\n [1]Sobrevivendo no Inferno \n [2]Raio-x do Brasil \n [3]Nada como um dia após o outro \n resposta: "))
        print()
        if rodada1 == 2:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez!\033[m")
            print()
        rodada2 = int(input("Quem são os integrantes dos Racionais MC's? \n [1]Mano Brown, Edi Rock, Ice Blue e Kl Jay \n [2]Mano Brown, Mv Bill, Edi Rock e Ice Cube \n [3]Mauricio Brown, Edi Rap, Ice Blue e Kl Jay \n resposta: "))
        print()
        if rodada2 == 1:
            pontos+=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez!\033[m")
            print()
        rodada3 = int(input("Qual a música que retrata um acidente fatal envolvendo o integrante Edi Rock? \n [1]A vítima \n [2]O acidente \n [3]Um homem na estrada\n :resposta: "))
        print()
        if rodada3 == 1:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez!\033[m")
            print()
        print("FIM DO QUIZ!")
        print()
        print(f"\033[34mSua pontuação: {pontos} pontos de 3\033[m")
        if pontos == 3 :
            print("Nada como um dia após o outro sendo fã do Racionais! Parabéns!")
        elif pontos >1:
            print("Sou + você! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")
    
    
    elif rap[escolha_rap -1]["Nome:"] == "BK":
        rodada1 = int(input("Qual nome verdadeiro do BK? \n [1]Bruno Kennedy \n [2]Luccas Carlos \n [3]Abebe Bikila\n resposta: "))
        print()
        if rodada1 == 3:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez!\033[m")
            print()
        rodada2 = int(input("Qual foi o último projeto lançado de BK? \n [1]Produto do ambiente \n [2] Diamantes, lágrimas e rostos para esquecer \n [3]Meu universo \n resposta: "))
        print()
        if rodada2 == 1:
            pontos+=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez!\033[m")
            print()
        rodada3 = int(input("Complete o nome do álbum: Castelos e ________? \n [1]Reis \n [2]Ruínas\n [3]Guerras\n resposta: "))
        print()
        if rodada3 == 2:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez!\033[m")
            print()
        print("FIM DO QUIZ!")
        print()
        print(f"\033[34mSua pontuação: {pontos} pontos de 3\033[m")
        if pontos == 3 :
            print("Você realmente é o líder em movimento! Parabéns!")
        elif pontos >1:
            print("Gigante(s)! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")

        
    elif rap[escolha_rap -1]["Nome:"] == "Djonga":
        rodada1 = int(input("Qual nome verdadeiro do Djonga? \n [1]Gustavo \n [2]Jefferson \n [3]Douglas\n resposta: "))
        print()
        if rodada1 == 1:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez!\033[m")
            print()
        rodada2 = int(input("Qual o time de Djonga? \n [1] Atlético Mineiro \n [2] Flamengo \n [3] Grêmio \n resposta: "))
        print()
        if rodada2 == 1:
            pontos+=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez!\033[m")
            print()
        rodada3 = int(input('Em qual obra a capa do álbum "Heresia" foi inspirada? \n [1] "Coisa de acender" de Djavan \n [2] "O descobridor dos sete mares" de Tim Maia \n [3]"Clube da esquina" de Milton Nascimento\n resposta: '))
        print()
        if rodada3 == 3:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez!\033[m")
            print()
        print("FIM DO QUIZ!")
        print()
        print(f"\033[34mSua pontuação: {pontos} pontos de 3\033[m")
        if pontos == 3 :
            print("Dono do quiz! Parabéns por acertar tudo!")
        elif pontos >1:
            print("O raio cai mais de 1 vez no mesmo lugar! Boa!")
        elif pontos==0:
            print("Não desanime! Vamos lá!")   
    else:
        print("\033[31mdigite um valor entre 1 e 3!\033[m")