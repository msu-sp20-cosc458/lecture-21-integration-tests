import app, unittest, flask_testing, requests

class ServerIntegrationTestCase(
    flask_testing.LiveServerTestCase
):
    def create_app(self):
        return app.app

    def test_server_sends_hello(self):
        response = requests.get(self.get_server_url())
        self.assertEqual(response.text, "Something goes here instead!")

if __name__ == '__main__':
    unittest.main()
