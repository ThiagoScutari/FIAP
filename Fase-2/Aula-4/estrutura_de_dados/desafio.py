import os
token = os.getenv("GITHUB_TOKEN")

'''
##-------------------------| PRIMEIRO SEMESTRE |---------------------------##

O aluno submete-se a três checkpoints (provas CP1, CP2 e CP3). A média dos checkpoints (MCP1Sem) equivale à média simples das duas maiores notas. O aluno participa do Challenge (projeto), que é composto de duas notas denominadas Sprint1 e Sprint2 (S1 e S2), a média dos sprints (MS1Sem) é calculada com base na média simples das notas S1 e S2. O aluno submete-se a uma prova semestral chamada Global Solution (GS1Sem).

A média do primeiro semestre (M1Sem) é calculada com a ponderação: MCP1Sem valendo 20%, MS1Sem valendo 20% e a GS1Sem valendo 60%.

Segue a fórmula:
M1Sem = (MCP1Sem . 2 + MS1Sem . 2 + GS1Sem . 6) / 10
#ler checkpoints
cp1
cp2
cp3
#calcular a media cp
descartar a menor nota e calcular a media
#ler sprints
sp1
sp2
#calcular a media sp
#ler prova sementral
gs

##-------------------------| SEGUNDO SEMESTRE |---------------------------##

O aluno se submete a três checkpoints (provas CP4, CP5 e CP6), a média dos checkpoints (MCP2Sem) equivale à média simples das duas maiores notas. O aluno participa do Challenge (projeto), que e composto de duas notas denominadas Sprint3 e Sprint4 (S3 e S4), a média dos sprints (MS2Sem) é calculada com base na média simples das notas S3 e S4. O aluno se submete a uma prova semestral chamada Global Solution (GS2Sem).

A média do segundo semestre (M2Sem) é calculada com a ponderação: MCP2Sem valendo 20%, MS2Sem valendo 20% e a GS2Sem valendo 60%.

Segue a fórmula:
M2Sem = (MCP2Sem . 2 + MS2Sem . 2 + GS2Sem . 6) / 10

##-------------------------| MEDIA ANUAL |---------------------------##

Com as M1Sem e M2Sem calculadas, agora podemos calcular a Média Anual (MA). Ela é calculada pela proporcao: M1Sem valendo 40% e M2Sem valendo 60%.

Segue a fórmula:
MA = (M1Sem . 4 + M2Sem . 6) / 10

##-------------------------| EXIBIR STATUS |---------------------------##
Uma vez calculada a Média Anual (MA), deverá exibir os Status, sendo estes como descritos a seguir:

-> Se a MA for maior ou igual a 6, o Status sera "Aprovado" (exibir juntamente com a
MA atingida).
-> Se a MA for menor do que 4, o Status sera "Reprovado" (exibir juntamente com a
MA atingida).
-> Se a MA estiver entre 4 e 5.9, o aluno poderá participar por meio do processo de
exame. Nesse caso, o programa devera pedir a Nota de Exame (NE) ao aluno e
calcular a nova Media Final (MF) considerando a media simples entre MA e NE,

logo:
Fórmula: MF= (MA + NE) / 2

##-------------------------| REQUISITOS |---------------------------##

Para desenvolver essa solução plenamente, você deve atender às seguintes informações e requisitos:
-> Todas as notas digitadas pelo usuário devem ser válidas (entre 0 e 10).
-> Caso uma nota não esteja nesse intervalo, advertir o usuário e pedir para ele digitar novamente a mesma nota.
-> Toda média calculada deve ser exibida em tela.
-> Utilize a boa prática: cada subalgoritmo dve resolver apenas um problema.
-> Ao final da execução do cálculo da média Anual, perguntar se o aluno deseja continuar executando o programa digitado [S]im ou [N]ão. A digitação do S ou N também deve ser verificada e somente essas duas letras serão aceitas.

'''
#função para ler notas
def ler_nota(mensagem: str) -> float:
    while True:
        try: 
            cp = float(input(f'{mensagem} \n'))
            if cp >= 0 and cp <= 10:
                break
            else:
                print('Valor inválido, tente novamente.')
                continue
        except ValueError:
            print('Valor inválido, tente novamente.')
            continue
    return cp

#Função para calcular a media de checkponits
def media_checkpoint(*notas) -> float:
    menor: float= notas[0]
    for nota in notas:
        if nota < menor:
            menor = nota
    return (sum(notas) - menor) / (len(notas) - 1)

#Função para calcular a media
def calcular_media(*notas) -> float:
    return sum(notas) / len(notas)

#ler notas dos checkpontis
cp1: float = ler_nota('Digite a nota para o Checkpoint 1:')
cp2: float = ler_nota('Digite a nota para o Checkpoint 2:')
cp3: float = ler_nota('Digite a nota para o Checkpoint 3:')

#ler sprints
sp1: float = ler_nota('Digite a nota para o Sprint 1:')
sp2: float = ler_nota('Digite a nota para o Sprint 2:')

#ler prova sementral
GS1Sem: float = ler_nota('Digite a nota para Global Solution:')

#calcular medias primeiro semestre
MCP1Sem: float = media_checkpoint(cp1, cp2, cp3)
MS1Sem: float = calcular_media(sp1, sp2)

M1Sem: float = ((MCP1Sem * 0.2) + (MCP1Sem * 0.2) + (MCP1Sem * 0.6)) / 10








































