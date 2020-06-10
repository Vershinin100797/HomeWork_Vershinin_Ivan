import unittest

import client


class TestClient(unittest.TestCase):

    def test_parse_response(self):
        self.assertRaises(AttributeError, client.Client.parse_response(None))

    def test_sending(self):
        self.assertRaises(TypeError, client.Client.sending(self, client_name=123))

    def test_input_name_pass(self):
        test_data = 'test_name'
        self.assertEqual(client.input_name(test_data), test_data, 'invalid name type!')

    def test_input_name(self):
        test_data = 123
        self.assertEqual(client.input_name(test_data), test_data, 'invalid name type!')


if __name__ == '__main__':
    unittest.main()
