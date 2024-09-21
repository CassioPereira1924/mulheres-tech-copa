'''print('Qual a sua idade?')
idade = int(input())

if idade >= 18:
    print('ACESSO LIBERADO! BOA FESTA!')
else:
    print('ACESSO NEGADO! VOCÊ É MENOR DE IDADE')'''

# CÓDIGO PARA LIBERAR ACESSO SOMENTE PARA MAIORES DE 19 ANOS

'''print('Qual a sua idade?')
idade = int(input())

if idade < 18:
    print('ACESSO NEGADO! VOCÊ É MENOR DE IDADE!')
elif idade == 18:
    print('VOCÊ ESTÁ QUASE LÁ! MAIS UM ANO E VOCÊ TERÁ ACESSO!')
else:
    print('ACESSO LIBERADO! BOA FESTA')'''

# código para verificar se o aluno esta aprovado


'''print('Digite a nota do primeiro bimestre:')   
B1 = float(input())  
print('Digite a nota do segundo bimestre:')   
B2 = float(input()) 
print('Digite a nota do terceiro bimestre:')   
B3 = float(input()) 
print('Digite a nota do quarto bimestre:')   
B4 = float(input()) 
media = (B1 + B2 + B3 + B4) / 4 
print('A média do aluno é ', media)

if media >= 7:
    print('PARABÉNS! VOCÊ ESTÁ APROVADO')
elif media >= 5:
    print('VOCÊ ESTÁ QUASE LÁ! VAMOS REALIZAR UMA RECUPERAÇÃO')
else:
    print('INFELIZMENTE VOCÊ FICOU REPROVADO!')'''


#CÓDIGO PARA VERIFICAR SE PODE PARTICIPAR DO MULHERES TECH

'''print('Qual seu gênero ? (F OU M)')     # Perguntando ao usuário qual seu gênero
genero = input().upper()                # criando variável genero e usando o comando input para o usuário digitar seu gênero e após usando o comando upper para transformar o que for digitado em letra maiúscula 
print('Qual município você mora? ')
municipio = input().lower()

if genero == 'F' and municipio == 'rio de janeiro':
    print('VOCÊ PODE PARTICIPAR DO MULHERES TECH')
else:
    print('VOCÊ NÃO PODE PARTICIPAR DO MULHERES TECH')'''


# CÓDIGO PARA LIBERAR ACESSO AO FILME PARA MAIORES DE 18 ANOS

print("*" *30 , 'BEM VINDO AO CINEMA SEVERIANO RIBEIRO', '*' * 30 )
print(' ')
print('Qual sua idade?')
idade = int(input())

if idade >= 18:
    print('ACESSO LIBERADO! BOM FILME\nAPROVEITE NOSSOS COMBOS DE PIPOCA COM REFRI DE 1 LITRO')

elif idade >= 16:
    print('O FILME SELECIONADO É PARA MAIORES DE 18 ANOS\nPARA ACESSAR PRECISA ESTAR ACOMPANHADO DE UM RESPOSÁVEL.\nVOCÊ ESTA COM SEU RESPOSÁVEL?')
    responsavel = input().upper()
    if responsavel == 'SIM':
        print('ACESSO LIBERADO! BOM FILME\nAPROVEITE NOSSOS COMBOS DE PIPOCA COM REFRI DE 1 LITRO')
    else:
        print('VOCÊ SÓ PODE VER O FILME ACOMPANHADO DE UM RESPONSÁVEL')

else:
    print('ACESSO NEGADO!\nVOCÊ É MENOR DE IDADE')




