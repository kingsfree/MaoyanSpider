# -*- coding: utf-8 -*-

# Scrapy settings for Maoyan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Maoyan'

SPIDER_MODULES = ['Maoyan.spiders']
NEWSPIDER_MODULE = 'Maoyan.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Maoyan (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# 设置日志级别
LOG_LEVEL = 'DEBUG'
# LOG_FILE = 'maoyan.log'

# 设置导出编码 - 主要针对json文件
FEED_EXPORT_ENCODING = 'utf-8'


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "Cache-Control": "no-cache",
    # "Connection": "keep-alive",
    # "Cookie": "__mta=216317225.1573550114689.1574308886701.1574308887158.39; uuid_n_v=v1; uuid=EE214880052C11EA9BA7457F9B3430D3218F8263606342BCA97522209E25E62C; _lxsdk_cuid=16e5ee5458ec8-02632da9397983-514e291a-c0000-16e5ee5458ebb; _lxsdk=EE214880052C11EA9BA7457F9B3430D3218F8263606342BCA97522209E25E62C; Hm_lvt_465b947fcfe94866a0ef5b6db7ce7bdf=1573698770; _csrf=0afd8fd1922f394c5571d96f64488c34297e267f562aefc0486e2cf83f50eafa; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1574154475,1574305002; __mta=216317225.1573550114689.1574306106027.1574308597681.36; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1574308887; _lxsdk_s=16e8c1acdf8-dcf-a87-810%7C%7C17",
    # "Host": "maoyan.com",
    # "Pragma": "no-cache",
    # "Sec-Fetch-Mode": "navigate",
    # "Sec-Fetch-Site": "none",
    # "Sec-Fetch-User": "?1",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Maoyan.middlewares.MaoyanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Maoyan.middlewares.MaoyanDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Maoyan.pipelines.MaoyanPipeline': 300,
   'Maoyan.pipelines.MaoyanMysqlPipeline':200,
   'Maoyan.pipelines.MaoyanMongoPipeline':249,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 定义存入MySQL相关变量
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PWD = '123456'
MYSQL_DB = 'maoyandb'
MYSQL_CHAR = 'utf8'

# 定义mongodb常用变量
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'maoyandb'
MONGO_SET = 'filmtab'









