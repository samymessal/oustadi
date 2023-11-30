import psycopg2
from psycopg2 import sql
import os

# Database connection parameters
db_params = {
    "dbname": os.environ.get('POSTGRES_DB'),
    "user": os.environ.get('POSTGRES_USER'),
    "password": os.environ.get('POSTGRES_PASSWORD'),
    "host": "db"
}

# Connect to the database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Create tables
cur.execute("""
    CREATE TABLE IF NOT EXISTS embeddings (
        embedding_id SERIAL PRIMARY KEY,
        embedding_vector FLOAT[],
        type VARCHAR(255),
        reference_id INTEGER
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS files (
        file_id SERIAL PRIMARY KEY,
        file_content TEXT,
        embedding_id INTEGER REFERENCES embeddings(embedding_id)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS chapters (
        chapter_id SERIAL PRIMARY KEY,
        file_id INTEGER REFERENCES files(file_id),
        chapter_content TEXT,
        embedding_id INTEGER REFERENCES embeddings(embedding_id)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS prompts (
        prompt_id SERIAL PRIMARY KEY,
        prompt_text TEXT,
        embedding_id INTEGER REFERENCES embeddings(embedding_id)
    );
""")

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
