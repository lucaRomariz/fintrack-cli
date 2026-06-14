import psycopg2

DATABASE_URL = "postgresql://postgres:romariz-miguel123456@db.mfmsahosljhpvkxcecyv.supabase.co:5432/postgres"

def get_connection():
    return psycopg2.connect(DATABASE_URL)