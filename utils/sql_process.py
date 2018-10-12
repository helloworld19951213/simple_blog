from datetime import datetime

import MySQLdb
import logging
from config import Config
import sys

__DBConfig__ = Config.DBConfig


class DbConn(object):
    def __init__(self, table):
        self.get_conn()
        self.table = table
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.NOTSET)

    def get_conn(self):
        connect = MySQLdb.connect(
            host=__DBConfig__.MYSQL_HOST,
            user=__DBConfig__.MYSQL_USER,
            passwd=__DBConfig__.MYSQL_PASSWD,
            db=__DBConfig__.MYSQL_DANAME,
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
            self.logger.info(sql)
            self.logger.info('insert sql:{0}'.format(sql))
            self.conn.cursor().execute(sql)
            self.conn.commit()
            self.logger.info(str(kwargs) + ' insert')
        except Exception:
            self.logger.error(sys.exc_info()[0:2])

    def close(self):
        self.conn.close()


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
