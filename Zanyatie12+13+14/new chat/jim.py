import json
import time


class JSONMessageEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class MessageBuilder:
    def __init__(self, msg):
        for key, val in msg.items():
            if isinstance(val, dict):
                sub_val = MessageBuilder(val)
                setattr(self, key, sub_val)
            else:
                setattr(self, key, val)

    def encode_to_json(self):
        return JSONMessageEncoder().encode(self)

    @staticmethod
    def get_object_of_json(json_obj):
        if json_obj:
            return json.JSONDecoder(object_hook=MessageBuilder).decode(json_obj)

    @staticmethod
    def create_presence_message(name, user_message, current_time=time.ctime()):
        return MessageBuilder({"teg": "presence_msg", "time": current_time,
                               "user":
                                   {"name": name,
                                    "status": "here"},
                               "message": user_message})

    @staticmethod
    def create_response_message(code, user_message):
        return MessageBuilder({"teg": "response_msg", "code": code, "message": user_message})
