# tests/test_user_routes.py
import json
import unittest
from app import app

class TestUserRoutes(unittest.TestCase):
    def test_get_user_route(self):
        client = app.test_client()
        response = client.get('/user/1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['user_id'], '1')
        # Add more assertions as needed

    def test_create_user_route(self):
        client = app.test_client()
        response = client.post('/user', json={'user_id': '2', 'username': 'jane_doe', 'email': 'jane.doe@example.com'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['user_id'], '2')
        # Add more assertions as needed

if __name__ == '__main__':
    unittest.main()
