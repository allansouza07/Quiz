#RAP
print ("Ola")
from rap  import quizrap
from mpb import quizmpb
from pagode import quizpagode
from pop import quizpop

#Escolha
def programa ():
    print()    
    escolha1= int(input("Escolha um gênero musical: \n [1] Rap Brasileiro \n [2] MPB \n [3] Pagode \n [4] Pop internacional \n [5] Rock \n Resposta: "))
    historico1 = list()
    if escolha1 == 1 :
        quizrap()     
    elif escolha1 ==2:
        quizmpb()
    elif escolha1 ==3:
        quizpagode()
    elif escolha1 == 4:
        quizpop()
programa()
while True:    
    condicao= str(input("Quer continuar? "))
    if condicao in " s S SIM sim ":
        programa()  
    else:
        break



