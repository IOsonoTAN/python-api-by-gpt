# app/services/user_service.py
from app.models.user import User
from app import db

def get_user(user_id):
    return User.query.get(user_id)

def create_user(data):
    new_user = User(
        username=data['username'],
        email=data['email'],
        phone_number=data['phone_number'],
        gender=data['gender']
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_all_users(page=1, per_page=10):
    users = User.query.paginate(page=page, per_page=per_page, error_out=False)
    return {
        'users': [user.to_dict() for user in users.items],
        'total_pages': users.pages,
        'current_page': users.page,
        'per_page': users.per_page,
        'total_users': users.total
    }

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user.to_dict() if user else None
