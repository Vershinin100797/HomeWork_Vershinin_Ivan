import unittest

import server


class TestServer(unittest.TestCase):

    def test_parse_message(self):
        test_data = 'adasdadafgdfgdfgdgdgdgdgadsa'
        self.assertRaises(AttributeError, server.Server.parse_message(test_data))

    def test_send_message(self):
        self.assertRaises(AttributeError, server.Server.send_message(self, None))

    def test_send_response(self):
        self.assertRaises(AttributeError, server.Server.send_response(self, None))

if __name__ == '__main__':
    unittest.main()
