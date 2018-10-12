import os
from pprint import pprint

class Monitor(object):
    def __init__(self):
        pass

    def get_io_info(self):
        all = os.popen('iostat').read().splitlines()
        full = [x for x in all if x != '' ]
        pprint(full)
        pass


if __name__ == '__main__':
    m = Monitor()
    m.get_io_info()
