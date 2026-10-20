import sqlite3
import psycopg2
#DB_PATH = "banco_escola.db"
DB_PATH = "postgresql://neondb_owner:npg_nlE3YJiIQ2us@ep-sparkling-block-b6dkia0q-pooler.c-2.sa-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH)
    return conn