import logging
import os

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

from utils.config import Config

__COS_config__ = Config.COSConfig
__STATIC_BUCKET__ = __COS_config__.Bucket
__COS_REGION__ = __COS_config__.Region
__COS_KEY__ = __COS_config__.SecretKey
__COS_ID__ = __COS_config__.SecretId


class Cos(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.client()

    def client(self):
        config = CosConfig(
            Region=__COS_REGION__,
            SecretId=__COS_ID__,
            SecretKey=__COS_KEY__,

        )
        self.cos_client = CosS3Client(config)

    def upload(self, path, bucket):
        """

        :param path:  文件目录
        :param bucket: 上传的bucket
        :return:
        """
        if os.path.exists(path):
            response_msg = self.cos_client.upload_file(
                Bucket=bucket,
                LocalFilePath=path,
                Key=path.split('/')[-1],
                PartSize=10,
                MAXThread=10
            )
            print(response_msg['Etag'])
        else:
            self.logger.error(path + ' is not exist')


if __name__ == '__main__':
    c = Cos()
    c.upload(path='/opt/simple_blog/web_static/1', bucket=__STATIC_BUCKET__)
