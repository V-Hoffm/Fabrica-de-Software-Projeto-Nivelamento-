import psycopg2 as ps # importa a biblioteca psycopg2 para realizar a conexão com o banco de dados postgresql
import os # importa a biblioteca os para realizar operações no sistema operacional
from dotenv import load_dotenv #importa a função load_dotenv da biblioteca dotenv para carregar as variaveis do .env

load_dotenv()

def get_conexao(): #função para conectar ao banco de dados com as variaveis do .env
    return ps.connect(
        database=os.getenv('database'),
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        port=os.getenv('port')
    )

def consulta_locais(cidade, tipo_objeto): #função para realizar a consulta de locais no banco que recebe a cidade e o tipo de objeto
    conexao = get_conexao() # conexao com o banco
    cursor = conexao.cursor() # criação do cursor conectado com o banco para realizar as operações
    comando_sql = "SELECT nome, tipo_objeto, endereco FROM fabricsoft.locais WHERE cidade = %s AND tipo_objeto ILIKE %s" #query para consultar com o %s como marcador de posição para inserir os dados de forma segura
    cursor.execute(comando_sql, (cidade, tipo_objeto)) # mandando o cursor executar o comando 
    resultados = cursor.fetchall() # traz o resultado em formato de lista de tuplas
    cursor.close() #fecha as conexões
    conexao.close()
    return resultados #retorna a lista de tuplas com a consulta

def salvar_solicitacao(nome, objeto, local, periodo):
    conexao = get_conexao()
    cursor = conexao.cursor()
    comando = "INSERT INTO fabricsoft.coletas (nome, objeto, local, periodo) VALUES (%s, %s, %s, %s)"
    cursor.execute(comando, (nome, objeto, local, periodo))
    conexao.commit() #para garantir que está tudo salvo no banco
    cursor.close()
    conexao.close()

def salvar_denuncia(local, hor, imagem_path, descricao):
    conexao = get_conexao()
    cursor = conexao.cursor()
    comando = "INSERT INTO fabricsoft.denuncias (local, horario, imagem, descricao) VALUES (%s, %s, %s, %s)"
    cursor.execute(comando, (local, hor, imagem_path, descricao))
    conexao.commit()
    cursor.close()
    conexao.close()

def salvar_review(coment):
    conexao = get_conexao()
    cursor = conexao.cursor()
    comando = "INSERT INTO fabricsoft.reviews (comentario) VALUES (%s)"
    cursor.execute(comando, (coment,))
    conexao.commit()
    cursor.close()
    conexao.close()