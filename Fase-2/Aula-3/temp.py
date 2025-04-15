
#realizar a media entre dois valores
def status_aluno(num1: float, num2: float) -> str:
    media: float
    media = (num1 + num2) / 2
    return f'Aprovado com media: {media:.2f}' if media >= 6 else f'Reprovado com media: {media:.2f}'

print(f' resultado: {status_aluno(7, 8)}')


print('teste')





