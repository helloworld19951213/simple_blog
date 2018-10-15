from datetime import datetime

import MySQLdb
import logging
from utils.config import Config
import sys

__DBConfig__ = Config.DBConfig

MYSQL_HOST = __DBConfig__.MYSQL_HOST
MYSQL_DANAME = __DBConfig__.MYSQL_DANAME
MYSQL_USER = __DBConfig__.MYSQL_USER
MYSQL_PASSWD = __DBConfig__.MYSQL_PASSWD
MYSQL_PORT = __DBConfig__.MYSQL_PORT


class DbConn(object):
    def __init__(self, table):
        self.get_conn()
        self.table = table
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.NOTSET)
        self.sql = None

    def get_conn(self):
        connect = MySQLdb.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            db=MYSQL_DANAME,
            charset='utf8'
        )
        self.conn = connect

    def insert(self, **kwargs):
        try:
            fields = ''
            values = ''
            for key, value in kwargs.items():
                fields += key + ','
                values += '"{0}"'.format(str(value)) + ','

            fields = fields.rstrip(',')
            values = values.rstrip(',')
            sql = " insert into {0}".format(self.table) + "({0})".format(fields) + " values({0})".format(values)
            self.sql = sql
            self.logger.info(sql)
            self.logger.info('insert sql:{0}'.format(sql))
            self.conn.cursor().execute(sql)
            self.conn.commit()
            self.logger.info(str(kwargs) + ' insert')
        except Exception:
            self.logger.error(sys.exc_info()[0:2])

    def close(self):
        self.conn.close()

    def get_sql(self):
        print(self.sql)


if __name__ == '__main__':
    db = DbConn(table='monitor_memory')
    now = datetime.now()
    db.insert(
        minion_id=1,
        memory_total=1,
        memory_used=1,
        memory_free=1,
        memory_share=1,
        memory_bu_ca=1,
        memory_available=1,
        memory_time=datetime.strftime(now, ('%Y-%m-%d %H:%M:%S'))
    )
