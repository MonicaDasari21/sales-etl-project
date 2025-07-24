import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv('POSTGRES_USER')
DB_PASS = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')  # default to localhost
DB_PORT = os.getenv('POSTGRES_PORT', '5432')       # default PostgreSQL port
DB_NAME = os.getenv('POSTGRES_DB')

conn_str = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(conn_str)

data = {
    'order_id': [101, 102, 103],
    'product': ['Shirt', 'Jeans', 'Shoes'],
    'quantity': [2, 1, 4],
    'price': [29.99, 49.99, 79.99]
}

df = pd.DataFrame(data)

if __name__ == "__main__":
    print("Running ETL script...")
    print("Connecting to database and loading data...\n")
    print(df)
    df.to_sql('sales', engine, if_exists='replace', index=False)
    print("\n✅ Data loaded successfully into 'sales' table!")




