import pandas as pd

clientes1 = pd.read_csv("Dados_Clientes1.csv", encoding ="utf-8", sep = ';')
clientes2 = pd.read_excel("Dados_Clientes2.xlsx")

df = pd.concat([clientes1, clientes2]) 
abreviacoes = ['Dra.','Sra.','Dr. ','Sr. ','Srta. ']
for abreviacoes in abreviacoes:
    df['Nome']= df['Nome'].str.replace(abreviacoes,'',regex=False)

df['Nome'] = df['Nome'].str.strip() 
UF_desejados = ['Espírito Santo','Minas Gerais','Rio de Janeiro', 'São Paulo','Alagoas','Bahia','Ceará','Maranhão','Paraíba','Pernambuco','Piauí','Rio Grando do Norte','Sergipe']
df = df.loc[df['UF'].isin(UF_desejados)]

df = df.loc[(df['Idade']) >= 18]

df.to_excel('Arquivo Final.xlsx', index=False)

