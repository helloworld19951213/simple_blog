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
- Why:
  - 将所有配置信息放到一个统一管理的仓库，方便配置文件的管理，如果涉及多人协作、测试环境以及线上环境等因素，再通过gitignore来防止配置文件的混乱，降低一些 secretkey暴露的风险


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