import socket

from jim import MessageBuilder
from log_config import chat_logger


class Server:
    _server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connections = []

    def __init__(self, host='localhost', port=8888):
        self._server_socket.bind((host, port))
        print('Server start!')

    @chat_logger
    def run_server(self):
        while True:
            try:
                data, addr = self._server_socket.recvfrom(1024)

                if addr not in self.connections:
                    self.connections.append(addr)

                for client in self.connections:
                    parsed_msg = self.parse_message(data)
                    if addr != client:
                        self.send_message(client, parsed_msg.user.name, parsed_msg.message)
                    else:
                        self.send_response(client, code=200, message='OK')

            except Exception as ex:
                pass

    @staticmethod
    def parse_message(msg):
        if msg:
            msg = msg.decode("utf-8")
            parsed_msg = MessageBuilder.get_object_of_json(msg)
            return parsed_msg
        else:
            raise AttributeError('invalid attribute value!')

    def send_message(self, client, name='user', user_message='-'):
        if client:
            gen_msg = MessageBuilder.create_presence_message(name, user_message)
            gen_msg_json = gen_msg.encode_to_json()
            self._server_socket.sendto(gen_msg_json.encode("utf-8"), client)
        else:
            raise AttributeError('client is not set or has invalid data')

    def send_response(self, client, code=204, message='No Content '):
        if client:
            gen_response = MessageBuilder.create_response_message(code, message)
            gen_response_json = gen_response.encode_to_json()
            self._server_socket.sendto(gen_response_json.encode("utf-8"), client)
        else:
            raise AttributeError('client is not set or has invalid data')


if __name__ == '__main__':
    server = Server()
    server.run_server()
