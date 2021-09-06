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

def add_movie(obj, token=None):
    if token:
        return obj.client.post(
            '/movie/add',
            data=json.dumps(dict(
                movie_name='Test Movie',
                movie_duration=100,
                poster_url='test.com/TestMovie'
            )),
            headers=dict(
                Authorization='Bearer ' + token
            ),
            content_type='application/json'
        )
    else:
        return obj.client.post(
            '/movie/add',
            data=json.dumps(dict(
                movie_name='Test Movie',
                movie_duration=100,
                poster_url='test.com/TestMovie'
            )),
            content_type='application/json'
        )


class TestMovieApis(BaseTestCase):

    def test_movie_add_not_admin(self):
        with self.client:
            register_response = register_user(self)
            reg_reponse_body = json.loads(register_response.data)
            auth_token = reg_reponse_body['Authorization']
            movie_reponse = add_movie(self, auth_token)
            self.assertEqual(movie_reponse.status_code, 401)
        
    def test_movie_no_user(self):
        with self.client:
            login_response = login_user(self)
            movie_reponse = add_movie(self)
            self.assertEqual(movie_reponse.status_code, 401)


if __name__ == '__main__':
    unittest.main()
