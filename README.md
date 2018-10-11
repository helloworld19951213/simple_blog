# simple_blog
一个简易blog

---
#### Usage
+ 1:  pip install -r requirements.txt
+ 2:  python manage.py makemigrations blog_app
+ 3:  python manage.py migrate
+ 4:  python manage.py createsuperuser
+ 5:  python manage.py runserver 0.0.0.0:8080
---


2018.10.11
- 添加配置文件 
  - utils/config.py
-- Usage:
例：在.config目录下新建一个  DBConfig.properties 


>DBConfig.properties
>

```python
# 不需要 引号 直接输入内容 调用时全部为str类型
MYSQL_HOST=127.0.0.1
MYSQL_DANAME=blog
MYSQL_USER=root
MYSQL_PASSWD=im7h322000
MYSQL_PORT=3306
```

>setting.py
>

```python
from utils.config import Config

DBinfo = Config.DBConfig  #你创建的配置文件名叫DBConfig 你就直接用Config调用你的文件名

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DBinfo.MYSQL_DANAME,
        'USER': DBinfo.MYSQL_USER,
        'PASSWORD': DBinfo.MYSQL_PASSWD,
        'HOST': DBinfo.MYSQL_HOST,
        'PORT': DBinfo.MYSQL_PORT,
    },
}
```