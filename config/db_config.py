from sqlalchemy import create_engine

# Replace "yourpassword" with your actual PostgreSQL password
DATABASE_URL = "postgresql://postgres:PPY_918aiguo@localhost/bitcoin_analysis"

def get_db_connection():
    """Returns a database connection."""
    return create_engine(DATABASE_URL)