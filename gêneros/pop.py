def quizpop():
    print()
    pop=[{"Nome:": "Michael", "banda": "Jackson five", "Doença": "Vitiligo","chipanzé":"Bubbles"}, {"Nome:": "Justin Bieber", "nascimento":"London,Canada","primeiro hit":"Baby","conjuge":"Hailey Bieber"}, {"Nome:": "Bruno Mars", "Primeiro e ultimo album": "Doo-woops & Hooligans e The romantic","Die with a smile":"Lady Gaga", "filho perdido":"Michael Jackson"}]
    pontos = 0
    while True:
        try:
            escolha_pop = int(input("\033[33mEscolha um desses artistas de pop: \033[m\n [1]: Michael Jackson \n [2]: Justin Bieber \n [3] Bruno Mars  \n Resposta: "))   
        except:
            print("\033[31mdigite um número entre 1 e 3!\033[m")
            continue
        else:
            print()
            print(f"Você selecionou {pop[escolha_pop -1]["Nome:"]}")
            print("Vamos começar as perguntas!")
            print()
            break

    if pop[escolha_pop -1]["Nome:"] == "Michael":
        rodada1 = int(input("Qual nome da banda formada pelos irmãos de Michael, em que ele era o vocalista principal?\n [1] The Jacksons \n [2] The Jackson Five \n [3] Michael & the Jackson \n resposta: "))
        print()
        if rodada1 == 2:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez\033[m")
            print()
        rodada2 = int(input("Qual nome da doença de Michael, que influenciou na sua mudança de cor de pele? \n [1] Melasma \n [2] Albinismo \n [3] Vitiligo \n resposta: "))
        print()
        if rodada2 == 2:
            pontos+=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez\033[m")
            print()
        rodada3 = int(input("Qual o nome do famoso chipanzé de Michael? \n [1] Bubbles \n [2] Kong \n [3] Billie \n :resposta: "))
        print()
        if rodada3 == 1:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez\033[m")
            print()
        print("FIM DO QUIZ!")
        print()
        print(f"\033[34mSua pontuação: {pontos} pontos de 3\033[m")
        if pontos == 3 :
            print("HIHIIIII! Boa!")
        elif pontos >1:
            print("Você é tão lendário quanto Michael! Excelente")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")
    
    elif pop[escolha_pop -1]["Nome:"] == "Justin Bieber":
        rodada1 = int(input("Qual a cidade em que Justin nasceu?\n [1] London, Canadá \n [2] Ottawa, Canadá \n [3] New Jersey, EUA \n resposta: "))
        print()
        if rodada1 == 1:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez\033[m")
            print()
        rodada2 = int(input("Qual o primeiro hit internacional de Justin? \n [1] Beaty and a Beast \n [2] Sorry \n [3] Baby \n resposta: "))
        print()
        if rodada2 == 3:
            pontos+=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez\033[m")
            print()
        rodada3 = int(input("Qual o nome da cônjuge de Justin? \n [1] Hailey \n [2] Selena \n [3] Mary \n :resposta: "))
        print()
        if rodada3 == 1:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez\033[m")
            print()
        print("FIM DO QUIZ!")
        print()
        print(f"\033[34mSua pontuação: {pontos} pontos de 3\033[m")
        if pontos == 3 :
            print("Você, nesse quiz, foi tão genial quanto Michael, HIHI! Boa!")
        elif pontos >1:
            print("Rusbé! Que atuação sua, ein! Excelente!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")


    elif pop[escolha_pop -1]["Nome:"] == "Bruno Mars":
        rodada1 = int(input("Qual o primeiro e último álbum de Bruno?\n [1] An evening with Silk Sonic e Doo-woop & Hooligans  \n [2] Unorthodox Jukebox e The Romantic  \n [3] Doo-woop & Hooligans e The Romantic \n resposta: "))
        print()
        if rodada1 == 3:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez\033[m")
            print()
        rodada2 = int(input('Qual artista Bruno Mars colaborou no hit "Die With a Smile"? \n [1] Madonna \n [2] Lady Gaga \n [3] Adele \n resposta: '))
        print()
        if rodada2 == 2:
            pontos+=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez\033[m")
            print()
        rodada3 = int(input("De qual artista fãs dizem que Bruno Mars é um possível filho perdido? \n [1] Prince \n [2] Lionel Richie \n [3] Michal Jackson \n :resposta: "))
        print()
        if rodada3 == 3:
            pontos +=1
            print("\033[32mCORRETO! Você ganhou um ponto!\033[m")
            print()
        else:
            print("\033[31mNão foi dessa vez\033[m")
            print()
        print("FIM DO QUIZ!")
        print()
        print(f"\033[34mSua pontuação: {pontos} pontos de 3\033[m")
        if pontos == 3 :
            print("That's What I Like! Foi bem demais!")
        elif pontos >1:
            print("Seu conhecimento se assemelha aos vocais de Bruno, ambos são inigualáveis! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")
    else:
        print("\033[31mDigite um valor entre 1 e 3\033[m")