from faker import Faker
import pandas as pd
import csv
import random

faker = Faker('pt_BR')

cabecalhos = ['Nome', 'CPF', 'Email', 'UF',
              'Telefone', 'Idade', 'Profissão']


# Gerando dados do arquivo CSV
with open('Dados_Clientes1.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv, delimiter=';')

    writer.writerow(cabecalhos)

    for x in range(3000):
        nome = faker.name()
        cpf = faker.cpf()
        email = faker.email()
        uf = faker.state()
        telefone = faker.phone_number()
        idade = random.randrange(16, 80)
        profissao = faker.job()
        writer.writerow([nome, cpf, email, uf, telefone,
                        idade, profissao])


# Gerando dados do arquivo Excel
registros = []

for x in range(3000):
    nome = faker.name()
    cpf = faker.cpf()
    email = faker.email()
    uf = faker.state()
    telefone = faker.phone_number()
    idade = random.randrange(16, 80)
    profissao = faker.job()

    registros.append([nome, cpf, email, uf, telefone, idade, profissao])

df = pd.DataFrame(registros, columns=cabecalhos)

df.to_excel('Dados_Clientes2.xlsx', index=False)
