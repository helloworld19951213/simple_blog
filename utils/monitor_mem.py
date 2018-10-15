import os
from datetime import datetime

from utils.sql_process import DbConn


def run():
    now = datetime.now()
    cmd_mem = "/usr/bin/free -m | grep Mem"
    mem_list = os.popen(cmd_mem).read().splitlines()[0].split()
    db = DbConn('monitor_memory')
    db.insert(
        minion_id=os.popen('hostname').read().splitlines()[0],
        memory_total=mem_list[1],
        memory_used=mem_list[2],
        memory_free=mem_list[3],
        memory_share=mem_list[4],
        memory_bu_ca=mem_list[5],
        memory_available=mem_list[6],
        memory_time=datetime.strftime(now, ('%Y-%m-%d %H:%M:%S')),
    )
    db.close()
    print(db.get_sql())


if __name__ == '__main__':
    run()
