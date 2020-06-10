import socket
import threading
import time

from jim import MessageBuilder
from log_config import chat_logger


class Client:
    _client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ('localhost', 8888)
    shutdown = False
    join = False

    def __init__(self):
        self._client_socket.connect(self.server)

    @chat_logger
    def receiving(self):
        while not self.shutdown:
            try:
                while True:
                    data, addr = self._client_socket.recvfrom(1024)
                    self.parse_response(data)
                    time.sleep(0.2)
            except Exception as ex:
                print(f"Что-то пошло не так: {ex}")
                self.shutdown = True

    @staticmethod
    def parse_response(response):
        if response:
            response = response.decode("utf-8")
            parsed_data = MessageBuilder.get_object_of_json(response)
            if parsed_data.teg == "response_msg":
                print(f'Code: {parsed_data.code}. {parsed_data.message}!')
            elif parsed_data.teg == "presence_msg":
                print(f'\n[{parsed_data.user.name}]:: {parsed_data.message} ----- {parsed_data.time}')
            else:
                print('Something goes wrong!')
        else:
            raise AttributeError('invalid attribute value!')

    def sending(self, client_name):
        if isinstance(client_name, str):
            while not self.shutdown:
                if not self.join:
                    self._client_socket.sendto(f"[{client_name}] connected ".encode("utf-8"), self.server)
                    self.join = True
                else:
                    try:
                        message = input("[Your message] :: ")
                        if message:
                            gen_message = MessageBuilder.create_presence_message(client_name, message)
                            gen_message_json = gen_message.encode_to_json()
                            self._client_socket.sendto(gen_message_json.encode("utf-8"),  self.server)
                        time.sleep(0.2)
                    except Exception as ex:
                        print(f"Что-то пошло не так: {ex}")
                        self.shutdown = True
        else:
            raise TypeError('wrong variable type!')

    def __del__(self):
        self._client_socket.close()


def input_name(name):
    if isinstance(name, str):
        return name
    else:
        raise TypeError('invalid name type!')
        input_name()


if __name__ == '__main__':
    user_name = input("Name: ")

    client = Client()

    recv_thread = threading.Thread(target=client.receiving)
    recv_thread.start()
    client.sending(client_name=input_name(user_name))
    recv_thread.join()
