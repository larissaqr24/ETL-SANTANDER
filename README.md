
# Projeto ETL Santander

Neste projeto individual, tivemos a oportunidade de criar uma ideia para um projeto ETL com base nas aulas que tivemos anteriormente.

O projeto será dividido em quatro partes.

## 1. Criação dos Dados
Nesta etapa, será criado um código para gerar dados fictícios a serem utilizados no projeto.

Os dados a serem gerados são:
- Nome
- CPF
- Email
- UF
- Telefone
- Idade
- Profissão

Os dados devem estar no idioma Português do Brasil.

Deve-se gerar dois arquivos, um em formato CSV e outro em formato Excel.

## 2. Extração dos Dados
Em outro módulo, crie um código que faça a leitura dos dois arquivos gerados anteriormente.

## 3. Transformação dos Dados
No mesmo módulo da extração, crie uma função para realizar a transformação dos dados. Nessa função, os dados dos dois arquivos lidos anteriormente devem ser passados como parâmetro, e a função deve retornar um DataFrame com os dados tratados.

Abaixo estão as etapas de tratamento dos dados:
- Concatenar as informações dos dois arquivos.
- Na coluna "Nome", remover qualquer abreviação (Srta, Sr, Dr, etc...).
  Exemplo: 
  - Entrada: Dra. Larissa Queiroz 
  - Saída: Larissa Queiroz 
- Na coluna "UF", filtrar apenas os estados das regiões nordeste e sudeste.
- Na coluna "Idade", filtrar apenas as pessoas maiores de idade.

## 4. Carregamento dos Dados
Com os dados tratados e retornados pela função, carregue-os em um arquivo final com o nome "Arquivo Final.xlsx".
