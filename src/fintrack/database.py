import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

def get_connection():
    # 1. Buscamos a variável DENTRO da função, toda vez que ela for chamada
    database_url = os.getenv("DATABASE_URL")
    
    if not database_url:
        raise ValueError(
            "\n❌ ERRO: A variável 'DATABASE_URL' veio vazia!\n"
            "O Python não conseguiu ler o seu arquivo '.env'.\n"
            "Verifique se o arquivo se chama exatamente '.env' e está na raiz do projeto."
        )
        

    return psycopg2.connect(database_url)