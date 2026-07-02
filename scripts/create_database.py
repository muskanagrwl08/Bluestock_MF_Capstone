from pathlib import Path
from sqlalchemy import create_engine

# Project folder
project_path = Path(__file__).resolve().parent.parent

# Database path
db_path = project_path / "bluestock_mf.db"

# Create SQLite database
engine = create_engine(f"sqlite:///{db_path}")

# Test the connection
connection = engine.connect()
connection.close()

print("✅ SQLite database created successfully!")
print(f"Database location: {db_path}")