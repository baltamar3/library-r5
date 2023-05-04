import os

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    def __init__(self, bucket=None, *args, **kwargs):
        self.bucket_name = settings.AWS_MEDIA_BUCKET_NAME
        self.file_overwrite = False
        return super(MediaStorage, self).__init__(*args, **kwargs)
