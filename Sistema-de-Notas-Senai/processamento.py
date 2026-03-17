def calcular_media(notas):

    if len(notas) == 0:
        return 0
    
    soma = 0

    for n in notas:
        soma += n
    return soma / len(notas)

def alunos_recuperacao(alunos):

    recuperacao = []

    for nome, notas in alunos:

        if len(notas) == 0:
            continue

        media = calcular_media(notas)

        if media < 7:
            recuperacao.append((nome, media))
    return recuperacao

def top_student(alunos):
    top = None

    for nome, notas in alunos:
        if len(notas) == 0:
            continue

        media = calcular_media(notas)

        if top is None or media > top[1]:
            top = (nome, media)

    return top