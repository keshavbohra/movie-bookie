import json
import unittest

from test.base import BaseTestCase

def register_user(obj):
    return obj.client.post(
        '/user/register',
        data=json.dumps(dict(
            email='client_test@test.com',
            username='client_test',
            password='password'
        )),
        content_type='application/json'
    )

def login_user(obj):
    return obj.client.post(
        '/auth/login',
        data=json.dumps(dict(
            email='client_test@test.com',
            password='password'
        )),
        content_type='application/json'
    )

def add_theatre(obj, token=None):
    if token:
        return obj.client.post(
            '/theatre/add',
            data=json.dumps(dict(
                theatre_name='Test Theatre',
                theatre_city='Test City',
                seats_num=50
            )),
            headers=dict(
                Authorization='Bearer ' + token
            ),
            content_type='application/json'
        )
    else:
        return obj.client.post(
            '/theatre/add',
            data=json.dumps(dict(
                theatre_name='Test Theatre',
                theatre_city='Test City',
                seats_num=50
            )),
            content_type='application/json'
        )


class TestTheatreApis(BaseTestCase):

    def test_theatre_add_not_admin(self):
        with self.client:
            register_response = register_user(self)
            reg_reponse_body = json.loads(register_response.data)
            auth_token = reg_reponse_body['Authorization']
            theatre_reponse = add_theatre(self, auth_token)
            self.assertEqual(theatre_reponse.status_code, 401)
        
    def test_theatre_no_user(self):
        with self.client:
            login_response = login_user(self)
            theatre_reponse = add_theatre(self)
            self.assertEqual(theatre_reponse.status_code, 401)


if __name__ == '__main__':
    unittest.main()
