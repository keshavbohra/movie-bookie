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


class TestAuthApis(BaseTestCase):

    def test_registered_user_login(self):
        with self.client:
            register_response = register_user(self)
            response_data_register = json.loads(register_response.data)
            self.assertEqual(register_response.status_code, 201)
            self.assertTrue(response_data_register['Authorization'])
    
            login_response = login_user(self)
            response_data_login = json.loads(login_response.data)
            self.assertEqual(login_response.status_code, 200)
            self.assertTrue(response_data_login['Authorization'])
    
    def test_user_logout(self):
        with self.client:
            register_response = register_user(self)
            response_data_register = json.loads(register_response.data)
            self.assertEqual(register_response.status_code, 201)
            self.assertTrue(response_data_register['Authorization'])

            login_response = login_user(self)
            response_data_login = json.loads(login_response.data)
            self.assertEqual(login_response.status_code, 200)
            self.assertTrue(response_data_login['Authorization'])
        
            logout_reponse = self.client.post(
                '/auth/logout',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        login_response.data
                    )['Authorization']
                )
            )
            data = json.loads(logout_reponse.data)
            self.assertEqual(login_response.status_code, 200)
            self.assertEqual(data['status'], 'success')

if __name__ == '__main__':
    unittest.main()