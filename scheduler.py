import time
from multiprocessing import Process
from update_database import update_db
from database_check import db_check


def schedule():
    while True:
        db_check()
        time.sleep(5)


if __name__ == '__main__':
    p1 = Process(target=update_db)
    p1.start()
    p2 = Process(target=schedule)
    p2.start()





