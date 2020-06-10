import unittest

import server


class TestServer(unittest.TestCase):

    def test_parse_message(self):
        test_data = 'adasdadafgdfgdfgdgdgdgdgadsa'
        self.assertRaises(AttributeError, server.Server.parse_message(test_data))


if __name__ == '__main__':
    unittest.main()
