registrar = {}
databese = []

while True:
    registrar['Matricula'] = int(input("Numero registro aluno: "))
    registrar['Nome'] = str(input("Digite o nome do aluno: "))
    registrar['Sexo'] = str(input("Qual o sexo [F/M]: ")).upper().split()[0]
    while registrar['Sexo'] not in 'FM':
        print('\nValor Inválido!\nTente novamente...')
        registrar['Sexo'] = str(input("\nSexo do aluno [F/M]: ")).upper().split()[0]
    registrar['Idade'] = int(input("Idade do aluno: "))
    option = str(input('Deseja continuar [Y/N] ? ')).upper().split()[0]
    databese.append(registrar.copy())
    registrar.clear()
    while option not in 'YN':
        print('\nValor inválido!\nTente novamente...')
        option = str(input('Deseja continuar [Y/N] ?')).upper().split()[0]
    if option == 'N':
        break

print(f'\n\n|{"MATRICULA"}    |   {"NOME":}     |  {"SEXO"}  |   {"IDADE"}')
print('_________________________________________________')


list = sorted(databese, key=lambda k: k['Matricula']) 

for i in list:
    for a, v in i.items():
        if a == 'Matricula':
            print(f'| {v:^12}', end='|')
        if a == 'Nome':
            print(f'{v:^12}', end='|')
        if a == 'Sexo':
            print(f'{v:^12}', end='|')
        if a == 'Idade':
            print(f'{v:^12}', end='|\n')
print('\n') 