from django.core.management.base import BaseCommand, CommandError
import os
import logging
from django.conf import settings

__STATIC_PATH__ = settings.__getattr__('STATIC_ROOT')


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def handle(self, *args, **options):
        # 这里处理command的事物
        currentDir = os.path.dirname(os.path.abspath(__file__))
        while __STATIC_PATH__ not in os.listdir(currentDir):
            tmpDir = os.path.abspath(os.path.join(currentDir, u'..'))
            if tmpDir == currentDir:
                self.logger.error(__STATIC_PATH__ + ' not found　！！！！')
                break
            currentDir = tmpDir
