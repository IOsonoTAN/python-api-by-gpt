# generate_mock_data.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from app.models.user import User

app = Flask(__name__)
app.config.from_object('app.config.Config')  # Make sure to adjust this based on your configuration
db = SQLAlchemy(app)
fake = Faker()

def generate_mock_users(num_records=100):
    users = []
    for _ in range(num_records):
        user_data = {
            'username': fake.user_name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'gender': fake.random_element(elements=('Male', 'Female', 'Other'))
        }
        user = User(**user_data)
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        generate_mock_users()
