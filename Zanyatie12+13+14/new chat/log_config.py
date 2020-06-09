import logging


def chat_logger(func):
   def wrap_log(*args, **kwargs):
      name = func.__name__
      chat_log = logging.getLogger("chat_logs")
      chat_log.setLevel(logging.INFO)

      open_log = logging.FileHandler("chat_logs.log")
      format="%(asctime)-10s %(levelname)-5s %(module)s %(funcName)-5s %(message)s"
      formatter = logging.Formatter(format)
      open_log.setFormatter(formatter)
      chat_log.addHandler(open_log)

      chat_log.info('Function %s was called', name)
      func(*args, **kwargs)
      return func

   return wrap_log