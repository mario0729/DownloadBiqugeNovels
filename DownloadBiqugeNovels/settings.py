# -*- coding: utf-8 -*-

# Scrapy settings for DownloadBiqugeNovels project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
BOT_NAME = 'DownloadBiqugeNovels'

SPIDER_MODULES = ['DownloadBiqugeNovels.spiders']
NEWSPIDER_MODULE = 'DownloadBiqugeNovels.spiders'

#随机获得user_agent
USER_AGENT_LIST = ['zspider/0.9-dev http://feedback.redkolibri.com/',
                    'Xaldon_WebSpider/2.0.b1',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Mozilla/5.0 (compatible; Speedy Spider; http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Speedy Spider (Entireweb; Beta/1.3; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.2; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.1; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.0; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Beta/1.0; www.entireweb.com)',
                    'Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Speedy Spider (http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (http://www.entireweb.com)',
                    'Sosospider+(+http://help.soso.com/webspider.htm)',
                    'sogou spider',
                    'Nusearch Spider (www.nusearch.com)',
                    'nuSearch Spider (compatible; MSIE 4.01; Windows NT)',
                    'lmspider (lmspider@scansoft.com)',
                    'lmspider lmspider@scansoft.com',
                    'ldspider (http://code.google.com/p/ldspider/wiki/Robots)',
                    'iaskspider/2.0(+http://iask.com/help/help_index.html)',
                    'iaskspider',
                    'hl_ftien_spider_v1.1',
                    'hl_ftien_spider',
                    'FyberSpider (+http://www.fybersearch.com/fyberspider.php)',
                    'FyberSpider',
                    'everyfeed-spider/2.0 (http://www.everyfeed.com)',
                    'envolk[ITS]spider/1.6 (+http://www.envolk.com/envolkspider.html)',
                    'envolk[ITS]spider/1.6 ( http://www.envolk.com/envolkspider.html)',
                    'Baiduspider+(+http://www.baidu.com/search/spider_jp.html)',
                    'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
                    'BaiDuSpider',
                    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com',]
 
USER_AGENT = random.choice(USER_AGENT_LIST)

#初始化pipeline
ITEM_PIPELINES = {
    #'tutorial.pipelines.TextPipeline': 300,
    'DownloadBiqugeNovels.pipelines.MongoPipeline': 400,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DownloadBiqugeNovels (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DownloadBiqugeNovels.middlewares.DownloadbiqugenovelsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'DownloadBiqugeNovels.middlewares.DownloadbiqugenovelsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'DownloadBiqugeNovels.pipelines.DownloadbiqugenovelsPipeline': 300,
#}

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
