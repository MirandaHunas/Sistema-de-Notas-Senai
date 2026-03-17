import processamento

alunos = [('Thiago', [10, 9, 8, 10]),
          ('Maria', [10, 10, 9, 8]),
          ('Eduarda', [3, 7, 6, 9]),
          ('Fernando', [])]

print('------- Bem vindo -------')

recuperacao = processamento.alunos_recuperacao(alunos)
top = processamento.top_student(alunos)

print('Alunos em recuperacao:')

for nome, media in recuperacao:
    print(f'{nome} - Media {media}')

print('Top Student:')

if top:
    print(f'{top[0]} - Media: {top[1]:.2f}')

else:
    print('Nenhum aluno valido, por favor tente denovo')