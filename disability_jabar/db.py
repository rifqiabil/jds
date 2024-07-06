import pandas as pd
from sqlalchemy import create_engine

# Konfigurasi koneksi database
DATABASE_URI = 'postgresql://postgres:postgres@5432/disability_jabar'

# Membuat engine koneksi
engine = create_engine(DATABASE_URI)

# Query untuk mengambil data dari tabel
query = 'SELECT * FROM disability_data'

# Mengambil data dari tabel ke dalam DataFrame pandas
df = pd.read_sql(query, engine)
