from django.core.management.base import BaseCommand, CommandError
import os
import logging
from django.conf import settings
from utils.cos_file_storage import Cos
from utils.config import Config

__STATIC_PATH__ = settings.__getattr__('STATIC_ROOT')
__COS_config__ = Config.COSConfig
__STATIC_BUCKET__ = __COS_config__.Bucket


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
        __STATIC_DIR__ = os.path.join(currentDir, __STATIC_PATH__)
        cos = Cos()
        cos.upload(path=__STATIC_DIR__, bucket=__STATIC_BUCKET__)
