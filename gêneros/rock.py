def quizrock():
    print()
    rock=[{"Nome:": "Queen", "principal": "Freddie Mercury", "Origem": "Londres","Ano Bohemian":1975}, {"Nome:": "Guns", "Origem":"California","maior sucesso e álbum":"Sweet Child of Mine Appetite for destruction","guitarrista":"Slash"}, {"Nome:": "Beatles", "Motivação assassinato": "Notoriedade","Origem":"Liverpool", "Abbey road":"Integrantes cruzando uma faixa"}]
    pontos = 0

    escolha_rock = int(input("Escolha um desses artistas de rock: \n [1]: Queen \n [2]: Gun N'Roses \n [3] The Beatles  \n Resposta: "))
    print()
    print(f"Você selecionou {rock[escolha_rock -1]["Nome:"]}")
    print("Vamos começar as perguntas!")
    print()

    if rock[escolha_rock -1]["Nome:"] == "Queen":
        rodada1 = int(input("Qual nome do principal vocalista da banda Queen?\n [1] Edi Rogers \n [2] Brian May \n [3] Freddie Mercury \n resposta: "))
        print()
        if rodada1 == 3:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input("Qual a origem da banda? \n [1] Londres, Inglaterra \n [2] Nova Iorque, EUA \n [3] Sidney, Autrália \n resposta: "))
        print()
        if rodada2 == 1:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input("Em que ano foi lançada a aclamada música Bohemian Rhapsody? \n [1] 1970 \n [2] 1971 \n [3] 1975 \n :resposta: "))
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
            print("MAMAAAAAAAAA UHUUUUUU!!! Que baita desempenho, fera!")
        elif pontos >1:
            print("Se você fosse uma música do Queen, seria Don´t Stop Me Now. Ninguém te para!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")
    
    elif rock[escolha_rock -1]["Nome:"] == "Guns":
        rodada1 = int(input("Qual a origem de Guns N'Roses?\n [1] California, EUA \n [2] Manchester, Inglaterra \n [3] Glasgow, Escócia \n resposta: "))
        print()
        if rodada1 == 1:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input("Qual e de que álbum é a música mais famosa da banda? \n [1] Welcome to the Jungle, de Use your ilusion \n [2] Sweet Child O'Mine, de appetite for destruction \n [3] November Rain, de Appetite for destruction \n resposta: "))
        print()
        if rodada2 == 3:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input("Qual o nome do guitarrista da banda? \n [1] Josh \n [2] Slash \n [3] Freddie \n :resposta: "))
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
            print("OOHH sweet taste of victory! A letra foi modificada para celebrar seu desempenho, como foi bem!")
        elif pontos >1:
            print("Mais impactante que o solo do Slash! Boa!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")


    elif rock[escolha_rock -1]["Nome:"] == "Beatles":
        rodada1 = int(input("Qual foi a motivação do assassino de John Lennon ao matá-lo?\n [1] John Lennon devia dinheiro a ele  \n [2] Ele queria ser mundialmente conhecido  \n [3] Ele recebeu uma quantia milionária de dinheiro para assassinar John \n resposta: "))
        print()
        if rodada1 == 2:
            pontos +=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada2 = int(input('Qual a origem dos Beatles? \n [1] Liverpool, Inglaterra \n [2] Londres, Inglattera \n [3] Nottingham, Inglaterra \n resposta: '))
        print()
        if rodada2 == 1:
            pontos+=1
            print("CORRETO! Você ganhou um ponto!")
            print()
        else:
            print("Não foi dessa vez!")
            print()
        rodada3 = int(input('Como é a capa do famoso álbum "Abbey Road"? \n [1] Os integrantes reunidos usando ternos brancos e gravatas borboletas \n [2] Os integrantes representados em formato de desenhos animados, deitados na grama de um parque \n [3] Os integrantes atravessando uma faixa de pedestres de uma avenida \n :resposta: '))
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
            print("Quem é mais lendário, você ou Beatles? Que pergunta difícil. Boa!")
        elif pontos >1:
            print("Hey Jude, olha só como esse cara é inteligente! Excelente!")
        elif pontos==0:
            print("Estude mais sobre o artista e talvez você possa melhorar! Vamos lá!")