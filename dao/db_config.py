import sqlite3
import psycopg2
#DB_PATH = "banco_escola.db"
DB_PATH = "postgresql://neondb_owner:npg_xvXcHO2T3Zfj@ep-long-grass-bbx3sh1r-pooler.c-15.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH)
    return conn