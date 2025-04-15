''''
calcular o valor percentual podendo ser acrescido, descontado ou apenas o valor final.
'''
from typing import Dict

# delcarar operações
operacao: Dict[str, str] = {
    'a': 'Acréscimo',
    'd': 'Desconto',
    'p': 'Percentual'
}
#BEGIN---------------------BLOCO DE CÓDIGO REPETIDO, CRIAR UMA FUNÇÃO PARA LER O TIPO FLOAT
#ler valor informado pelo usuario 
while True:
    try:
        valor = float(input('Digite o valor para calcular: '))
        break
    except ValueError:
        print('Valor incorreto, tente novamente.')
        continue

#ler valor percentual informado pelo usuario
while True:
    try:
        percentual = float(input('Digite o valor percentual: '))
        break
    except ValueError:
        print('Valor incorreto, tente novamente.')
        continue
#END---------------------BLOCO DE CÓDIGO REPETIDO, CRIAR UMA FUNÇÃO PARA LER O TIPO FLOAT

#ler o tipo de operação informado pelo usuario
while True:
    try:
        tipo = str(input(f"Digite a letra correspondete ao calculo que deseja:\n"
                         f"(a) {operacao.get('a')} | (d) {operacao.get('d')} | (p) {operacao.get('p')} \n").lower())
        if operacao.get(tipo) == None:
            print('Valor incorreto, tente novamente.')
            continue
        else:
            break
    except ValueError:
        print('Valor incorreto, tente novamente.')
        continue

#função para calcular os valores informados
def calcular_valor(valor, percentual: float, tipo: str) -> float:
    def fator (tipo: str, percentual: float) -> float:
        match tipo:
            case 'a':
                return 1 + percentual / 100
            case 'd':
                return 1 - percentual / 100
            case 'p':
                return percentual / 100
    return valor * fator(tipo, percentual)

#escreve para o usuários os resultados
print(f'O {operacao.get(tipo)} de {percentual:.1f}% sobre {valor} é: {calcular_valor(valor, percentual, tipo)}')


