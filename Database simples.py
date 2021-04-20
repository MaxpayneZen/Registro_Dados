import sys
from time import sleep
import pandas as pd

banco = {}
dados = []

while True:
    print("\tOperações: \n [A] Adicionar \n [B] Busca nome \n [M] Mostrar todos os banco \n [S] Sair")
    
    operacao = str(input('O que deseja fazer:')).upper()
    
    if operacao == 'A' or operacao == 'ADICIONAR':
        n = str(input('Digite o nome: '))
        i = int(input('Digite a idade: '))
        banco["Nome"] = n
        banco["Idade"] = i
        dados.append(banco.copy())
        
    elif operacao== 'B' or operacao == 'BUSCA':
        buscaNome = input('Digite o nome que deseja buscar: ')
        for nome in dados:
            if buscaNome == nome:
                print("Achei")
        else:
            print('Nome nao encontrado! ')  
           
    elif operacao == 'M' or operacao == 'MOSTRAR':
          mN = pd.DataFrame(dados)
          print(mN)
          
    
    elif operacao == 'S' or operacao == 'SAIR':
        print('Volte Logo !!')
        sleep(1)
        sys.exit()
    else:
        print('Erro de escolha das operações!')
        for t in range(1):
            for l in range(1,18):
                print('- -', end=' ')
            sleep(0.5)
            print()
            
        
        