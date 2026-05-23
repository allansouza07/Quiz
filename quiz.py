#RAP
print ("Ola")
from gêneros.rap  import quizrap
from gêneros.mpb import quizmpb
from gêneros.pagode import quizpagode
from gêneros.pop import quizpop
from gêneros.rock import quizrock

#Escolha
def programa ():
    print()    
    while True:
        try:
            escolha1= int(input("Escolha um gênero musical: \n [1] Rap Brasileiro \n [2] MPB \n [3] Pagode \n [4] Pop internacional \n [5] Rock \n Resposta: "))
        except:
            print("escolha um número de 1 a 5!")
            continue
        else:
            break
    historico1 = list()
    if escolha1 == 1 :
        quizrap()     
    elif escolha1 ==2:
        quizmpb()
    elif escolha1 ==3:
        quizpagode()
    elif escolha1 == 4:
        quizpop()
    elif escolha1 ==5:
        quizrock()
    else:
        print("opção inválida!")
programa()
while True:    
    condicao= str(input("Quer continuar? "))
    if condicao in " s S SIM sim ":
        programa()  
    else:
        break



