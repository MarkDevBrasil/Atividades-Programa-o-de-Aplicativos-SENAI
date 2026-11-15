import mysql.connector

# conexão com o banco de dados
def conectar():

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="N/A",
        database="FuncionariosDB"
    )

    return conexao