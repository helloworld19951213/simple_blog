import time
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from mdeditor.fields import MDTextField

from utils.make_thumb import create_thumb_pic


def user_directory_path(instance, filename):
    # 重命名 上传的图片名
    ext = filename.split('.')[-1]
    new_fileName = str(instance.id) + str(time.time() * 1000).split('.')[0][-10:] + '.' + ext
    return 'image/{0}/{1}/{2}'.format(datetime.now().year, datetime.now().month, new_fileName)


class UserProfile(AbstractUser):
    gender_choices = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(choices=gender_choices, default=0, verbose_name='性别')
    nickname = models.CharField(default='horSun', max_length=20, verbose_name='用户昵称')
    head_pic = models.ImageField(default='/static/my_beautf_self.jpg', verbose_name='头像', upload_to=user_directory_path)
    thumb_head_pic = models.ImageField(default='/static/thumbmy_beautf_self.jpg', null=True, blank=True,
                                       verbose_name='缩略图')

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        swappable = 'AUTH_USER_MODEL'

    @property
    def thumb_head(self):
        thumb_path = create_thumb_pic(self.head_pic)
        self.thumb_head_pic = thumb_path
        self.save()
        return thumb_path

    def __str__(self):
        return self.nickname


class BaseModel(models.Model):
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_show = models.BooleanField(default=True, verbose_name='是否显示')

    class Meta:
        abstract = True


class Blog(BaseModel):
    title = models.CharField(max_length=100, verbose_name='标题')
    author = models.ForeignKey(UserProfile, related_name='user_blog', verbose_name='作者')
    content = MDTextField(verbose_name='详细内容')
    tag = models.ForeignKey('BlogTag', verbose_name='文章分类')
    simple_content = models.CharField(verbose_name='概要', max_length=255)

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name
        db_table = 'blog_list'

    def __str__(self):
        return self.title


class BlogTag(BaseModel):
    name = models.CharField(max_length=10, verbose_name='类名')

    class Meta:
        verbose_name = '标签分类'
        verbose_name_plural = verbose_name
        db_table = 'blog_tag'

    def __str__(self):
        return self.name
