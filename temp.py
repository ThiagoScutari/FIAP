vendedor: float = 23456.57
vetor: list = [1,2,3,4,5]

#print(vetor[2])

def preencher_vetor(v: list) -> None:
    print('-' * 25, 'PREENCHER VALORES', '-' * 25)
    for i in range(5):
        vetor[i] = int(input('Digite um valor: '))

def exibir_vetor(v: list) -> None:
    print('-' * 25, 'EXIBIR VALORES', '-' * 25)
    for i in vetor:
        print(i)

def somar_vetor(v: list) -> int:
    print('-' * 25, 'SOMAR VALORES', '-' * 25)
    return sum(v)


##------------------------|  PROGRMA PRINCIPAL  |------------------------##
preencher_vetor(vetor)
exibir_vetor(vetor)
print(f'a soma dos valores {vetor} é : {somar_vetor(vetor)}.')

