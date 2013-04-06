# coding: utf-8
# author: Jove Yu <yushijun110[AT]gmail.com>
import os

ROOT_DIR = os.path.dirname(__file__)

if 'SERVER_SOFTWARE' in os.environ:
    import sae.const
    # SAE
    DEFAULT_FILE_STORAGE = 'saestorage.SaeStorage'
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': sae.const.MYSQL_DB, 
        'USER': sae.const.MYSQL_USER,
        'PASSWORD': sae.const.MYSQL_PASS,
        'HOST': sae.const.MYSQL_HOST,            
        'PORT': sae.const.MYSQL_PORT,                
    }
    }
else:
    # Local
    DEFAULT_FILE_STORAGE = 'saestorage.SaeStorage'
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'jovesky', 
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',            
        'PORT': '3306',                
    }
    }

# 邮箱（报错时发送）
EMAIL = 'yushijun110@gmail.com'

# 主题
THEME = 'jove'

# 站点名称
SITE_TITLE = 'JoveSky'
# 站点地址
SITE_URL = 'jovesky.com'
# 副标题
SITE_SUBTITLE = u'I love what I do'
# 作者
SITE_AUTHOR = 'Jove'
# 描述
SITE_DESC = 'Jove\'s personal site'

# 分页大小
PER_PAGE = 5
# recent 个数
RECENT_COUNT = 5
# feed 数量
FEED_COUNT = 10

# google 统计的 id
GA_ID = 'UA-15372596-1'

# 多说评论设置
DUOSHUO_SECRET = ''
DUOSHUO_SHORT_NAME = 'jovesky'


#SAE
ACCESS_KEY=''
SECRET_KEY=''
APP_NAME=''



#### 以下配置不要改动 ####
TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__), '../blog/theme/'+THEME+'/templates/'),
)
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), '../blog/theme/'+THEME+'/static/'),
)

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../uploads')
