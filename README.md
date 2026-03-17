# Sistema de Notas - SENAI

# Requisitos

# Requisitos Funcionais (RF)

RF01: Receber uma lista de alunos com suas notas.

RF02: Calcular a média das notas de cada aluno.

RF03: Identificar alunos em recuperação (média menor que 7).

RF04: Identificar o aluno com maior média (Top Student).

RF05: Gerar um relatório final em arquivo .txt.


# Requisitos Não Funcionais (RNF)

RNF01: O sistema deve ser modularizado em dois arquivos (main.py e processamento.py).

RNF02: Utilizar listas, tuplas e estruturas de repetição.

RNF03: O código deve ser organizado e fácil de entender.


# Regras de Negócio (RN)

RN01: A média é calculada pela soma das notas dividida pela quantidade de notas.

RN02: Alunos com média menor que 7.0 estão em recuperação.

RN03: O aluno com maior média será considerado Top Student.



# Estrutura dos Dados

O sistema ultiza uma lista de tuplas:

Lista de Tuplas [("Nome", [notas])].



# Git 

O projeto esta ultizando o Git para controle

Branch principal:
    main.py

Branches:
    feat/calculo
    feat/relatorio

Após finalizar, realizarei um merge para a branch main.
