# db_init.py
from app import app, db

# Create the database tables within the application context
with app.app_context():
    # Create the database tables
    db.create_all()
