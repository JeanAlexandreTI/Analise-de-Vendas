# %%
import pandas as pd

registro_vendas = {
    'Produto':['Garrafa','Caderno','Estojo','Folha A4'],
    'Data':['01/04/2020','03/08/2020','29/02/2021','07/04/2021'],
    'Qtde':[6, 6, 8, 9],
    'Preco':[15.00, 10.00, 7.00, 6.00]
}

df = pd.DataFrame(registro_vendas, index = None)
df
# %%
def total_vendido():
    print('===' * 15)
    print('Total Vendido'.center(45))
    print('===' * 15)

    for i in range(len(df)):
        print(f'{df['Produto'][i]} - R${df['Qtde'][i] * df['Preco'][i]}')

    print('===' * 15)


total_vendido()

# %%
def venda_unidade_preco():
    print('===' * 15)
    print('Mais Unidades Vendidas'.center(45))
    print('===' * 15)

    for i in range(len(df)):
        if df['Qtde'][i] == max(df['Qtde']):

            mais_unidade_dict ={
                'Produto':[ df['Produto'][i]],
                'Qtde': [df['Qtde'][i]],
                'Preco Unitario':[ df['Preco'][i]],
                'Preco Total': [df['Preco'][i] * df['Qtde'][i]]
            }

            tabela_mais_unidade = pd.DataFrame(mais_unidade_dict, index=None)
            print(tabela_mais_unidade)


    print('===' * 15)
    print('Maior Valor Vendido'.center(45))
    print('===' * 15)

    for i in range(len(df)):
        if df['Preco'][i] * df['Qtde'][i] == max(df['Preco'] * df['Qtde']):

            maior_preco_dict ={
                'Produto': [df['Produto'][i]],
                'Qtde': [df['Qtde'][i]],
                'Preco Unitario': [df['Preco'][i]],
                'Preco Total': [df['Preco'][i] * df['Qtde'][i]]
            }

            tabela_maior_preco = pd.DataFrame(maior_preco_dict)
            print(tabela_maior_preco)

    print('===' * 15)


venda_unidade_preco()

#%%
def filtro_mes():
    mes={
    "janeiro" : '01',
    "fevereiro" : '02',
    "março" : '03',
    "abril" : '04',
    "maio" : '05',
    "junho" : '06',
    "julho" : '07',
    "agosto" : '08',
    "setembro" : '09',
    "outubro" : '10',
    "novembro" : '11',
    "dezembro" : '12'
    }

    print('===' * 15)
    print(f'Escolha o numero referente ao mes que deseja filtrar:')
    for k, v in mes.items():
        print(f'{k.title()} - {v}')

    print('===' * 15)

    mes_escolhido = input('Opcao: ')

    indice = 0
    for i in df['Data']:
        mes_concat = i[3] + i[4]


        if mes_concat == mes_escolhido:
            valores = df.iloc[indice]
            print(pd.DataFrame(valores, index = None))
            indice += 1 

        else:
            indice += 1 
    

filtro_mes()
# %%
