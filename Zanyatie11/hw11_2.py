import sys
import threading
import time


class Locks(object):

    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.initial = initial

    def up(self):
        with self.lock:
            self.initial += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.initial == 0:
                self.lock.wait()
            self.initial -= 1


class Forks(object):

    def __init__(self, number):
        self.number = number
        self.user = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):
        with self.lock:
            while self.taken:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write(f"философ{user} взял вилку{self.number}\n")
            self.lock.notifyAll()

    def drop(self, user):
        with self.lock:
            while not self.taken:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write(f"философ{user} положил вилку{self.number}\n")
            self.lock.notifyAll()


class Philosopher (threading.Thread):

    def __init__(self, number, left, right, butler):
        threading.Thread.__init__(self)
        self.number = number
        self.left = left
        self.right = right
        self.butler = butler

    def run(self):
        for i in range(20):
            self.butler.down()
            time.sleep(0.2)
            self.left.take(self.number)
            time.sleep(0.2)
            self.right.take(self.number)
            time.sleep(0.2)
            self.right.drop(self.number)
            self.left.drop(self.number)
            self.butler.up()
        sys.stdout.write(f"Философ{self.number} закончил думать и есть\n")


def main():
    n = 5

    butler = Locks(n-1)

    c = [Forks(i) for i in range(n)]

    p = [Philosopher(i, c[i], c[(i+1) % n], butler) for i in range(n)]

    for i in range(n):
        p[i].start()


if __name__ == "__main__":
    main()
