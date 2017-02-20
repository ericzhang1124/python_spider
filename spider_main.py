# !/usr/bin/env python
# coding:utf-8
import sys

sys.path.append('/Users/uxin/Eric/git_repository')

from python_spider import url_manager, html_downloader, html_parser,html_outputer


class SpiderMain(object):

	def __init__(self): # 初始化URL管理器、HTML下载器、HTML解析器、HTML存储器
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
	
	def crawl(self, root_url):# 启动爬虫
		count = 1
		page_url = 'http://baike.baidu.com'
		self.urls.add_new_url(root_url) # 将rooturl 添加到url管理器
		while self.urls.has_new_url(): # 如果url管理器存在 new_url 就返回True
			try:
				new_url = self.urls.get_new_url()  # 从URL管理器获取一个 
				print 'craw %d : %s' % (count, new_url)
				html_cont = self.downloader.download(new_url) # 使用下载器，下载从URL管理器取出的url
				new_urls, new_data = self.parser.parse(page_url, html_cont) # 使用解析器解析下载器下载下来的资源，将目标数据存储起来
				self.urls.add_new_urls(new_urls) # 用URL管理器存储新的URL列表
				self.outputer.collect_data(new_data) # 用输出存储器存储目标数据	

				if count == 100: 
					break

				count = count + 1
			except:
				print 'craw failed!'
		self.outputer.output_html() # 输出爬虫结果
		print self.urls.has_new_url()	

if __name__ == "__main__":
	root_url = "http://baike.baidu.com/item/Python" # 设置入口url
	obj_spider = SpiderMain() # 创建调度器实例
	obj_spider.crawl(root_url) # 启动爬虫