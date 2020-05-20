import time
from threading import Thread, BoundedSemaphore, get_ident

__author__ = 'Вершинин Иван Александрович'
current_writer = None
current_readers = []
writers = []

s_writer = BoundedSemaphore(2)
s_reader = BoundedSemaphore(3)


def writing(interval):
    while True:
        s_writer.acquire()
        writers.append(get_ident())
        time.sleep(interval)
        writers.remove(get_ident())
        s_writer.release()


def reading(interval):
    while True:
        s_reader.acquire()
        current_readers.append(get_ident())
        time.sleep(interval)
        current_readers.remove(get_ident())
        s_reader.release()


def check(interval):
   global current_writer
   while True:
       if current_writer == writers[0]:
           current_writer = writers[1]
       else:
           current_writer = writers[0]
       print(f'Писатель {current_writer}, только что добавил новую запись')
       print(f'Сипсок читателей: {current_readers}')
       time.sleep(interval)


if __name__ == '__main__':
    writer_thread = (Thread(target=writing, args=(1,)) for _ in range(2))
    reader_thread = (Thread(target=reading, args=(3,)) for _ in range(5))
    check_thread = Thread(target=check, args=(3,))
    for t in writer_thread:
        t.start()
    for k in reader_thread:
        k.start()
    check_thread.start()
