'''
Um aluno (ALUNO1) possui 10 avaliações por ano. Com esse aluno desejamos executar as sguites operações:
1. Armazenar as notas dessas 10 avaliações em uma lista.
2. Calcular a média das notas.
3. Exibir as notas armazenadas.
4. Exibir uma nota específica.
5. Exibir a média das notas.
6. Exibir a maior nota.
7. Exibir a menor nota.
'''
import os

def menu() -> int:
    '''
    Função para exibir o menu de opções.
    '''
    print("Menu de Opções:")
    print("1. Inserir notas")
    print("2. Exibir notas")
    print("3. Exibir nota específica")
    print("4. Editar nota específica")
    print("5. deletar nota específica")
    print("6. Exibir média")
    print("7. Exibir maior nota")
    print("8. Exibir menor nota")
    print("9. Sair")
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if 1 <= opcao <= 9:
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    return opcao

def executar_opcao(opcao: int, notas: list) -> bool:
    '''
    Função para executar a opção escolhida pelo usuário.
    '''
    match opcao:
        case 1:
            ler_notas(notas)
        case 2:
            exibir_notas(notas)
        case 3:
            exibir_nota_especifica(notas)
        case 4:
            editar_nota_especifica(notas)
        case 5:
            deletar_nota_especifica(notas)
        case 6:
            exibir_media(notas)
        case 7:
            exibir_maior_nota(notas)
        case 8:
            exibir_menor_nota(notas)
        case 9:
            print("Saindo...")
            return False  # Sair do loop principal
        case _:
            print("Opção inválida. Tente novamente.")
    return True # Continuar no loop principal

# 1. Armazenar as notas dessas 10 avaliações em uma lista.
notas = []
def ler_notas(notas: list) -> None:
    '''
    Função para ler 10 notas e armazená-las em uma lista.
    '''
    notas.clear()  # Limpa notas antigas antes de registrar novas
    for i in range(10):
        while True:
            try:
                nota = float(input(f'Digite a nota {i+1}: '))
                if 0 <= nota <= 10:
                    break
                else:
                    print("Nota inválida. Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        notas.append(nota)

# 2. Exibir as notas armazenadas.
def exibir_notas(notas: list) -> None:
    '''
    Função para exibir as notas armazenadas.
    '''
    if not notas:
        print("Nenhuma nota registrada.")
        return
    print("Notas armazenadas:")
    for i, nota in enumerate(notas):
        print(f'Nota {i+1}: {nota}')

# 3. Exibir uma nota específica.
def exibir_nota_especifica(notas: list) -> None:
    '''
    Função para exibir uma nota específica.
    '''
    if not notas:
        print("Nenhuma nota registrada.")
        return
    else:
        while True:
            try:
                indice = int(input("Digite o índice da nota que deseja exibir (1 a 10): ")) - 1
                if 0 <= indice < len(notas):
                    print(f'Nota {indice+1}: {notas[indice]}')
                    break
                else:
                    print("Índice inválido. Digite um valor entre 1 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

# 4. Editar uma nota específica.
def editar_nota_especifica(notas: list) -> None:
    '''
    Função para editar nota específica.
    '''
    if not notas:
        print("Nenhuma nota registrada.")
        return
    else:
        while True:
            try:
                indice = int(input("Digite o índice da nota que deseja editar (1 a 10): ")) - 1
                if 0 <= indice < len(notas):
                    try:
                        nova_nota = float(input(f'Digite a nova nota para a nota {indice+1}: '))
                        if 0 <= nova_nota <= 10:
                            notas[indice] = nova_nota
                            print(f'Nota {indice+1} editada: {notas[indice]}')
                            break
                        else:
                            print("Nota inválida. Digite um valor entre 0 e 10.")
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")


# 5. Deletar uma nota específica.
def deletar_nota_especifica(notas: list) -> None:
    '''
    Função para deletar nota específica.
    '''
    if not notas:
        print("Nenhuma nota registrada.")
        return
    else:
        while True:
            try:
                indice = int(input("Digite o índice da nota que deseja deletar (1 a 10): ")) - 1
                if 0 <= indice < len(notas):
                    poped_nota = notas.pop(indice)
                    print(f'Nota {indice+1} deletada: {poped_nota}')
                    break
                else:
                    print("Índice inválido. Digite um valor entre 1 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")


# 6. Calcular a média das notas.
def calcular_media(notas: list) -> float:
    '''
    Função para calcular a média das notas.
    '''
    if not notas:
        print("Nenhuma nota registrada.")
        return 0.0
    else:
        return sum(notas) / len(notas)

# 6. Exibir a média das notas.
def exibir_media(notas: list) -> None:
    '''
    Função para exibir a média das notas.
    '''
    media = calcular_media(notas)
    print(f'Média das notas: {media:.2f}')

# 7. Exibir a maior nota.
def exibir_maior_nota(notas: list) -> None:
    '''
    Função para exibir a maior nota.
    '''
    if not notas:
        print("Nenhuma nota registrada.")
        return
    else:
        maior_nota = max(notas)
        print(f'Maior nota: {maior_nota}')

# 8. Exibir a menor nota.
def exibir_menor_nota(notas: list) -> None:
    '''
    Função para exibir a menor nota.
    '''
    if not notas:
        print("Nenhuma nota registrada.")
        return
    else:
        menor_nota = min(notas)
        print(f'Menor nota: {menor_nota}')

# Função principal para executar as operações
def main():
    '''
    Função principal para executar o programa.
    '''
    while True:
        print("-" * 30)
        print("Sistema de Notas do Aluno")
        print("-" * 30 + '\n')
        opcao: int = menu()
        if not executar_opcao(opcao, notas):
            break
        print('\n' + "-" * 30)  # Separador para melhor visualização entre as operações

if __name__ == "__main__":
    main()
    # O código foi estruturado em funções para facilitar a leitura e manutenção.
    # Cada função tem uma responsabilidade específica e o código principal chama essas funções na ordem desejada.


