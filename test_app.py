from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
    #ensure Flask was set up correctly
    def test_login(self):
        tester =  app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    #ensure index page loads correctly
    def test_index(self):
        tester =  app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertTrue(b'Welcome to our JTC exchange!' in response.data)

    #ensure that main page requires user login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertIn(b'This Exchange is By Invitation Only', response.data)

    #test incorrect login credentials
    def test_incorrect_login_page(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        ) 
        self.assertEqual(response.status_code, 404)

    def test_buy(float):
        tester = app.test_client(float)
        response = tester.get('/buy', content_type='html/text')
        float.assertEqual(response.status_code, 200)

    def test_sell(float):
        tester = app.test_client(float)
        response = tester.get('/sell', content_type='html/text')
        float.assertEqual(response.status_code, 200)
    

if __name__ == '__main__':
    unittest.__main__()
    